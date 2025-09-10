
import os, re, json, yaml, datetime, hashlib, random
from pathlib import Path
from jinja2 import Template
from slugify import slugify
import feedparser, requests
from lxml import html
from markdownify import markdownify as md

# --- config with defaults ---
CFG  = yaml.safe_load(open("automation/bot_config.yaml", encoding="utf-8"))
TOP  = yaml.safe_load(open("automation/topics.yaml",   encoding="utf-8"))
TPL  = Template(open("automation/templates/post.md.j2", encoding="utf-8").read())

POSTS_PER_DAY = int(CFG.get("posts_per_day", 2))
MIN_WORDS     = int(CFG.get("min_words", 300))
TAGS          = CFG.get("tags", ["general"])
OUTDIR        = Path("site/content/posts")   # <- listable by themes
OUTDIR.mkdir(parents=True, exist_ok=True)

USER_AGENT = {"User-Agent":"Mozilla/5.0 (compatible; AutoBot/1.0)"}

def fetch_items(max_items_per_feed=20):
    rss = TOP.get("sources",{}).get("rss",[])
    items=[]
    for url in rss:
        try:
            d = feedparser.parse(url)
            for e in d.entries[:max_items_per_feed]:
                items.append({
                    "title": e.get("title","").strip(),
                    "url":   e.get("link","").strip(),
                    "summary": e.get("summary","").strip()
                })
        except Exception:
            continue
    # dedupe by title+url
    seen=set(); out=[]
    for it in items:
        if not it["title"] or not it["url"]: continue
        h=hashlib.sha1((it["title"]+it["url"]).encode()).hexdigest()
        if h in seen: continue
        seen.add(h); out.append(it)
    random.shuffle(out)
    return out

def extract_body(url, limit=6500):
    try:
        r = requests.get(url, timeout=8, headers=USER_AGENT)
        r.raise_for_status()
        tree = html.fromstring(r.content)
        # grab paragraphs; fall back to the whole document text
        paras = tree.xpath("//article//p//text() | //main//p//text() | //p//text()")
        text  = " ".join(p.strip() for p in paras if p and p.strip())
        if not text:
            text = tree.text_content()
        return md(text)[:limit]
    except Exception:
        return ""

def passes_quality(body:str)->bool:
    words = len(re.findall(r"\w+", body))
    if words < MIN_WORDS: return False
    if body.lower().count("http") > 25: return False
    return True

def make_post(item):
    raw = extract_body(item["url"])
    if not raw: return None
    body = re.sub(r'\n{3,}', '\n\n', raw).strip()
    if not passes_quality(body): return None

    slug = slugify(item["title"])[:80] or f"post-{datetime.datetime.utcnow().timestamp():.0f}"
    data = {
        "title": item["title"],
        "date": datetime.datetime.utcnow().isoformat()+"Z",
        "tags": json.dumps(TAGS),
        "description": (item["summary"] or item["title"])[:150],
        "canonical": item["url"],
        "intro": f"{item['title']} — summary and exam-relevant notes.",
        "bullets": "- Key insight 1\n- Key insight 2\n- Key insight 3",
        "body": body,
        "internal_links": "",
        "updated": datetime.date.today().isoformat(),
        "slug": slug
    }
    content = TPL.render(**data)
    fpath = OUTDIR / f"{slug}.md"
    with open(fpath,"w",encoding="utf-8") as f:
        f.write(content)
    return fpath

def seed_post():
    slug = f"seed-{datetime.date.today()}"
    fpath = OUTDIR / f"{slug}.md"
    if fpath.exists(): return
    with open(fpath,"w",encoding="utf-8") as f:
        f.write(f"""+++
title = "Seed post {datetime.date.today()}"
date = "{datetime.datetime.utcnow().isoformat()}Z"
tags = {json.dumps(TAGS)}
description = "Pipeline test"
+++

This is a seed post to verify the pipeline. Replace with real content on the next run.
""")

def main():
    made=0
    items = fetch_items()
    for it in items:
        if made >= POSTS_PER_DAY: break
        if make_post(it): made += 1

    if made == 0:
        seed_post()
    print(f"drafted {made} post(s)")

if __name__ == "__main__":
    main()

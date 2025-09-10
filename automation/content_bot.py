import os, re, json, yaml, datetime, hashlib
from pathlib import Path
from jinja2 import Template
from slugify import slugify
import feedparser, requests
from lxml import html
from markdownify import markdownify as md

CFG  = yaml.safe_load(open("automation/bot_config.yaml", encoding="utf-8"))
TOP  = yaml.safe_load(open("automation/topics.yaml",   encoding="utf-8"))
TPL  = Template(open("automation/templates/post.md.j2", encoding="utf-8").read())
TODAY_DIR = Path("site/content")/datetime.date.today().strftime("%Y/%m")

def fetch_items(max_items=30):
    items=[]
    for url in TOP.get("sources",{}).get("rss",[]):
        d = feedparser.parse(url)
        for e in d.entries[:max_items]:
            items.append({"title":e.get("title",""), "url":e.get("link",""), "summary":e.get("summary","")})
    # dedupe
    seen=set(); out=[]
    for it in items:
        h=hashlib.sha1((it["title"]+it["url"]).encode()).hexdigest()
        if h not in seen: seen.add(h); out.append(it)
    return out

def extract_body(url, limit=6000):
    try:
        r = requests.get(url, timeout=8, headers={"User-Agent":"Mozilla/5.0"})
        tree = html.fromstring(r.content)
        paras = tree.xpath("//p//text()")
        text  = " ".join(p.strip() for p in paras if p.strip())
        return md(text)[:limit]
    except: return ""

def passes_quality(body:str)->bool:
    words = len(re.findall(r"\w+", body))
    if words < CFG["min_words"]: return False
    # simple diversity check
    if body.lower().count("http") > 20: return False
    return True

def make_post(item, tags):
    raw = extract_body(item["url"])
    if not raw: return None
    # lightweight rewrite
    body = re.sub(r'\n{3,}', '\n\n', raw).strip()
    if not passes_quality(body): return None
    slug = slugify(item["title"])[:80]
    data = {
        "title": item["title"],
        "date": datetime.datetime.utcnow().isoformat()+"Z",
        "tags": json.dumps(tags),
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
    TODAY_DIR.mkdir(parents=True, exist_ok=True)
    f = TODAY_DIR/f"{slug}.md"
    open(f,"w",encoding="utf-8").write(content)
    return f

def main():
    made=0
    for it in fetch_items()[: CFG["posts_per_day"] * 5]:
        if made >= CFG["posts_per_day"]: break
        if make_post(it, CFG["tags"]): made += 1
    print(f"drafted {made} post(s)")

if __name__ == "__main__":
    main()

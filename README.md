# Auto Blog (Hugo + Netlify + GitHub Actions)

Flow: daily Action drafts posts -> opens PR -> you tap Merge -> Netlify deploys.

## Setup
1) Create GitHub repo (public).  
2) Add files below.  
3) Netlify: New site from Git, build=`hugo`, publish=`site/public`, env `HUGO_VERSION=0.128.0`.  
4) Edit `automation/topics.yaml`.  
5) Wait for daily PR or run workflow manually (Actions -> "Draft posts (PR)").

## Monetization
- Paste AdSense/Ezoic snippet in `site/layouts/partials/head.html`.
- Edit `automation/affiliates.yaml` and use shortcode `{{< aff "id" "Label" >}}`.

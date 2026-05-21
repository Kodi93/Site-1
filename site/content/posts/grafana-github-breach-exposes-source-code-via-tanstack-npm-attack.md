+++
title = "Grafana GitHub Breach Exposes Source Code via TanStack npm Attack"
date = "2026-05-21T14:04:02.820552Z"
tags = ["security", "certification"]
description = "Grafana Labs, on May 19, 2026, said an investigation into its recent breach found no evidence of customer production systems or operations being compr"
canonicalURL = "https://thehackernews.com/2026/05/grafana-github-breach-exposes-source.html"
+++

Grafana GitHub Breach Exposes Source Code via TanStack npm Attack — summary and exam-relevant notes.

## Key Points
- Key insight 1
- Key insight 2
- Key insight 3

## Details
Grafana Labs, on May 19, 2026, said an investigation into its recent breach found no evidence of customer production systems or operations being compromised. It said the scope of the incident is limited to the Grafana Labs GitHub environment, which includes public and private source code along with internal GitHub repositories. "After the initial assessment, we found that in addition to source code, the downloaded content included GitHub repositories that some Grafana Labs teams use to collaborate on and store internal operational information and other details about our business," it said . "This includes business contact names and email addresses that would be exchanged in a professional relationship context, not information pulled from or processed through the use of production systems or the Grafana Cloud platform." The open-source visualization software maker also noted that the breach originated from the TanStack npm supply chain attack orchestrated by TeamPCP, which also hit OpenAI and Mistral AI, and that it detected the activity on May 11, 2026. "We performed analysis and quickly rotated a significant number of GitHub workflow tokens, but a missed token led to the attackers gaining access to our GitHub repositories," it said. "A subsequent review confirmed that a specific GitHub workflow we originally deemed not impacted had, in fact, been compromised." The company said it subsequently received an extortion demand from an unnamed threat actor on May 16, but opted against paying the ransom as there is no guarantee that the stolen data would actually be deleted, and could act as a catalyst for future campaigns. Since then, Grafana has taken steps to rotate automation tokens, implement enhanced monitoring, audit all commits for signs of malicious activity, and bolster its overall GitHub security posture. It's worth mentioning here that a data extortion crew named CoinbaseCartel listed Grafana Labs on its dark web site on May 15, 2026. The Hacker News has contacted Grafana for comment, and we will update the story if we hear back. The development comes as GitHub said it's investigating unauthorized access to its internal repositories after the notorious threat actor known as TeamPCP listed the platform's source code and internal organizations for sale on a cybercrime forum. Learn practical strategies to detect and defend against cyber threats beyond zero-day vulnerabilities. Learn how to validate automated pentesting results for accurate security decisions. Get the latest news, expert insights, exclusive resources, and strategies from industry leaders, all for free.



{{< aff "training_partner" "Recommended course" >}}

{{< aff "vpn_vendor" "Try a VPN deal" >}}

*Updated: 2026-05-21*
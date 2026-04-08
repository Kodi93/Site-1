+++
title = "Axios NPM supply chain incident"
date = "2026-04-08T13:30:15.207832Z"
tags = ["security", "certification"]
description = "Overview of the recent Axios NPM supply chain incident including details of the payloads delivered from actor-controlled infrastructure."
canonicalURL = "https://blog.talosintelligence.com/axois-npm-supply-chain-incident/"
+++

Axios NPM supply chain incident — summary and exam-relevant notes.

## Key Points
- Key insight 1
- Key insight 2
- Key insight 3

## Details
Cisco Talos is actively investigating the March 31, 2026 supply chain attack on the official Axios node package manager (npm) package during which two malicious versions (v1.14.1 and v0.30.4) were deployed. Axios is one of the more popular JavaScript libraries with as many as 100 million downloads per week. Axios is a widely-deployed HTTP client library for JavaScript that simplifies HTTP requests, specifically for REST endpoints. The malicious packages were only available for approximately three hours, but if downloaded Talos strongly encourages that all deployments should be rolled back to previous known safe versions (v1.14.0 or v0.30.3). Additionally, Talos strongly recommends users and administrators investigate any systems that downloaded the malicious package for follow-on payloads from actor-controlled infrastructure. The primary modification of the packages introduced a fake runtime dependency (plain-crypto-js) that executes via post-install without any user interaction required. Upon execution, the dependency reaches out to actor-controlled infrastructure (142[.]11[.]206[.]73) with operating system information to deliver a platform-specific payload to Linux, MacOS, or Windows. On MacOS, a binary, “com.apple.act.mond”, is downloaded and run using zsh. Windows is delivered a ps1 file, which copies the legitimate powershell executable to “%PROGRAM DATA%\wt.exe”, and executes the downloaded ps1 file with hidden and execution policy bypass flags. On Linux, a Python backdoor is downloaded and executed. The payload is a remote access trojan (RAT) with typical associated capabilities allowing the actor to gather information and run additional payloads. As with most supply chain attacks, the full impact will likely take some time to uncover. The threat actors exfiltrated credentials along with remote management capabilities. Therefore, Talos strongly recommends organizations treat any credentials present on their systems with the malicious package as compromised and begin the process of rotating them as quickly as possible. Actors are likely to try to weaponize access as quickly as possible to maximize financial gain. Supply chain attacks tend to have unexpected downstream impacts, as these packages are widely used across a variety of applications, and the compromised credentials can be leveraged in follow-on attacks. For additional context, about 25% of the top 100 vulnerabilities in the Cisco Talos 2025 Year in Review affect widely used frameworks and libraries, highlighting the risk of supply chain-style attacks. Talos will continue to monitor any follow-on impacts from this supply chain attack in the days and weeks ahead, as well as any additional indicators that are uncovered as a result of our ongoing investigation. IP Address: 142[.]11[.]206[.]73 Domains: Sfrclak[.]com SHA256 e10b1fa84f1d6481625f741b69892780140d4e0e7769e7491e5f4d894c2e0e09 (setup[.]js) fcb81618bb15edfdedfb638b4c08a2af9cac9ecfa551af135a8402bf980375cf (Linux) 617b67a8e1210e4fc87c92d1d1da45a2f311c08d26e89b12307cf583c900d101 (Windows) 92ff08773995ebc8d55ec4b8e1a225d0d1e51efa4ef88b8849d0071230c9645a (MacOS) ed8560c1ac7ceb6983ba995124d5917dc1a00288912387a6389296637d5f815c (6202033.ps1) Cisco Talos updates this blog with additional IOCs, guidance, recommendations and timelines as of March 10, 2026. Cisco Talos is tracking the active exploitation of CVE-2026-20127, a vulnerability in Cisco Catalyst SD-WAN Controller, formerly vSmart, that allows an unauthenticated remote attacker to bypass authentication and obtain administrative privileges. Cisco Talos recently discovered a new threat actor, UAT-9221, leveraging VoidLink in campaigns. Their activities may go as far back as 2019, even without VoidLink. © Cisco Systems, Inc. and/or its affiliates. All rights
reserved. View our Privacy Policy.



{{< aff "training_partner" "Recommended course" >}}

{{< aff "vpn_vendor" "Try a VPN deal" >}}

*Updated: 2026-04-08*
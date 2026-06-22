+++
title = "MediaArea heap-based buffer overflow vulnerabilities"
date = "2026-06-22T14:51:26.929756Z"
tags = ["security", "certification"]
description = "Talos researchers find 4 heap-based buffer overflow vulnerabilities in MediaArea's MediaInfoLib."
canonicalURL = "https://blog.talosintelligence.com/mediaarea-heap-based-buffer-overflow-vulnerabilities/"
+++

MediaArea heap-based buffer overflow vulnerabilities — summary and exam-relevant notes.

## Key Points
- Key insight 1
- Key insight 2
- Key insight 3

## Details
Cisco Talos’ Vulnerability Discovery & Research team recently disclosed four vulnerabilities in MediaArea MediaInfoLib library. The vulnerabilities mentioned in this blog post have been patched by their respective vendor, in adherence to Cisco’s third-party vulnerability disclosure policy . For Snort coverage that can detect the exploitation of these vulnerabilities, download the latest rule sets from Snort.org , and our latest Vulnerability Advisories are always posted on Talos Intelligence’s website . Discovered by Dimitrios Tatsis of Cisco Talos. MediaArea produces digital media analysis open-source software, as well as support tools for file investigation. MediaInfoLib provides a UI for technical and tag data for video and audio media files. Talos discovered four vulnerabilities in MediaInfoLib. TALOS-2026-2367 (CVE-2026-25104), TALOS-2026-2368 (CVE-2026-25713), TALOS-2026-2371 (CVE-2026-28764), and TALOS-2026-2374 (CVE-2026-22554) are heap-based buffer overflow vulnerabilities in various functionalities of MediaInfoLib (version(s): 26.01). All can lead to arbitrary code execution. An attacker can provide a malicious file to trigger these vulnerabilities. Cisco Talos’ Vulnerability Discovery & Research team recently disclosed eight vulnerabilities in TP-Link, and one each in Adobe Photoshop, OpenVPN, and Gen Digital's Norton VPN. Cisco Talos’ Vulnerability Discovery & Research team recently disclosed one Foxit Reader vulnerability, and six LibRaw file reader vulnerabilities.
The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to Cisco’s third-party vulnerability disclosure policy.    
For Snort coverage that can detect Cisco Talos’ Vulnerability Discovery & Research team recently disclosed a vulnerability in HikVision, as well as 10 in TP-Link, and 19 in Canva.
The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to Cisco’s third-party vulnerability disclosure policy.
For © Cisco Systems, Inc. and/or its affiliates. All rights
reserved. View our Privacy Policy.



{{< aff "training_partner" "Recommended course" >}}

{{< aff "vpn_vendor" "Try a VPN deal" >}}

*Updated: 2026-06-22*
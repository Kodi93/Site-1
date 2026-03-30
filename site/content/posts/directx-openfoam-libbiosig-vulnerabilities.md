+++
title = "DirectX, OpenFOAM, Libbiosig vulnerabilities"
date = "2026-03-30T13:30:37.324762Z"
tags = ["security", "certification"]
description = "<p>Cisco Talos&#x2019; Vulnerability Discovery &amp; Research team recently disclosed vulnerabilities in the BioSig Project Libbiosig library and Open"
canonicalURL = "https://blog.talosintelligence.com/directx-openfoam-libbiosig-vulnerabilities/"
+++

DirectX, OpenFOAM, Libbiosig vulnerabilities — summary and exam-relevant notes.

## Key Points
- Key insight 1
- Key insight 2
- Key insight 3

## Details
Cisco Talos’ Vulnerability Discovery & Research team recently disclosed vulnerabilities in the BioSig Project Libbiosig library and OpenCFD OpenFOAM, as well as an unpatched vulnerability in Microsoft DirectX. The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to Cisco’s third-party vulnerability disclosure policy , apart from the DirectX vulnerability. For Snort coverage that can detect the exploitation of these vulnerabilities, download the latest rule sets from Snort.org , and our latest Vulnerability Advisories are always posted on Talos Intelligence’s website . Discovered by KPC of Cisco Talos. The Microsoft DirectX End-User Runtime installs runtime libraries from the legacy DirectX SDK for some certain games. It comes pre-installed on Windows XP Service Pack 2, Windows Server 2003 Service Pack 1, Windows Vista, Windows 7, Windows 8.0, Windows 8.1, Windows 10, and Windows Server equivalents. Talos discovered a local privilege escalation vulnerability in the installation process of DirectX End-User Runtime: TALOS-2025-2293 (CVE-2025-68623). A low-privileged user can replace an executable file during the installation process, which may result in unintended elevation of privileges. Discovered by Dimitrios Tatsis of Cisco Talos. OpenFOAM is an open-source computational fluid dynamics (CFD) software developed primarily by OpenCFD Ltd. Talos discovered TALOS-2025-2292 (CVE-2025-61982), an arbitrary code execution vulnerability in the Code Stream directive functionality of OpenCFD OpenFOAM 2506. A specially crafted OpenFOAM simulation file can lead to arbitrary code execution. An attacker can provide a malicious file to trigger this vulnerability. Discovered by Mark Bereza of Cisco Talos. BioSig is an open source software library for biomedical signal processing. The BioSig Project seeks to encourage research in biomedical signal processing by providing open source software tools. Libbiosig is a library dependency for BioSig. Talos discovered TALOS-2025-2323 (CVE-2025-64736), an out-of-bounds read vulnerability in the ABF parsing functionality of The Biosig Project libbiosig 3.9.2 and Master Branch (5462afb0). A specially crafted .abf file can lead to an information leak. An attacker can provide a malicious file to trigger this vulnerability. Talos also discovered two heap-based buffer overflow vulnerabilities, TALOS-2026-2361 (CVE-2026-22891) and TALOS-2026-2362 (CVE-2026-20777), in the Intan CLP parsing and Nicolet WFT parsing functionalities of the BioSig Project, respectively. A specially crafted CLP or WFT file can lead to arbitrary code execution. An attacker can provide a malicious file to trigger these vulnerabilities. Cisco Talos’ Vulnerability Discovery & Research team recently disclosed a vulnerability in HikVision, as well as 10 in TP-Link, and 19 in Canva.
The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to Cisco’s third-party vulnerability disclosure policy.
For Snort coverage Cisco Talos’ Vulnerability Discovery & Research team recently disclosed three vulnerabilities in Foxit PDF Editor, one in the Epic Games Store, and twenty-one in MedDream PACS. Cisco Talos’ Vulnerability Discovery & Research team recently disclosed vulnerabilities in Biosig Project Libbiosig, Grassroot DiCoM, and Smallstep step-ca.
The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to Cisco’s third-party vulnerability disclosure policy, except for Grassroot, as the DiCoM vulnerabilities © Cisco Systems, Inc. and/or its affiliates. All rights
reserved. View our Privacy Policy.



{{< aff "training_partner" "Recommended course" >}}

{{< aff "vpn_vendor" "Try a VPN deal" >}}

*Updated: 2026-03-30*
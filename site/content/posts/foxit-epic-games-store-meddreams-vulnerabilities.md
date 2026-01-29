+++
title = "Foxit, Epic Games Store, MedDreams vulnerabilities"
date = "2026-01-29T13:23:39.280176Z"
tags = ["security", "certification"]
description = "<p>Cisco Talos&#x2019; Vulnerability Discovery &amp; Research team recently disclosed three vulnerabilities in Foxit PDF Editor, one in the Epic Games"
canonicalURL = "https://blog.talosintelligence.com/foxi-and-epic-games/"
+++

Foxit, Epic Games Store, MedDreams vulnerabilities — summary and exam-relevant notes.

## Key Points
- Key insight 1
- Key insight 2
- Key insight 3

## Details
Cisco Talos’ Vulnerability Discovery & Research team recently disclosed three vulnerabilities in Foxit PDF Editor, one in the Epic Games Store, and twenty-one in MedDream PACS.. The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to Cisco’s third-party vulnerability disclosure policy . For Snort coverage that can detect the exploitation of these vulnerabilities, download the latest rule sets from Snort.org , and our latest Vulnerability Advisories are always posted on Talos Intelligence’s website . Discovered by KPC of Cisco Talos. Foxit PDF Editor is a popular PDF handling platform for editing, e-signing, and collaborating on PDF documents. Talos found three vulnerabilities: TALOS-2025-2275 (CVE-2025-57779) is a privilege escalation vulnerability in the installation of Foxit PDF Editor via the Microsoft Store. A low-privilege user can replace files during the installation process, which may result in elevation of privileges. TALOS-2025-2277 (CVE-2025-58085) and TALOS-2025-2278 (CVE-2025-59488)  are use-after-free vulnerabilities, one in the way Foxit Reader handles a Barcode field object, and one in the way Foxit Reader handles a Text Widget field object. A specially crafted JavaScript code inside a malicious PDF document can trigger these vulnerabilities, which can lead to memory corruption and result in arbitrary code execution. An attacker needs to trick the user into opening the malicious file to trigger these vulnerabilities. Exploitation is also possible if a user visits a specially crafted, malicious site if the browser plugin extension is enabled. Discovered by KPC of Cisco Talos. Epic Games Store is a storefront application for purchasing and accessing video games. Talos found TALOS-2025-2279 (CVE-2025-61973), a local privilege escalation vulnerability in the installation of Epic Games Store via the Microsoft Store. A low-privilege user can replace a DLL file during the installation process, which may result in elevation of privileges. Discovered by Marcin “Icewall” Noga of Cisco Talos. MedDream PACS server is a medical-integration system for archiving and communicating about DICOM 3.0 compliant images. Talos found 21 reflected cross-site scripting (XSS) vulnerabilities across several functions of MedDream PACS Premium 7.3.6.870. An attacker can provide a specially crafted URL to trigger these vulnerabilities, which can lead to arbitrary JavaScript code execution. Cisco Talos’ Vulnerability Discovery & Research team recently disclosed vulnerabilities in Biosig Project Libbiosig, Grassroot DiCoM, and Smallstep step-ca.
The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to Cisco’s third-party vulnerability disclosure policy, except for Grassroot, as the DiCoM vulnerabilities Cisco Talos’ Vulnerability Discovery & Research team recently disclosed an out-of-bounds read vulnerability in PDF XChange Editor, and ten vulnerabilities in Socomec DIRIS Digiware M series and Easy Config products.
The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to Cisco’s Cisco Talos’ Vulnerability Discovery & Research team recently disclosed five vulnerabilities in Dell ControlVault 3 firmware and its associated Windows software, four vulnerabilities in Entr'ouvert Lasso, and one vulnerability in GL.iNet Slate AX.
The vulnerabilities mentioned in this blog post have been patched by their respective vendors, © Cisco Systems, Inc. and/or its affiliates. All rights
reserved. View our Privacy Policy.



{{< aff "training_partner" "Recommended course" >}}

{{< aff "vpn_vendor" "Try a VPN deal" >}}

*Updated: 2026-01-29*
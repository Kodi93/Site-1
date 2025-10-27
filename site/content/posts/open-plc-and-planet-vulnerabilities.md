+++
title = "Open PLC and Planet vulnerabilities"
date = "2025-10-27T13:26:25.207864Z"
tags = ["security", "certification"]
description = "<p>Cisco Talos&#x2019; Vulnerability Discovery &amp; Research team recently disclosed one vulnerability in the OpenPLC logic controller and four vulne"
canonicalURL = "https://blog.talosintelligence.com/open-plc-and-planet-vulnerabilities/"
+++

Open PLC and Planet vulnerabilities — summary and exam-relevant notes.

## Key Points
- Key insight 1
- Key insight 2
- Key insight 3

## Details
Cisco Talos’ Vulnerability Discovery & Research team recently disclosed one vulnerability in the OpenPLC logic controller and four vulnerabilities in the Planet WGR-500 router. For Snort coverage that can detect the exploitation of these vulnerabilities, download the latest rule sets from Snort.org , and our latest Vulnerability Advisories are always posted on Talos Intelligence’s website . Discovered by a member of Cisco Talos. OpenPLC is an open-source programmable logic controller intended to provide a low cost industrial solution for automation and research. Talos researchers found TALOS-2025-2223 (CVE-2025-53476), a denial-of-service vulnerability in the ModbusTCP server functionality of OpenPLC\_v3. A specially crafted series of network connections can prevent the server from processing subsequent Modbus requests. An attacker can open a series of TCP connections to trigger this vulnerability. Discovered by Francesco Benvenuto of Cisco Talos. The Planet Networking & Communication WGR-500 is an industrial router designed for Internet of Things (IoT) networks, particularly industrial networks such as transportation, government buildings, and other public areas. Talos found four vulnerabilities in the router software. TALOS-2025-2226 (CVE-2025-54399-CVE-2025-54402) includes multiple stack-based buffer overflow vulnerabilities in the formPingCmd functionality. A specially crafted series of HTTP requests can lead to stack-based buffer overflow. TALOS-2025-2227 (CVE-2025-54403-CVE-2025-54404) includes multiple OS command injection vulnerabilities in the swctrl functionality. A specially crafted network request can lead to arbitrary command execution. TALOS-2025-2228 (CVE-2025-48826) is a format string vulnerability in the formPingCmd functionality of Planet WGR-500. A specially crafted series of HTTP requests can lead to memory corruption. TALOS-2025-2229 (CVE-2025-54405-CVE-2025-54406) includes multiple OS command injection vulnerabilities in the formPingCmd functionality. A specially crafted series of HTTP requests can lead to arbitrary command execution. Cisco Talos’ Vulnerability Discovery & Research team recently disclosed five vulnerabilities in Nvidia and one in Adobe Acrobat.
The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to Cisco’s third-party vulnerability disclosure policy.    
For Snort coverage that can detect the exploitation Cisco Talos’ Vulnerability Discovery & Research team recently disclosed ten vulnerabilities in BioSig Libbiosig, nine in Tenda AC6 Router, eight in SAIL, two in PDF-XChange Editor, and one in a Foxit PDF Reader.
The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence Cisco Talos’ Vulnerability Discovery & Research team recently disclosed seven vulnerabilities in WWBN AVideo, four in MedDream, and one in an Eclipse ThreadX module.
The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to Cisco’s third-party vulnerability disclosure policy.    
For Snort © Cisco Systems, Inc. and/or its affiliates. All rights
reserved. View our Privacy Policy.



{{< aff "training_partner" "Recommended course" >}}

{{< aff "vpn_vendor" "Try a VPN deal" >}}

*Updated: 2025-10-27*
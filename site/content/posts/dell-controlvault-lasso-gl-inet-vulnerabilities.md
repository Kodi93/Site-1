+++
title = "Dell ControlVault, Lasso, GL.iNet vulnerabilities"
date = "2025-12-17T13:28:36.707474Z"
tags = ["security", "certification"]
description = "<p>Cisco Talos&#x2019; Vulnerability Discovery &amp; Research team recently disclosed five vulnerabilities in Dell ControlVault 3 firmware and its ass"
canonicalURL = "https://blog.talosintelligence.com/dell-controlvault-lasso-gl-inet-vulnerabilities/"
+++

Dell ControlVault, Lasso, GL.iNet vulnerabilities — summary and exam-relevant notes.

## Key Points
- Key insight 1
- Key insight 2
- Key insight 3

## Details
Cisco Talos’ Vulnerability Discovery & Research team recently disclosed five vulnerabilities in Dell ControlVault 3 firmware and its associated Windows software, four vulnerabilities in Entr'ouvert Lasso, and one vulnerability in GL.iNet Slate AX. The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to Cisco’s third-party vulnerability disclosure policy . For Snort coverage that can detect the exploitation of these vulnerabilities, download the latest rule sets from Snort.org , and our latest Vulnerability Advisories are always posted on Talos Intelligence’s website . Discovered by Philippe Laulheret of Cisco Talos. The Dell ControlVault is a hardware-based security solution designed for user authentication functions. Talos reported five vulnerabilities, as follows: Discovered by Keane O'Kelley and another member of Cisco Advanced Security Initiative Group. Lasso is a free (GNU General Public License) C library that defines processes for federated identities, single sign-on, and related protocols. TALOS-2025-2193 (CVE-2025-47151) is a type confusion vulnerability, where a specially crafted SAML response can lead to an arbitrary code execution. TALOS-2025-2194 (CVE-2025-46404), TALOS-2025-2195 (CVE-2025-46784), and TALOS-2025-2196 (CVE-2025-46705) are denial of service vulnerabilities. Specially crafted SAML responses can lead to a denial of service in all three cases. Discovered by Lilith >\_> of Cisco Talos. Slate AX (GL-AXT1800) is a Wi-Fi 6GB travel router. Cisco Talos discovered a firmware downgrade vulnerability, TALOS-2025-2230 (CVE-2025-44018), in the OTA Update functionality. A specially crafted .tar file can lead to a firmware downgrade. An attacker can perform a man-in-the-middle attack to trigger this vulnerability. Cisco Talos’ Vulnerability Discovery & Research team recently disclosed an out-of-bounds read vulnerability in PDF XChange Editor, and ten vulnerabilities in Socomec DIRIS Digiware M series and Easy Config products.
The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to Cisco’s Cisco Talos’ Vulnerability Discovery & Research team recently disclosed three vulnerabilities in Dell BSAFE, two in Fade In screenwriting software, and one in Trufflehog.
The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to Cisco’s third-party vulnerability disclosure policy.    
For Snort Cisco Talos’ Vulnerability Discovery & Research team recently disclosed one vulnerability in the OpenPLC logic controller and four vulnerabilities in the Planet WGR-500 router.  
For Snort coverage that can detect the exploitation of these vulnerabilities, download the latest rule sets from Snort.org, and our latest Vulnerability Advisories are always © Cisco Systems, Inc. and/or its affiliates. All rights
reserved. View our Privacy Policy.



{{< aff "training_partner" "Recommended course" >}}

{{< aff "vpn_vendor" "Try a VPN deal" >}}

*Updated: 2025-12-17*
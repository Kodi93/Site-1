+++
title = "TruffleHog, Fade In and BSAFE Crypto-C vulnerabilities"
date = "2025-11-17T13:26:37.447327Z"
tags = ["security", "certification"]
description = "<p>Cisco Talos&#x2019; Vulnerability Discovery &amp; Research team recently disclosed three vulnerabilities in Dell BSAFE, two in Fade In screenwritin"
canonicalURL = "https://blog.talosintelligence.com/trufflehog-fade-in-and-bsafe-crypto-c-vulnerabilities/"
+++

TruffleHog, Fade In and BSAFE Crypto-C vulnerabilities — summary and exam-relevant notes.

## Key Points
- Key insight 1
- Key insight 2
- Key insight 3

## Details
Cisco Talos’ Vulnerability Discovery & Research team recently disclosed three vulnerabilities in Dell BSAFE, two in Fade In screenwriting software, and one in Trufflehog. The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to Cisco’s third-party vulnerability disclosure policy . For Snort coverage that can detect the exploitation of these vulnerabilities, download the latest rule sets from Snort.org , and our latest Vulnerability Advisories are always posted on Talos Intelligence’s website . Discovered by Piotr Bania of Cisco Talos. Fade In is a cross-platform text handling software for screenwriters. TALOS-2025-2250 (CVE-2025-53855) is an out-of-bounds write vulnerability in the XML parser functionality of GCC Productions Inc. Fade In 4.2.0. A specially crafted .fadein file can lead to an out-of-bounds write. TALOS-2025-2252 (CVE-2025-53814) is a use-after-free vulnerability in the XML parser functionality of GCC Productions Inc. Fade In 4.2.0. A specially crafted .xml file can lead to heap-based memory corruption. Discovered by Adam Reiser of Cisco ASIG. TruffleHog is a detection system for code repositories and ticket systems that finds exposed sensitive information, such as API keys and passwords. This vulnerability is described in an accompanying article on the Truffle Security website. The vuln is an arbitrary code execution vulnerability in the Git functionality of TruffleHog 3.90.2, TALOS-2025-2243 (CVE-2025-41390). A specially crafted repository can lead to a arbitrary code execution. An attacker can provide a malicious repository to trigger this vulnerability. Discovered by Jason Crowder. Dell BSAFE Crypto-C is FIPS-140 validated cryptography development kit for C/C++ environments. In cooperation with Jason Crowder, Talos published three vulnerabilities in the Dell BSAFE Crypto-C module. This product is at end of service; the vulnerable versions were added to an existing CVE. TALOS-2025-2140 (CVE-2019-3728) is an integer overflow vulnerability, and TALOS-2025-2141 (CVE-2019-3728) is an integer underflow vulnerability. In both cases, a specially crafted ASN.1 record can lead to an out-of-bounds read. An attacker can provide a malformed ASN.1 record to trigger this vulnerability. TALOS-2025-2142 (CVE-2019-3728) is a stack overflow vulnerability. A specially crafted ASN.1 record can lead to denial of service. Cisco Talos’ Vulnerability Discovery & Research team recently disclosed one vulnerability in the OpenPLC logic controller and four vulnerabilities in the Planet WGR-500 router.  
For Snort coverage that can detect the exploitation of these vulnerabilities, download the latest rule sets from Snort.org, and our latest Vulnerability Advisories are always Cisco Talos’ Vulnerability Discovery & Research team recently disclosed five vulnerabilities in Nvidia and one in Adobe Acrobat.
The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to Cisco’s third-party vulnerability disclosure policy.    
For Snort coverage that can detect the exploitation Cisco Talos’ Vulnerability Discovery & Research team recently disclosed ten vulnerabilities in BioSig Libbiosig, nine in Tenda AC6 Router, eight in SAIL, two in PDF-XChange Editor, and one in a Foxit PDF Reader.
The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence © Cisco Systems, Inc. and/or its affiliates. All rights
reserved. View our Privacy Policy.



{{< aff "training_partner" "Recommended course" >}}

{{< aff "vpn_vendor" "Try a VPN deal" >}}

*Updated: 2025-11-17*
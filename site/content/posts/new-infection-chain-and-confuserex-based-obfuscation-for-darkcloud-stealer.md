+++
title = "New Infection Chain and ConfuserEx-Based Obfuscation for DarkCloud Stealer"
date = "2025-09-13T13:14:49.184378Z"
tags = ["security", "certification"]
description = "<p>DarkCloud Stealer's delivery has shifted. We explore three different attack chains that use ConfuserEx obfuscation and a final payload in Visual Ba"
canonicalURL = "https://unit42.paloaltonetworks.com/new-darkcloud-stealer-infection-chain/"
+++

New Infection Chain and ConfuserEx-Based Obfuscation for DarkCloud Stealer — summary and exam-relevant notes.

## Key Points
- Key insight 1
- Key insight 2
- Key insight 3

## Details
Unit 42 researchers recently observed a shift in the delivery method in the distribution of DarkCloud Stealer and the obfuscation techniques used to complicate analysis. First seen in early April 2025, these new methods and techniques include an additional infection chain for DarkCloud Stealer. This chain involves obfuscation by ConfuserEx and a final payload written in Visual Basic 6 (VB6). We previously identified a series of attacks linked to the distribution of DarkCloud Stealer. It also leveraged AutoIt to bypass detection systems. We documented these details in DarkCloud Stealer: Comprehensive Analysis of a New Attack Chain That Employs AutoIt . Palo Alto Networks customers are better protected through the following products and services: If you think you might have been compromised or have an urgent matter, contact the Unit 42 Incident Response team . We have observed three slightly different attack chains delivering the same final DarkCloud Stealer payload in recent attacks. Each attack chain starts with a phishing email that contains either a tarball (TAR), Roshal (RAR) or a 7-Zip (7Z) archive. Both the TAR or RAR versions contain a JavaScript (JS) file, while the 7Z version contains a Windows Script File (WSF). The threat actor is at a point in development that, for all infection chain paths, almost every stage is obfuscated or protected. Figure 1 shows an overview of the different infection chains of these recent DarkCloud Stealer campaigns. In the chains initiated by a JS script, executing the script downloads and executes a PowerShell (PS1) file from an open directory server. The PS1 file then drops an executable (EXE) file that is the ConfuserEx -protected version of the final DarkCloud payload. Looking at the JS file here in Figure 2, the script is obfuscated by the tool javascript-obfuscator . Figure 3 below shows the deobfuscated version of the same script. In summary, the script: Figure 4 illustrates an open directory server hosting many malicious PS1 files. In this case, the kay.ps1 is the next stage PS1 sample that the JS script downloaded and executed. The infection chain initiated by a 7Z archive drops a WSF file. The WSF file mainly consists of a single  tag, which contains a



{{< aff "training_partner" "Recommended course" >}}

{{< aff "vpn_vendor" "Try a VPN deal" >}}

*Updated: 2025-09-13*
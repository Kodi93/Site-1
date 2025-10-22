+++
title = "New .NET CAPI Backdoor Targets Russian Auto and E-Commerce Firms via Phishing ZIPs"
date = "2025-10-22T13:27:39.776218Z"
tags = ["security", "certification"]
description = "Cybersecurity researchers have shed light on a new campaign that has likely targeted the Russian automobile and e-commerce sectors with a previously u"
canonicalURL = "https://thehackernews.com/2025/10/new-net-capi-backdoor-targets-russian.html"
+++

New .NET CAPI Backdoor Targets Russian Auto and E-Commerce Firms via Phishing ZIPs — summary and exam-relevant notes.

## Key Points
- Key insight 1
- Key insight 2
- Key insight 3

## Details
Cybersecurity researchers have shed light on a new campaign that has likely targeted the Russian automobile and e-commerce sectors with a previously undocumented .NET malware dubbed CAPI Backdoor . According to Seqrite Labs , the attack chain involves distributing phishing emails containing a ZIP archive as a way to trigger the infection. The cybersecurity company's analysis is based on the ZIP artifact that was uploaded to the VirusTotal platform on October 3, 2025. Present with the archive is a decoy Russian-language document that purports to be a notification related to income tax legislation and a Windows shortcut (LNK) file. The LNK file, which has the same name as the ZIP archive (i.e., "Перерасчет заработной платы 01.10.2025"), is responsible for the execution of the .NET implant ("adobe.dll") using a legitimate Microsoft binary named " rundll32.exe ," a living-off-the-land (LotL) technique known to be adopted by threat actors. The backdoor, Seqrite noted, comes with functions to check if it's running with administrator-level privileges, gather a list of installed antivirus products, and open the decoy document as a ruse, while it stealthily connects to a remote server ("91.223.75[.]96") to receive further commands for execution. The commands allow CAPI Backdoor to steal data from web browsers like Google Chrome, Microsoft Edge, and Mozilla Firefox; take screenshots; collect system information; enumerate folder contents; and exfiltrate the results back to the server. It also attempts to run a long list of checks to determine if it's a legitimate host or a virtual machine, and makes use of two methods to establish persistence, including setting up a scheduled task and creating a LNK file in the Windows Startup folder to automatically launch the backdoor DLL copied to the Windows Roaming folder. Seqrite's assessment that the threat actor is targeting the Russian automobile sector is down to the fact that one of the domains linked to the campaign is named carprlce[.]ru, which appears to impersonate the legitimate "carprice[.]ru." "The malicious payload is a .NET DLL that functions as a stealer and establishes persistence for future malicious activities," researchers Priya Patel and Subhajeet Singha said. AI adoption is surging—but without the right controls, it's chaos; learn how to turn security into your competitive edge. The future of GRC isn't coming—it's already here, powered by AI that learns, adapts, and audits itself. Get the latest news, expert insights, exclusive resources, and strategies from industry leaders – all for free.



{{< aff "training_partner" "Recommended course" >}}

{{< aff "vpn_vendor" "Try a VPN deal" >}}

*Updated: 2025-10-22*
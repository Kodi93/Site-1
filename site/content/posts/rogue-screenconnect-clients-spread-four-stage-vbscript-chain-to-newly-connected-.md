+++
title = "Rogue ScreenConnect Clients Spread Four-Stage VBScript Chain to Newly Connected Hosts"
date = "2026-09-08T13:03:39.646863Z"
tags = ["security", "certification"]
description = "Cybersecurity researchers have disclosed details of worm-like activity that abuses ConnectWise ScreenConnect to distribute a malicious Visual Basic Sc"
canonicalURL = "https://thehackernews.com/2026/09/rogue-screenconnect-clients-spread-four.html"
+++

Rogue ScreenConnect Clients Spread Four-Stage VBScript Chain to Newly Connected Hosts — summary and exam-relevant notes.

## Key Points
- Key insight 1
- Key insight 2
- Key insight 3

## Details
Cybersecurity researchers have disclosed details of worm-like activity that abuses ConnectWise ScreenConnect to distribute a malicious Visual Basic Script (VBScript) payload to newly connected systems. According to Huntress , three unrelated incidents have been found to use diverse initial access methods, namely a Quick Assist tech-support scam, a phishing-delivered MSI installer, and a fake Geek Squad refund form lure, to activate a four-stage VBScript chain that leads to rogue ScreenConnect installations. However, once the ScreenConnect instances were installed, the cybersecurity company said it observed the clients repeatedly spawning "wscript.exe" to execute VBScripts named 1.vbs, 2.vbs, 3.vbs, and 4.vbs. The incidents were observed in August 2026. The details of the three attacks are below - Across these incidents, the attack sequence is said to have followed a four-step process, with each VBScript launching the next and allowing it to progress further - At least three different payloads have been detected based on the state value - In addition, "%TEMP%\runner.ps1" takes steps to terminate every "wscript.exe" or "cscript.exe" process, and deletes the staging directory after the final stage is run. The 4.vbs script also writes the four VBScript files to "C:\Users\Public\Libraries\Default\Lib\Lib1" if the value in "%TEMP%\value.txt" is set to 010 or 011. This, in turn, triggers a round of payload deliveries, effectively turning the compromised host into a content-delivery mechanism for the malicious scripts every time the backdoored client observes a new Host connection. "This creates a worm-like behavior: propagating infections over new ScreenConnect connections. Connecting to an infected ScreenConnect client can cause the server-side Host system to receive and execute the same four-stage VBScript chain," Huntress said. "Later, the client records each ConnectionID to avoid repeatedly targeting the same active session, but then removes that identifier after it disconnects – allowing a later reconnection to trigger the infection again." "The incidents share additional indicators, including a WindowsServiceHost User Run Key pointing to WindowsServiceHost.vbs in the user's AppData directory," Huntress said, adding it observed other remote monitoring and management (RMM) tools, including UltraViewer, on some impacted hosts. On the other hand, the state value branch "011," which translates to: (1) no existing installation of ScreenConnect on the system, (2) Microsoft Defender is the only the endpoint protection program installed on the machine, and (3) no ScreenConnect clients are present, includes payloads to disable Microsoft Defender reporting, turn off Windows memory integrity, and runs an XMRig cryptocurrency miner. "Considering the extent and complexity of these attack chains, the Huntress SOC made strong recommendations that these affected hosts be re-imaged from known-good media, or a clean operating system install," Huntress said. In response to the findings, ConnectWise has issued an advisory , stating it has identified an issue affecting file transfer behavior in ScreenConnect Remote Access Support and Access sessions. The issue, it added, impacts both Cloud and On-Premise deployments. Until a fix is in place, customers are recommended to mitigate the risk by disabling the ability for technicians to transfer files - See how to test new CVEs against your environment, confirm what attackers can actually exploit, and fix the exposures that pose the greatest risk. Learn how to identify exploitable risk faster, prioritize what matters most, and reduce exposure before AI-powered attacks accelerate the threat. Get the latest news, expert insights, exclusive resources, and strategies from industry leaders, all for free.



{{< aff "training_partner" "Recommended course" >}}

{{< aff "vpn_vendor" "Try a VPN deal" >}}

*Updated: 2026-09-08*
+++
title = "KongTuke activity, (Tue, Nov 18th)"
date = "2025-11-19T13:26:33.788104Z"
tags = ["security", "certification"]
description = "Introduction&#xd;"
canonicalURL = "https://isc.sans.edu/diary/rss/32498"
+++

KongTuke activity, (Tue, Nov 18th) — summary and exam-relevant notes.

## Key Points
- Key insight 1
- Key insight 2
- Key insight 3

## Details
Introduction Today's diary is an example of KongTuke activity using fake CAPTCHA pages for a ClickFix -style lure. Also known as LandUpdate808 or TAG-124 and described as a sophisticated TDS system , KongTuke has been active since at least May 2024.  I keep track of this campaign through the infosec.exchange Mastodon instance, which is mostly information from the @monitorsg profile. With URLscan , I can pivot on the information from Mastodon to find compromised sites and generate infection traffic in my lab. On Monday, 2025-11-17, I found an example of a legitimate website with a KongTuke-injected script, and I generated some infection traffic. Details The image below shows an example of the fake CAPTCHA page and ClickFix style instructions. Shown above: Fake CAPTCHA page from a legitimate site with KongTuke-injected script, with the ClickFix style instructions and malicious command. The CAPTCHA page hijacks the clipboard, injecting text for a malicious command to download and run PowerShell script. Potential victims would read the instructions and paste this command into Run window. I tried this on a vulnerable Windows client in an Active Directory (AD) environment, and it ran PowerShell script that retrieved a zip archive containing a malicious Python script, as well as the Windows Python environment to run it. The malicious Python script generated HTTPS traffic to telegra[.]ph , but I was unable to determine the URL or content of the traffic. Shown above: Traffic from the infection, filtered in Wireshark. Shown above: Initial PowerShell script retrieved by the ClickFix command that was pasted into the Run window. Shown above: Final HTTP request from the initial infection traffic returned a zip archive containing a Python environment and a malicious Python script. Post-Infection Forensics The malicious Python package was saved to the Windows client under the user account's AppData\Roaming directory under a folder named DATA . A scheduled task kept the infection persistent. Shown above: The malicious Python script, made persistent on the infected Windows client through a scheduled task. Indicators from the infection The following URLs were generated during the initial infection traffic: For post-infection traffic, telegra[.]ph is a publishing tool that allows people to create and share simple web pages. I don't know the specific URL used for this infection, and the domain itself is not malicious. The following is the zip archive containing the Windows Python environment and the malicious Python script. Final Words I'm not sure what the script from this malicious Python package actually does.  If anyone knows what this is, feel free to leave a comment. --- Bradley Duncan brad [at] malware-traffic-analysis.net Login here to join the discussion.



{{< aff "training_partner" "Recommended course" >}}

{{< aff "vpn_vendor" "Try a VPN deal" >}}

*Updated: 2025-11-19*
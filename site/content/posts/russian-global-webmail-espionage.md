+++
title = "Russian Global Webmail Espionage"
date = "2026-07-30T13:31:39.730360Z"
tags = ["security", "certification"]
description = "<p>Unit 42 details a Russian cyberespionage campaign targeting  Zimbra webmail servers using JavaScript injection to steal credentials.</p>
<p>The pos"
canonicalURL = "https://unit42.paloaltonetworks.com/russian-webmail-espionage/"
+++

Russian Global Webmail Espionage — summary and exam-relevant notes.

## Key Points
- Key insight 1
- Key insight 2
- Key insight 3

## Details
Unit 42 has observed a persistent cyberespionage campaign we track as CL-STA-1114. This activity cluster overlaps with activity from a Russian threat actor tracked by other vendors as Void Blizzard and LAUNDRY BEAR. The attackers behind this campaign targeted Zimbra webmail in organizations in the following sectors: Unique to this campaign, the group leveraged zero-click phishing emails that exploit a vulnerability in the Zimbra Collaboration Suite (ZCS) webmail platform (CVE-2025-66376). The exploit automatically injects a malicious JavaScript payload without requiring recipient interaction. Once executed, the payload exfiltrates sensitive user data, including login credentials, email archives, and search histories. Threat actors continue to actively target unpatched ZCS instances using CVE-2025-66376. Palo Alto Networks customers are better protected from the threats discussed above through the following products: If you think you might have been compromised or have an urgent matter, contact the Unit 42 Incident Response team . The attackers behind CL-STA-1114 have been active since at least 2024 , and this campaign targeting Zimbra servers started in July 2025. Initial access starts with a phishing email that contains either an HTML attachment or embedded HTML in the message text. This lure is designed to catch recipients' attention with news headlines. Figure 1 shows an example of the lure used and a snippet of the underlying HTML code. The HTML text contains an obfuscated division with a Base64-encoded script (highlighted in red in Figure 1). The obfuscated section creates an invisible Scalable Vector Graphics (SVG) element that, upon loading, decodes the Base64-encoded script into a JavaScript payload that it injects into the victim’s browser. When executed, this JavaScript exfiltrates the victim’s Zimbra webmail data to a hard-coded command and control (C2) server. Exfiltrated data includes: Over the course of this campaign, we observed minimal changes to the JavaScript payload. Figure 2 illustrates the attack chain. Since we began tracking this campaign, there have been at least nine IP addresses and nine domains for the C2 servers. These servers were active for an average of 35.4 days. See the Indicators of Compromise (IoC) section for a list of the IP addresses and domains used in CL-STA-1114 activity. This campaign activity in CL-STA-1114 illustrates the persistent and evolving threat of state-sponsored cyberespionage. The attacker behind this activity targets widely used mail platforms like Zimbra, posing a risk to critical industries globally. This research highlights the need for vigilance, proactive patching and advanced threat detection to protect organizations. Network administrators, defenders and security researchers should patch vulnerable systems and use the IoCs below to investigate and strengthen defenses against CL-STA-1114 and similar activity. Palo Alto Networks customers are better protected from the threats discussed above through the following products: If you think you may have been compromised or have an urgent matter, get in touch with the Unit 42 Incident Response team or call: Palo Alto Networks has shared these findings with our fellow Cyber Threat Alliance (CTA) members. CTA members use this intelligence to rapidly deploy protections to their customers and to systematically disrupt malicious cyber actors. Learn more about the Cyber Threat Alliance . Subscribe for email updates to all Unit 42 threat research. By submitting this form, you agree to our Terms of Use and acknowledge our Privacy Statement. This site is protected by reCAPTCHA and the Google Privacy Policy and Terms of Service apply. Invalid captcha! By submitting this form, I understand my personal data will be processed in accordance with Palo Alto Networks Privacy Statement and Terms of Use. Copyright © 2026 Palo Alto Networks. All Rights Reserved



{{< aff "training_partner" "Recommended course" >}}

{{< aff "vpn_vendor" "Try a VPN deal" >}}

*Updated: 2026-07-30*
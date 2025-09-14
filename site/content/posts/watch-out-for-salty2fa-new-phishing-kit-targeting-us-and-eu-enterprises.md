+++
title = "Watch Out for Salty2FA: New Phishing Kit Targeting US and EU Enterprises"
date = "2025-09-14T13:14:11.549757Z"
tags = ["security", "certification"]
description = "Phishing-as-a-Service (PhaaS) platforms keep evolving, giving attackers faster and cheaper ways to break into corporate accounts. Now, researchers at "
canonicalURL = "https://thehackernews.com/2025/09/watch-out-for-salty2fa-new-phishing-kit.html"
+++

Watch Out for Salty2FA: New Phishing Kit Targeting US and EU Enterprises — summary and exam-relevant notes.

## Key Points
- Key insight 1
- Key insight 2
- Key insight 3

## Details
Phishing-as-a-Service (PhaaS) platforms keep evolving, giving attackers faster and cheaper ways to break into corporate accounts. Now, researchers at ANY.RUN has uncovered a new entrant: Salty2FA , a phishing kit designed to bypass multiple two-factor authentication methods and slip past traditional defenses. Already spotted in campaigns across the US and EU, Salty2FA puts enterprises at risk by targeting industries from finance to energy. Its multi-stage execution chain, evasive infrastructure, and ability to intercept credentials and 2FA codes make it one of the most dangerous PhaaS frameworks seen this year. Salty2FA's ability to bypass push, SMS, and voice-based 2FA means stolen credentials can lead directly to account takeover. Already aimed at finance, energy, and telecom sectors, the kit turns common phishing emails into high-impact breaches. ANY.RUN analysts mapped Salty2FA campaigns and found activity spanning multiple regions and industries, with the US and EU enterprises most heavily hit . Based on data from the ANY.RUN Sandbox and TI, Salty2FA activity began gaining momentum in June 2025, with early traces possibly dating back to March–April. Confirmed campaigns have been active since late July and continue to this day, generating dozens of fresh analysis sessions daily. One recent case analyzed by ANY.RUN shows just how convincing Salty2FA can be in practice. An employee received an email with the subject line "External Review Request: 2025 Payment Correction", a lure designed to trigger urgency and bypass skepticism. When opened in the ANY.RUN sandbox, the attack chain unfolded step by step: View real-world case of Salty2FA attack The email contained a payment correction request disguised as a routine business message. Join 15K+ enterprises worldwide that cut investigation time and stop breaches faster with ANY.RUN Get started now The link led to a Microsoft-branded login page, wrapped in Cloudflare checks to bypass automated filters. In the sandbox, ANY.RUN's Automated Interactivity handled the verification automatically, exposing the flow without manual clicks and cutting investigation time for analysts. Employee details entered on the page were harvested and exfiltrated to attacker-controlled servers. If the account had multi-factor authentication enabled, the phishing page prompted for codes and could intercept push, SMS, or even voice call verification. By running the file in the sandbox, SOC teams could see the full execution chain in real time, from the first click to credential theft and 2FA interception. This level of visibility is critical, because static indicators like domains or hashes mutate daily, but behavioral patterns remain consistent. Sandbox analysis gives faster confirmation of threats, reduced analyst workload, and better coverage against evolving PhaaS kits like Salty2FA. Salty2FA shows how fast phishing-as-a-service is evolving and why static indicators alone won't stop it. For SOCs and security leaders, protection means shifting focus to behaviors and response speed: By combining these measures, enterprises can turn Salty2FA from a hidden risk into a known and manageable threat. Enterprises worldwide are turning to interactive sandboxes like ANY.RUN to strengthen their defenses against advanced phishing kits such as Salty2FA. The results are measurable: With visibility into 88% of threats in under 60 seconds , enterprises get the speed and clarity they need to stop phishing before it leads to a major breach. Try ANY.RUN today : built for enterprise SOCs that need faster investigations, stronger defenses, and measurable results. App risks move fast—code-to-cloud visibility helps teams cut noise, gain control, and stop threats first. Shadow AI Agents are multiplying faster than governance can keep up—learn how to spot, stop, and secure them before they put your business at risk. Get the latest news, expert insights, exclusive resources, and strategies from industry leaders – all for free.



{{< aff "training_partner" "Recommended course" >}}

{{< aff "vpn_vendor" "Try a VPN deal" >}}

*Updated: 2025-09-14*
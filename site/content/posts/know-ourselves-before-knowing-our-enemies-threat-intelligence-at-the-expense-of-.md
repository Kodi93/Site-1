+++
title = "Know Ourselves Before Knowing Our Enemies: Threat Intelligence at the Expense of Asset Management"
date = "2025-11-17T13:26:37.381904Z"
tags = ["security", "certification"]
description = "<p>Effective cyber defense starts with knowing your own network. Unit 42 explains why asset management is the foundation of threat intelligence.</p>
<"
canonicalURL = "https://unit42.paloaltonetworks.com/asset-management/"
+++

Know Ourselves Before Knowing Our Enemies: Threat Intelligence at the Expense of Asset Management — summary and exam-relevant notes.

## Key Points
- Key insight 1
- Key insight 2
- Key insight 3

## Details
Cyber threat intelligence is often touted as a way to help defend an organization's IT environment. If we better understand the threats that might target our networks, we can better defend ourselves against those threats. This is true, but threat intelligence is only effective if an organization also properly manages its IT assets. Asset management consists of: While not entirely a security function, asset management should be at the base of any IT security pyramid. As I wrote in 2019 for SANS Internet Storm Center (ISC) , "Without inventory management, we cannot properly secure our infrastructure, because we don't fully understand everything on our network." An unknown or improperly managed host within an organization's network could provide a window for attackers to establish a foothold in the environment. Unfortunately, asset management isn't as exciting as the cyberthreats we face. Reading about a particular threat is often more intriguing than taking the practical steps needed to defend against it. I first noticed this as a volunteer handler at the ISC . During my time with the ISC, I frequently wrote diaries that provided examples of Windows-based malware infections and the associated indicators. My lab environment consisted of purposefully vulnerable hosts, so I ended these diaries with best practices to help protect against the threat. A key part of these final words included a statement advising that properly administered and up-to-date Windows hosts were much less likely to become infected. Readers would occasionally leave favorable comments about the technical content regarding the threats, but sometimes they commented on how frustrating it was to see the same preventative measures over and over again in my diaries. However, these preventative measures are the best security practices. When implemented, they were often effective against prominent malware families like Emotet and Qakbot (Qbot). In my diaries about these malware families, the samples in my lab could easily have been prevented through various vendors' endpoint security solutions. However, these malware families were responsible for millions of malware infections worldwide. In the 2023 takedown of Qakbot's infrastructure, the malware family was reportedly responsible for more than 700,000 infections . In a disruption of Emotet's infrastructure in 2021, it was reportedly responsible for over 1.6 million infections. Some of this can be attributed to the cat-and-mouse game of cybercriminals trying to stay ahead of security vendors. But many of these infections could've been detected or prevented with proper asset management. Knowing the threat posed by malware families like Emotet and Qakbot may be part of an effective defense, but without the bedrock of asset management, threat intelligence about those attacks is far less effective. The bedrock of asset management is necessary to better defend an organization against any IT threat. Although attacks have evolved, we see many time-honored tactics that remain the same. For example, an ongoing tactic is using SEO poisoning to deliver malware disguised as legitimate software. For an Akira ransomware infection in August 2025 , the initial access vector was SEO poisoning that led to a Bumblebee malware infection. This is a classic case of an initial infection leading to lateral movement and a domain controller takeover, where the attackers deployed ransomware across the network. My advice? Know ourselves before we know the enemy, because the enemy is always looking for weaknesses in our defense. Without comprehensive asset management, attackers can find avenues into our networks. Palo Alto Networks Unit 42 Attack Surface Assessment can help find these potential access paths before attackers can take advantage of them. Subscribe for email updates to all Unit 42 threat research. By submitting this form, you agree to our Terms of Use and acknowledge our Privacy Statement. Invalid captcha! By submitting this form, you agree to our Terms of Use and acknowledge our Privacy Statement . Copyright © 2025 Palo Alto Networks. All Rights Reserved



{{< aff "training_partner" "Recommended course" >}}

{{< aff "vpn_vendor" "Try a VPN deal" >}}

*Updated: 2025-11-17*
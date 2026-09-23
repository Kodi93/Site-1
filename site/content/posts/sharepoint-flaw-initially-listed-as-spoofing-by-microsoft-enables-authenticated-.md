+++
title = "SharePoint Flaw Initially Listed as Spoofing by Microsoft Enables Authenticated RCE"
date = "2026-09-23T13:04:09.906790Z"
tags = ["security", "certification"]
description = "A SharePoint Server vulnerability that Microsoft initially classified as a spoofing flaw with a CVSS score of 6.5 actually enables authenticated remot"
canonicalURL = "https://thehackernews.com/2026/09/sharepoint-flaw-initially-listed-as.html"
+++

SharePoint Flaw Initially Listed as Spoofing by Microsoft Enables Authenticated RCE — summary and exam-relevant notes.

## Key Points
- Key insight 1
- Key insight 2
- Key insight 3

## Details
A SharePoint Server vulnerability that Microsoft initially classified as a spoofing flaw with a CVSS score of 6.5 actually enables authenticated remote code execution, according to full technical details published today by Viettel Cyber Security researcher Dinh Ho Anh Khoa. The flaw, CVE-2026-65660 , affects SharePoint Server 2016, 2019, and Subscription Edition. Patches have been available since the August 11 security updates , and the National Vulnerability Database scores it 8.8. Microsoft's advisory describes CVE-2026-65660 as allowing an authorized attacker to perform spoofing and assigns no impact to integrity or availability. The CVE record that Microsoft publishes separately, updated on September 11, titles the same flaw a remote code execution vulnerability and says it allows an authorized attacker to execute code. Both records assign CWE-94, a code-injection weakness. Defenders who triaged CVE-2026-65660 based on the advisory saw a moderate spoofing flaw, not a code-execution vulnerability with a near-maximum score. Khoa is the researcher who demonstrated the original ToolShell exploit chain against SharePoint at Pwn2Own Berlin in May 2025. That chain was later exploited by Chinese state-backed groups and triggered emergency patches from Microsoft. The researcher has since disclosed several other SharePoint flaws, including CVE-2026-55040, an authentication bypass that attackers exploited shortly after its details became public in August. The latest CVE-2026-65660 vulnerability sits in how SharePoint checks whether server-side controls are on the SafeControls list, a filter that prevents dangerous classes from loading. When the ToolPane component processes web-part markup, it reconstructs Register directives by writing attribute values between double quotes without escaping quotes inside them. An attacker can inject additional directives through the unescaped quotes, registering arbitrary .NET classes after the type check runs but before the control is loaded. With arbitrary class loading, the attacker uses XamlServices.Parse() to trigger code execution through deserialization. The writeup includes a working in-memory webshell payload that avoids the registry permission failures other deserialization methods encounter, Khoa said. The researcher also demonstrated that the flaw can be chained with a separate, already-patched authentication bypass to reach pre-authentication remote code execution on servers configured to allow anonymous page access. Khoa says the bypass was fixed in a June 9 patch, and servers that applied the fix are not exposed to the pre-authentication path. No exploitation of CVE-2026-65660 has been reported in the wild, and the flaw is not in CISA's Known Exploited Vulnerabilities catalog. Microsoft's advisory rates exploitation as unlikely, though the full exploit markup is now public. Khoa says he has used the exploit in penetration testing engagements. The August 11 patch fixes the flaw and turns off the vulnerable function by default, according to the researcher. Khoa says the flaw also affects SharePoint 2013, though Microsoft's advisory lists only 2016, 2019, and Subscription Edition. SharePoint 2013 has been out of support since April 2023 and receives no security updates. AI agents are already operating inside enterprises with growing access to sensitive systems and data—while security teams still lack the visibility, controls, and governance to keep that access in check. Attackers are using AI to accelerate reconnaissance, compromise identities and escalate access. See how security teams can fight back with runtime identity controls. Get the latest news, expert insights, exclusive resources, and strategies from industry leaders, all for free.



{{< aff "training_partner" "Recommended course" >}}

{{< aff "vpn_vendor" "Try a VPN deal" >}}

*Updated: 2026-09-23*
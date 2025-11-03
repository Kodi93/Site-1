+++
title = "A phishing with invisible characters in the subject line, (Tue, Oct 28th)"
date = "2025-11-03T13:25:05.940256Z"
tags = ["security", "certification"]
description = "While reviewing malicious messages that were delivered to our handler inbox over the past few days, I noticed that the &#xe2;&#x20ac;&#x153;subject&#x"
canonicalURL = "https://isc.sans.edu/diary/rss/32428"
+++

A phishing with invisible characters in the subject line, (Tue, Oct 28th) — summary and exam-relevant notes.

## Key Points
- Key insight 1
- Key insight 2
- Key insight 3

## Details
While reviewing malicious messages that were delivered to our handler inbox over the past few days, I noticed that the “subject” of one phishing e-mail looked quite strange when displayed in the Outlook message list… As you can see, once the message was open, the subject was displayed as a normal, readable text. This suggested that some invisible characters were likely present… A quick look at the e-mail headers proved this to be the case. The subject was composed of the following two lines: This formatting meant that the subject was included in the message in a MIME “encoded-word” format, which is described in RFC 2047 as having the following structure[ 1 ]: In our case, the subject therefore consisted of two encoded words containing text written in the UTF-8 character set, which has been Base64 encoded. Once both lines were decoded, one could clearly see that an invisible character was indeed being used in multiple places in the strings – specifically the soft hyphen, which has a Unicode code point U+00AD, and which is more commonly used as the ­ HTML entity[ 2 ]. Although soft hyphens aren’t – strictly speaking – invisible, Outlook as well as most other e-mail clients don’t render them as visible text in most cases. The use of the soft hyphen character – combined with splitting the subject into multiple MIME encoded-words – was clearly intended as an attempt at bypassing e-mail filtering mechanisms that are supposed to automatically detect potentially malicious messages. Why is this approach noteworthy? Because although the use of invisible characters in phishing e-mails in general (and of the use of the “shy” character in particular[ 3 ]) is quite common when it comes to making the contents of e-mail messages less readable to security solutions, it is quite unusual to see it also applied to a subject of a message. In fact, the only allusion to this technique I’ve been able to find with a quick Google search was a general mention in an article by Microsoft Threat Intelligence from 2021, which states that “In several observed campaigns, attackers inserted invisible Unicode characters to break up keywords in an email body or subject line in an attempt to bypass detection and automated security analysis”[ 4 ]. Since the use of invisible characters in e-mail subject lines doesn’t seem to be widely known, I have therefore decided that it would be worthwhile to dedicate this short diary to it. It should be noted that the subject line wasn’t the only place where the soft hyphen character was used in the message – it was also heavily present in the text itself, where it was used to break up individual words… For completeness’s sake, we should also mention that the link in the phishing pointed to the URL hxxps[:]//stopsoriasis[.]co[.]il/Webmail/webmail.php?email=[ [email protected] ], where a generic “webmail login” credential stealing page was placed… [1] https://datatracker.ietf.org/doc/html/rfc2047 [2] https://en.wikipedia.org/wiki/Soft\_hyphen [3] https://isc.sans.edu/diary/31626 [4] https://www.microsoft.com/en-us/security/blog/2021/08/18/trend-spotting-email-techniques-how-modern-phishing-emails-hide-in-plain-sight/ ----------- Jan Kopriva LinkedIn Nettles Consulting Login here to join the discussion.



{{< aff "training_partner" "Recommended course" >}}

{{< aff "vpn_vendor" "Try a VPN deal" >}}

*Updated: 2025-11-03*
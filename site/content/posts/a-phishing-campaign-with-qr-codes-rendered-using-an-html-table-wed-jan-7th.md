+++
title = "A phishing campaign with QR codes rendered using an HTML table, (Wed, Jan 7th)"
date = "2026-01-07T13:14:43.717453Z"
tags = ["security", "certification"]
description = "Malicious use of QR codes has long been ubiquitous, both in the real world as well as in electronic communication. This is hardly surprising given tha"
canonicalURL = "https://isc.sans.edu/diary/rss/32606"
+++

A phishing campaign with QR codes rendered using an HTML table, (Wed, Jan 7th) — summary and exam-relevant notes.

## Key Points
- Key insight 1
- Key insight 2
- Key insight 3

## Details
Malicious use of QR codes has long been ubiquitous, both in the real world as well as in electronic communication. This is hardly surprising given that a scan of a QR code can lead one to a phishing page as easily as clicking a link in an e-mail. No more surprising is that vendors of security technologies have, over time, developed mechanisms for detecting and analyzing images containing QR codes that are included in e-mail messages[ 1 , 2 ]. These security mechanisms make QR code-based phishing less viable. However, due to the “cat and mouse” nature of cybersecurity, threat actors continually search for ways of bypassing various security controls, and one technique that can be effective in bypassing QR code detection and analysis in e-mail messages was demonstrated quite well in a recent string of phishing messages which made it into our inbox. The technique in question is based on the use of imageless QR codes rendered with the help of an HTML table. While it is not new by any stretch[ 3 ], it is not too well-known, and I therefore consider it worthy of at least this short post. Samples of the aforementioned phishing messages I have access to have been sent out between December 22nd and December 26th, and all of them had the same basic layout consisting of only a few lines of text along with the QR code. Although it looks quite normal (except perhaps for being a little “squished”), the QR code itself was – as we have indicated above – displayed not using an image but rather with the help of an HTML table made up of cells with black and white background colors, as you can see from the following code. Links encoded in all QR codes pointed to subdomains of the domain lidoustoo[.]click, and except for the very first sample from December 22nd, which pointed to onedrive[.]lidoustoo[.]click, all the URLs had the following structure: While the underlying technique of rendering QR codes using HTML tables is – as we’ve mentioned – not new, its appearance in a real-world phishing campaign is a useful reminder that many defensive controls still implicitly rely on assumptions about how malicious content is represented… And these assumptions might not always be correct. It is also a good reminder that purely technical security controls can never stop all potentially malicious content – especially content that has a socio-technical dimension – and that even in 2026, we will have to continue improving not just the technical side of security, but also user awareness of current threat landscape. [1] https://www.proofpoint.com/us/blog/email-and-cloud-threats/malicious-qr-code-detection-takes-giant-leap-forward [2] https://www.cloudflare.com/learning/security/what-is-quishing/ [3] https://media.defcon.org/DEF%20CON%2032/DEF%20CON%2032%20villages/DEF%20CON%2032%20-%20Adversary%20Vilage%20-%20Melvin%20Langvik%20-%20Evading%20Modern%20Defenses%20When%20Phishing%20with%20Pixels.pdf ----------- Jan Kopriva LinkedIn Nettles Consulting Login here to join the discussion.



{{< aff "training_partner" "Recommended course" >}}

{{< aff "vpn_vendor" "Try a VPN deal" >}}

*Updated: 2026-01-07*
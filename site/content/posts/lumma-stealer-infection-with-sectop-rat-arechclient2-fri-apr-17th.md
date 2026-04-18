+++
title = "Lumma Stealer infection with Sectop RAT (ArechClient2), (Fri, Apr 17th)"
date = "2026-04-18T13:25:47.857927Z"
tags = ["security", "certification"]
description = "Introduction&#xd;"
canonicalURL = "https://isc.sans.edu/diary/rss/32904"
+++

Lumma Stealer infection with Sectop RAT (ArechClient2), (Fri, Apr 17th) — summary and exam-relevant notes.

## Key Points
- Key insight 1
- Key insight 2
- Key insight 3

## Details
Introduction This diary provides indicators from a Lumma Stealer infection that was followed by Sectop RAT (ArechClient2). I searched for cracked versions of popular copyright-protected software, and I downloaded the initial malware after following the results of one such search. This is a common distribution technique for various families of malware, and I often find Lumma Stealer this way. In this case, the initial malware for Lumma Stealer was delivered as a password-protected 7-zip archive. The extracted malware is an inflated Windows executable (EXE) file at 806 MB. The EXE is padded with null-bytes (0x00), a technical which increases the EXE size while allowing the compressed archive file to be much smaller. The password-protected archive and inflated EXE file are designed to avoid detection. Images from the infection Shown above: Example of a page with instructions to download the initial malware file. Shown above: Traffic from the infection filtered in Wireshark. Shown above: Sectop RAT persistent on an infected Windows host. Indicators of Compromise Example of download link from the site advertising cracked versions of copyright-protected software: hxxps[:]//incolorand[.]com/how-visual-patch-enhances-ui-consistency-across-releases/?utm\_source={CID}&utm\_term=Adobe%20Premiere%20Pro%20(2026)%20Full%20v26.0.2%20Espa%C3%B1ol%20[Mega]&utm\_content={SUBID1}&utm\_medium={SUBID2} Example of URL for page with the file download instructions: hxxps[:]//mega-nz.goldeneagletransport[.]com/Adobe\_Premiere\_Pro\_%282026%29\_Full\_v26.0.2\_Espa%C3%B1ol\_%5BMega%5D.zip?c=ABUZ4WkRgQUA\_YUCAFVTFwASAAAAAACh&s=360721 Example of URL for file download from site above site impersonating MEGA: hxxps[:]//arch.primedatahost3[.]cfd/auth/media/JvWcFd5vUoYTrImvtWQAASTh/Adobe\_Premiere\_Pro\_(2026)\_Full\_v26.0.2\_Espa%C3%B1ol\_%5BMega%5D.zip Downloaded file: Extracted malware: Deflated malware: Lumma Stealer command and control (C2) domains from Triage sandbox analysis: Follow-up malware: Example of Sectop RAT C2 traffic from an infected Windows host: --- Bradley Duncan brad [at] malware-traffic-analysis.net Login here to join the discussion.



{{< aff "training_partner" "Recommended course" >}}

{{< aff "vpn_vendor" "Try a VPN deal" >}}

*Updated: 2026-04-18*
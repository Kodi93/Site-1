+++
title = "AutoIT Payload Injector , (Tue, Jul 28th)"
date = "2026-08-03T13:50:23.247730Z"
tags = ["security", "certification"]
description = "For a long time, AutoIT&#x5b;1&#x5d; has been pretty common in the malware ecosystem. Threat actors still use it because it&#x27s easy to write and po"
canonicalURL = "https://isc.sans.edu/diary/rss/33192"
+++

AutoIT Payload Injector , (Tue, Jul 28th) — summary and exam-relevant notes.

## Key Points
- Key insight 1
- Key insight 2
- Key insight 3

## Details
For a long time, AutoIT[ 1 ] has been pretty common in the malware ecosystem. Threat actors still use it because it’s easy to write and powerful. Indeed, it can perform all the required actions to inject a payload into a remote process as you’ll see below. Since last week, I detected a wave of similar emails that deliver the same kind of payload. The example I'll cover started with a fake bank email containing a RAR archive ( "Bank\_account\_details.rar" - SHA256:5c4ca58e41c009c664a7134df12b0fdc0815f572e117fe67ca35582f19d9deab). The archive contains a VBS script (SHA256:f88d9094a90f7000a3fb2cd7c981e03357ce2b39df9de5ee1d0742e619e3860f) This first script is pretty simple: it decodes a Base64 payload, dumps it on disk with a random name and invokes a PowerShell interpreter to decompress it (I beautified the script a bit): Once unzipped, the VBS will execute the dumped script. Another PowerShell will be invoked to dump three new files on disk: These files are Base64 encoded and XOR with the keys 0x02 and 0x3D: PowerShell will then invoke the following command: Persistence is added via a classic Run key: vijewyufveonabghulluonouceyasi.exe is an AutoIT3 interpreter (SHA256: bdd2b7236a110b04c288380ad56e8d7909411da93eed2921301206de0cb0dda1) “wwman” is the AutoIT script that will perform the injection of the shellcode stored in Ennnn: This script will decode the shellcode (XOR key 0xEC), launch a charmap.exe, inject and launch the payload via the following API calls: Yes, AutoIT is able to invoke any API call! The process charmap.exe is the legitimate executable file for the Character Map utility built into Microsoft Windows. It allows you to view, select, and copy special symbols, accented characters, or unique glyphs from any installed font to your clipboard. To wrap up the infection chain: The shellcode will deliver a VIPKeylogger[ 2 ] malware that will talk to cphost17[.]qhoster[.]net. It seems that AutoIT is back on stage because I found another malware analysis report that describes the same infection path[ 3 ]. [1] https://www.autoitscript.com/site/ [2] https://malpedia.caad.fkie.fraunhofer.de/details/win.vipkeylogger [3] https://www.blackfog.com/medusahvnc-a-hidden-desktop/ Xavier Mertens (@xme) Senior ISC Handler | SANS Principal Instructor | Freelance Consultant Xameco | PGP Key Login here to join the discussion.



{{< aff "training_partner" "Recommended course" >}}

{{< aff "vpn_vendor" "Try a VPN deal" >}}

*Updated: 2026-08-03*
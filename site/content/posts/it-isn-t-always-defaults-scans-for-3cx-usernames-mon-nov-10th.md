+++
title = "It isn't always defaults: Scans for 3CX usernames, (Mon, Nov 10th)"
date = "2025-11-13T13:27:19.208977Z"
tags = ["security", "certification"]
description = "Today, I noticed scans using the username "FTP&#x5f;3cx" showing up in our logs. 3CX is a well-known maker of business phone system software &#x5b;1&#"
canonicalURL = "https://isc.sans.edu/diary/rss/32464"
+++

It isn't always defaults: Scans for 3CX usernames, (Mon, Nov 10th) — summary and exam-relevant notes.

## Key Points
- Key insight 1
- Key insight 2
- Key insight 3

## Details
Today, I noticed scans using the username "FTP\_3cx" showing up in our logs. 3CX is a well-known maker of business phone system software [1]. My first guess was that this was a default user for one of their systems. But Google came up empty for this particular string. The 3CX software does not appear to run an FTP server, but it offers a feature to back up configurations to an FTP server [2]. The example user used in the documentation is "3cxftpuser", not "FTP\_3cx". Additionally, the documentation notes that the FTP server can run on a different system from the 3CX software. For a backup, it would not make much sense to have it all run on the same system. The scans we are seeing likely target FTP servers users set up to back up 3CX configurations, and not the 3CX software itself. I am not familiar enough with 3CX to know precisely what the backup contains, but it most likely includes sufficient information to breach the 3CX installation. The credentials we observe with our Cowrie-based honeypots are collected for telnet and ftp. In particular, on Linux systems, you often use a system user to connect via FTP. Any credentials working via FTP will also work for telnet or SSH. Keep that in mind when configuring a user for FTP access, and of course, FTP should not be your first choice for backing up sensitive data, but we all know it does happen. Here are the passwords attacks are attempting to use: Here are some other "3cx" related usernames we have seen in the past: If anyone with more 3CX experience reads this, is there a reason for someone to use these usernames? Or are there any defaults I didn't find? [1] https://www.3cx.com [2] https://www.3cx.com/docs/ftp-server-pbx-backups-linux/ -- Johannes B. Ullrich, Ph.D. , Dean of Research, SANS.edu Twitter | Login here to join the discussion.



{{< aff "training_partner" "Recommended course" >}}

{{< aff "vpn_vendor" "Try a VPN deal" >}}

*Updated: 2025-11-13*
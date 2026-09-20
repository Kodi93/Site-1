+++
title = "MacOS 27 - First Boot, (Tue, Sep 15th)"
date = "2026-09-20T13:03:24.095421Z"
tags = ["security", "certification"]
description = "I have not done this type of diary in a while: What traffic will you see from a system on boot, before a user logs in&#x3f; I just took a quick look a"
canonicalURL = "https://isc.sans.edu/diary/rss/33340"
+++

MacOS 27 - First Boot, (Tue, Sep 15th) — summary and exam-relevant notes.

## Key Points
- Key insight 1
- Key insight 2
- Key insight 3

## Details
I have not done this type of diary in a while: What traffic will you see from a system on boot, before a user logs in? I just took a quick look at macOS 27 "Golden Gate" to see what traffic you should expect. Here are some of the highlights: I captured about 300 packets. This was likely inflated for this particular system as it connected via Wi-Fi and wired network interfaces. Each network interface will do its own DHCP/IP discovery during boot. I only used router advertisements for IPv6, not DHCPv6. As it is supposed to, macOS 27 does standard compliant duplicate address discovery before accepting an IPv6 address. It does use ICMPv6 nonces to prevent some spoofing DoS attacks: :: > ff02::1:ff8f:bd1c ICMPv6 86  Neighbor Solicitation for fe80::14e5:ff56:308f:bd1c Internet Control Message Protocol v6 Type: Neighbor Solicitation (135) Code: 0 Checksum: 0xd8bb [correct] [Checksum Status: Good] Reserved: 00000000 Target Address: fe80::14e5:ff56:308f:bd1c ICMPv6 Option (Nonce) Type: Nonce (14) Length: 1 (8 bytes) Nonce: 30480a0a9b7c macOS 27 resolved these hostnames during boot: TCP options have not changed for a few years now in macOS. macOS 27 still uses the somewhat more conservative window scale of "6". It also still uses ECN and random timestamps. I recorded four TCP connection during boot: Just like prior macOS versions, macOS 27 does advertise any services via multicast DNS on port 5353/udp During boot, the only visible user-agent is contained in the OCSP request: com.apple.trustd/3.0. The user agent is the same as prior versions of macOS. The user agent for Safari is: Mozilla/5.0 (Macintosh; Intel Mac OS X 10\_15\_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/27.0 Safari/605.1.15 The version of Safari is indicated as "27.0", but oddly enough, the OS version states "Intel Mac OS X 10\_15\_7" (this was collected from a Mac with "M" CPU). -- Johannes B. Ullrich, Ph.D. , Dean of Research, SANS.edu Twitter | Login here to join the discussion.



{{< aff "training_partner" "Recommended course" >}}

{{< aff "vpn_vendor" "Try a VPN deal" >}}

*Updated: 2026-09-20*
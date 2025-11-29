+++
title = "Unicode: It is more than funny domain names., (Wed, Nov 12th)"
date = "2025-11-29T13:20:15.477234Z"
tags = ["security", "certification"]
description = "When people discuss the security implications of Unicode, International Domain Names (IDNs) are often highlighted as a risk. However, while visible an"
canonicalURL = "https://isc.sans.edu/diary/rss/32472"
+++

Unicode: It is more than funny domain names., (Wed, Nov 12th) — summary and exam-relevant notes.

## Key Points
- Key insight 1
- Key insight 2
- Key insight 3

## Details
When people discuss the security implications of Unicode, International Domain Names (IDNs) are often highlighted as a risk. However, while visible and often talked about, IDNs are probably not what you should really worry about when it comes to Unicode. There are several issues that impact application security beyond confusing domain names. At first sight, Unicode is a standard that assigns numbers to characters [1]. It extends the ASCII standard, which only allowed for 127 different characters, to an essentially unlimited range of characters. With Unicode, we also have various encoding schemes, such as UTF-8 and UTF-16, that regulate how the respective code is expressed as a multi-byte value. Unicode version 17.0 defines 159,801 different characters. This includes not only characters for various languages but also emojis and math symbols. Here are some of the issues that are often overlooked: When discussing domain names, one issue that arises is the use of characters that are easily confused. The Unicode project has a tool to identify them [2]. But this issue goes beyond domain names. If you allow the full Unicode character set for usernames, users may be able to impersonate other users on your platform. This has frequently happened on X [3]. However, other platforms, such as internal messaging systems, could also be abused in similar ways. These techniques aim to address the issue that some systems are unable to represent the entire Unicode character range, but offer similar characters that can be used to represent these "missing" characters. The "confusable" tool mentioned above is also helpful to identify them. In its worst form, this could convert an otherwise harmless character, like a "FULLWIDTH GRAVE ACCENT", into a single quote, bypassing filters to prevent injection vulnerabilities. The key defense is to avoid any conversion after a string has passed input validation. However, unintentional conversion can happen on some platforms as data is inserted into databases. "Variant Selectors" are non-printable ("invisible") Unicode code points that are used to specify an alternate representation of a given character. They may be used by first specifying a "normal" character, followed by a variant selector, and then an alternative character, such as an emoji. There are sixteen possible variant selectors. Selector-16 (#FE0F) would be used to define an emoji representation for a given character. Variant selectors were recently abused in the "Glass Worm" attack against VS Code extensions. In this case, variant selectors were used because they are not visible; they were used solely to encode obfuscated code snippets. The "Glass Worm" used sequences of variant selectors without following them up with an alternative glyph, which is not standard-compliant. Usually, each variant selector should be followed by a glyph. Most languages are written/read left to right, and this is the default in most operating systems and editors. However, some languages use right-to-left. Unicode defines a "right-to-left (0x200F)" and "left-to-right (0x200E)" mark to indicate the direction. The direction may be changed at any point in the document. There are a few other Unicode code points that allow swapping the direction text is rendered (0x202A-E). Different text directions can be abused to make code reviews more difficult. A human reviewer will typically not see the change in direction, while a compiler or interpreter will, and as a result the code execution is different from what the human reviewer observed. There is a nice demo of this issue at trojansource.code [5] [1] https://unicode.org/ [2] https://util.unicode.org/UnicodeJsps/confusables.jsp [3] https://isc.sans.edu/diary/28440 [4] https://www.koi.ai/blog/glassworm-first-self-propagating-worm-using-invisible-code-hits-openvsx-marketplace [5] https://trojansource.codes/ -- Johannes B. Ullrich, Ph.D. , Dean of Research, SANS.edu Twitter | Login here to join the discussion.



{{< aff "training_partner" "Recommended course" >}}

{{< aff "vpn_vendor" "Try a VPN deal" >}}

*Updated: 2025-11-29*
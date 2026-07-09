+++
title = "Tracing Digital Intent: New MacOS Tahoe 26 Artifact Discovered"
date = "2026-07-09T13:53:32.907387Z"
tags = ["security", "certification"]
description = "<p>Unit 42 has discovered a new macOS Tahoe 26 forensic artifact that tracks user menu selections across the operating system. Learn more here. </p>
<"
canonicalURL = "https://unit42.paloaltonetworks.com/new-macos-artifact-discovered/"
+++

Tracing Digital Intent: New MacOS Tahoe 26 Artifact Discovered — summary and exam-relevant notes.

## Key Points
- Key insight 1
- Key insight 2
- Key insight 3

## Details
Forensic examiners are constantly hunting for data that reveals not just what happened on a system, but the user's intent behind it. With the release of macOS Tahoe 26, a new artifact has surfaced that provides exactly this level of granularity. We have identified a new Biome stream, App.MenuItem , which logs specific menu selections made by users across the operating system. This artifact offers a step-by-step record of user actions — from compressing files to emptying the trash — providing critical context for user activity across the operating system. This blog outlines where to find this artifact, how to process it and what stories the data can tell. The Apple Biome system has long been a gold mine for forensic investigators, tracking everything from app usage to media consumption. In macOS Tahoe 26.x, Apple appears to have introduced a new stream specifically designed to track menu selections, likely to facilitate user suggestions or learning behavior. The artifact is located at ~/Library/Biome/streams/restricted/App.MenuItem/local . Unlike simple logs, this file contains SEGB-encapsulated protobuf entries. SEGB is the file format used by the Biome. While this format requires specific tooling to parse, the payoff is significant. The stream captures the exact text of menu items selected by the user, along with the timestamp of the activity, providing a narrative of their interaction with the interface. Because standard forensic tools may not yet parse this specific stream, examiners can utilize open-source tools like ccl-segb to extract the raw data. In our testing, this artifact is not parsed by the most common commercially available digital forensic tools available. To process the file: The true value of App.MenuItem lies in its ability to reconstruct a user's workflow. Where a file system event might simply show a file was deleted, this artifact can show the deliberate action of selecting "Move to Trash" followed by "Empty Trash.” Consider the following sequence of events observed in our sample analysis: In this scenario, we see a clear pattern: data creation, compression (likely for exfiltration) and subsequent cleanup. We even see interaction with specific UI elements, such as Copy and Paste Item later in the timeline. While powerful, this artifact is not without limitations. It relies on the menu item text itself. If a menu option does not explicitly contain the file or folder name (e.g., a generic "Open" command vs. "Compress 'Report'"), the specific target of the action might not be visible in this stream alone. However, when correlated with file system logs, App.MenuItem provides the "human" context that technical logs often miss. The discovery of the App.MenuItem artifact in MacOS Tahoe 26 adds a powerful new layer to forensic investigations. By capturing the specific menu choices a user makes, examiners can reconstruct digital intent with greater precision than before. Whether you are investigating data exfiltration or trying to understand a sequence of events, this Biome stream provides a narrative view of user behavior. As macOS continues to evolve, so must our forensic methodologies. We encourage all examiners working with Tahoe images to verify if this artifact is present and incorporate it into their standard analysis workflows. Subscribe for email updates to all Unit 42 threat research. By submitting this form, you agree to our Terms of Use and acknowledge our Privacy Statement. This site is protected by reCAPTCHA and the Google Privacy Policy and Terms of Service apply. Invalid captcha! By submitting this form, I understand my personal data will be processed in accordance with Palo Alto Networks Privacy Statement and Terms of Use. Copyright © 2026 Palo Alto Networks. All Rights Reserved



{{< aff "training_partner" "Recommended course" >}}

{{< aff "vpn_vendor" "Try a VPN deal" >}}

*Updated: 2026-07-09*
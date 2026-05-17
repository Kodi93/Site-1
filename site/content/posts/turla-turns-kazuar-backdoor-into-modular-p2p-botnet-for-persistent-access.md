+++
title = "Turla Turns Kazuar Backdoor Into Modular P2P Botnet for Persistent Access"
date = "2026-05-17T13:29:28.994897Z"
tags = ["security", "certification"]
description = "The Russian state-sponsored hacking group known as
  
    Turla
  
  has transformed its custom backdoor Kazuar into a modular peer-to-peer (P2P) botn"
canonicalURL = "https://thehackernews.com/2026/05/turla-turns-kazuar-backdoor-into.html"
+++

Turla Turns Kazuar Backdoor Into Modular P2P Botnet for Persistent Access — summary and exam-relevant notes.

## Key Points
- Key insight 1
- Key insight 2
- Key insight 3

## Details
The Russian state-sponsored hacking group known as Turla has transformed its custom backdoor Kazuar into a modular peer-to-peer (P2P) botnet that's engineered for stealth and persistent access to compromised hosts. Turla, per the U.S. Cybersecurity and Infrastructure Security Agency (CISA), is assessed to be affiliated with Center 16 of Russia's Federal Security Service (FSB). It overlaps with activity traced by the broader cybersecurity community under the names ATG26, Blue Python, Iron Hunter, Pensive Ursa, Secret Blizzard (formerly Krypton), Snake, SUMMIT, Uroburos, Venomous Bear, Waterbug, and WRAITH. The hacking group is known for its attacks targeting government, diplomatic, and defense sectors in Europe and Central Asia, as well as endpoints previously breached by Aqua Blizzard (aka Actinium and Gamaredon) to support the Kremlin's strategic objectives. "This upgrade aligns with Secret Blizzard's broader objective of gaining long-term access to systems for intelligence collection," the Microsoft Threat Intelligence team said in a report published Thursday. "While many threat actors rely on increasing usage of native tools (living-off-the-land binaries (LOLBins)) to avoid detection, Kazuar's progression into a modular bot highlights how Secret Blizzard is engineering resilience and stealth directly into their tooling." A key tool in Turla's arsenal is Kazuar , a sophisticated .NET backdoor that has been consistently put to use since 2017. The latest findings from Microsoft charts its evolution from a "monolithic" framework into a modular bot ecosystem featuring three distinct component types, each with its own well-defined roles. These changes enable flexible configuration, reduce observable footprint, and facilitate broad tasking. Attacks distributing the malware have been found to rely on droppers like Pelmeni and ShadowLoader to decrypt and launch the modules. The three module types that form the foundation for Kazuar's architecture are listed below - The Kernel module type exposes three internal communication mechanisms (via Windows Messaging, Mailslot, and named pipes) and three different methods for contacting attacker-controlled infrastructure (via Exchange Web Services, HTTP, and WebSockets). The component also "elects" a single Kernel leader to communicate with the Bridge module on behalf of the other Kernel modules. "Elections occur over Mailslot, and the leader is elected based on the amount of work (length of time the Kernel module has been running) divided by interrupts (reboots, logoffs, process terminated)," Microsoft explained. "Once a leader is elected, it announces itself as the leader and tells all other Kernel modules to set SILENT. Only the elected leader is not SILENT, which allows the leader Kernel module to log activity and request tasks through the Bridge module." Another function of the module is to initiate various threads to set up a named pipe channel between Kernel modules for inter-Kernel communications, specify an external communication method, as well as facilitate Kernel-to-Worker and Kernel-to-Bridge communication over Windows messaging or Mailslot. The end goal of the Kernel is to poll new tasks from the C2 server, parse incoming messages, assign tasks to the Worker, update configuration, and send the results of the tasks back to the server. Furthermore, the module incorporates a task handler that makes it possible to process commands issued by the Kernel leader. Data collected by the Worker module is then aggregated, encrypted, and written to the malware's working directory, from where it's exfiltrated to the C2 server. "Kazuar uses a dedicated working directory as a centralized on-disk staging area to support its internal operations across modules," Microsoft said. "This directory is defined through configuration and is consistently referenced using fully qualified paths to avoid ambiguity across execution contexts." "Within the working directory, Kazuar organizes data by function, isolating tasking, collection output, logs, and configuration material into distinct locations. This design allows the malware to decouple task execution from data storage and exfiltration, maintain operational state across restarts, and coordinate asynchronous activity between modules while minimizing direct interaction with external infrastructure." Learn how to stop patient zero attacks before they bypass detection and compromise your systems at entry points. Learn how to validate real attack paths and reduce exploitable risk with continuous agentic security validation. Get the latest news, expert insights, exclusive resources, and strategies from industry leaders, all for free.



{{< aff "training_partner" "Recommended course" >}}

{{< aff "vpn_vendor" "Try a VPN deal" >}}

*Updated: 2026-05-17*
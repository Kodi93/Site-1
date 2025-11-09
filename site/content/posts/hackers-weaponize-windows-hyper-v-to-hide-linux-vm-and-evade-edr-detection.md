+++
title = "Hackers Weaponize Windows Hyper-V to Hide Linux VM and Evade EDR Detection"
date = "2025-11-09T13:17:40.602375Z"
tags = ["security", "certification"]
description = "The threat actor known as Curly COMrades has been observed exploiting virtualization technologies as a way to bypass security solutions and execute cu"
canonicalURL = "https://thehackernews.com/2025/11/hackers-weaponize-windows-hyper-v-to.html"
+++

Hackers Weaponize Windows Hyper-V to Hide Linux VM and Evade EDR Detection — summary and exam-relevant notes.

## Key Points
- Key insight 1
- Key insight 2
- Key insight 3

## Details
The threat actor known as Curly COMrades has been observed exploiting virtualization technologies as a way to bypass security solutions and execute custom malware. According to a new report from Bitdefender, the adversary is said to have enabled the Hyper-V role on selected victim systems to deploy a minimalistic, Alpine Linux-based virtual machine. "This hidden environment, with its lightweight footprint (only 120MB disk space and 256MB memory), hosted their custom reverse shell, CurlyShell, and a reverse proxy, CurlCat," security researcher Victor Vrabie, along with Adrian Schipor and Martin Zugec, said in a technical report. Curly COMrades was first documented by the Romanian cybersecurity vendor in August 2025 in connection with a series of attacks targeting Georgia and Moldova. The activity cluster is assessed to be active since late 2023, operating with interests that are aligned with Russia. These attacks were found to deploy tools like CurlCat for bidirectional data transfer, RuRat for persistent remote access, Mimikatz for credential harvesting, and a modular .NET implant dubbed MucorAgent, with early iterations dating back all the way to November 2023. In a follow-up analysis conducted in collaboration with Georgia CERT, additional tooling associated with the threat actor has been identified, alongside attempts to establish long-term access by weaponizing Hyper-V on compromised Windows 10 hosts to set up a hidden remote operating environment. "By isolating the malware and its execution environment within a VM, the attackers effectively bypassed many traditional host-based EDR detections," the researchers said. "The threat actor demonstrated a clear determination to maintain a reverse proxy capability, repeatedly introducing new tooling into the environment." Besides using Resocks , Rsockstun , Ligolo-ng , CCProxy , Stunnel , and SSH-based methods for proxy and tunneling, Curly COMrades has employed various other tools, including a PowerShell script designed for remote command execution and CurlyShell, a previously undocumented ELF binary deployed in the virtual machine that provides a persistent reverse shell. Written in C++, the malware is executed as a headless background daemon to connect to a command-and-control (C2) server and launch a reverse shell, allowing the threat actors to run encrypted commands. Communication is achieved via HTTP GET requests to poll the server for new commands and using HTTP POST requests to transmit the results of the command execution back to the server. "Two custom malware families – CurlyShell and CurlCat – were at the center of this activity, sharing a largely identical code base but diverging in how they handled received data: CurlyShell executed commands directly, while CurlCat funneled traffic through SSH," Bitdefender said. "These tools were deployed and operated to ensure flexible control and adaptability." Static defenses overwhelm teams with vuln lists. Learn how automation and context-driven reduction close real risks faster. Learn how to protect cloud workloads, control access, and meet compliance requirements — without slowing innovation. Get the latest news, expert insights, exclusive resources, and strategies from industry leaders – all for free.



{{< aff "training_partner" "Recommended course" >}}

{{< aff "vpn_vendor" "Try a VPN deal" >}}

*Updated: 2025-11-09*
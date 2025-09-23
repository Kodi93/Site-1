+++
title = "GitHub Mandates 2FA and Short-Lived Tokens to Strengthen npm Supply Chain Security"
date = "2025-09-23T13:22:15.030237Z"
tags = ["security", "certification"]
description = "GitHub on Monday announced that it will be changing its authentication and publishing options "in the near future" in response to a recent wave of sup"
canonicalURL = "https://thehackernews.com/2025/09/github-mandates-2fa-and-short-lived.html"
+++

GitHub Mandates 2FA and Short-Lived Tokens to Strengthen npm Supply Chain Security — summary and exam-relevant notes.

## Key Points
- Key insight 1
- Key insight 2
- Key insight 3

## Details
GitHub on Monday announced that it will be changing its authentication and publishing options "in the near future" in response to a recent wave of supply chain attacks targeting the npm ecosystem, including the Shai-Hulud attack . This includes steps to address threats posed by token abuse and self-replicating malware by allowing local publishing with required two-factor authentication (2FA), granular tokens that will have a limited lifetime of seven days, and trusted publishing , which enables the ability to securely publish npm packages directly from CI/CD workflows using OpenID Connect (OIDC). Trusted publishing, besides eliminating the need for npm tokens, establishes cryptographic trust by authenticating each publish using short-lived, workflow-specific credentials that cannot be exfiltrated or reused. Even more significantly, the npm CLI automatically generates and publishes provenance attestations for the package. "Every package published via trusted publishing includes cryptographic proof of its source and build environment," GitHub noted back in late July 2025. "Your users can verify where and how your package was built, increasing trust in your supply chain." To support these changes, the Microsoft-owned company said it will be enacting the following steps - The development comes a week after a supply chain attack codenamed Shai-Hulud injected a self-replicating worm into hundreds of npm packages that scanned developer machines for sensitive secrets and transmitted them to an attacker-controlled server. "By combining self-replication with the capability to steal multiple types of secrets (and not just npm tokens), this worm could have enabled an endless stream of attacks had it not been for timely action from GitHub and open source maintainers," GitHub's Xavier René-Corail said. The disclosure comes as software supply chain security company Socket said it identified a malicious npm package named fezbox that's capable of harvesting browser passwords using a novel steganographic technique. The package is no longer available for download from npm. It attracted a total of 476 downloads since it was first published on August 21, 2025. "In this package, the threat actor (npm alias janedu; registration email janedu0216@gmail[.]com) executes a payload within a QR code to steal username and password credentials from web cookies, within the browser," security researcher Olivia Brown said . Fezbox claims to be a JavaScript utility consisting of common helper functions. But, in reality, it harbors stealthy code to fetch a QR code from a remote URL, parse the QR code, and execute the JavaScript payload contained within that URL. The payload, for its part, attempts to read document.cookie , extracts username and password information from the cookie, and transmits the information to an external server ("my-nest-app-production>.up.railway[.]app") via an HTTPS POST request. "Most applications no longer store literal passwords in cookies, so it's difficult to say how successful this malware would be at its goal," Brown noted. "However, the use of a QR code for further obfuscation is a creative twist by the threat actor. This technique demonstrates how threat actors continue to improve their obfuscation techniques and why having a dedicated tool to check your dependencies is more important than ever." Join our free webinar to master AI-powered workflows—practical steps for secure, scalable automation. Secure your Python projects in 2025—stop "pip install and pray" with proven supply chain defenses. Get the latest news, expert insights, exclusive resources, and strategies from industry leaders – all for free.



{{< aff "training_partner" "Recommended course" >}}

{{< aff "vpn_vendor" "Try a VPN deal" >}}

*Updated: 2025-09-23*
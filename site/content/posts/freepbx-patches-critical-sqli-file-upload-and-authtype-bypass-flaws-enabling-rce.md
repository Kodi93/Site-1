+++
title = "FreePBX Patches Critical SQLi, File-Upload, and AUTHTYPE Bypass Flaws Enabling RCE"
date = "2025-12-17T13:28:36.597070Z"
tags = ["security", "certification"]
description = "Multiple security vulnerabilities have been disclosed in the open-source private branch exchange (PBX) platform FreePBX, including a critical flaw tha"
canonicalURL = "https://thehackernews.com/2025/12/freepbx-authentication-bypass-exposed.html"
+++

FreePBX Patches Critical SQLi, File-Upload, and AUTHTYPE Bypass Flaws Enabling RCE — summary and exam-relevant notes.

## Key Points
- Key insight 1
- Key insight 2
- Key insight 3

## Details
Multiple security vulnerabilities have been disclosed in the open-source private branch exchange (PBX) platform FreePBX, including a critical flaw that could result in an authentication bypass under certain configurations. The shortcomings, discovered by Horizon3.ai and reported to the project maintainers on September 15, 2025, are listed below - It's worth mentioning here that the authentication bypass is not vulnerable in the default configuration of FreePBX, given that the "Authorization Type" option is only displayed when the three following values in the Advanced Settings Details are set to "Yes": However, once the prerequisite is met, an attacker could send crafted HTTP requests to sidestep authentication and insert a malicious user into the "ampusers" database table, effectively accomplishing something similar to CVE-2025-57819 , another flaw in FreePBX that was disclosed as having been actively exploited in the wild in September 2025. "These vulnerabilities are easily exploitable and enable authenticated/unauthenticated remote attackers to achieve remote code execution on vulnerable FreePBX instances," Horizon3.ai security researcher Noah King said in a report published last week. The issues have been addressed in the following versions - In addition, the option to choose an authentication provider has now been removed from Advanced Settings and requires users to set it manually through the command-line using fwconsole. As temporary mitigations, FreePBX has recommended that users set "Authorization Type" to "usermanager," set "Override Readonly Settings" to "No," apply the new configuration, and reboot the system to disconnect any rogue sessions. "If you did find that web server AUTHTYPE was enabled inadvertently, then you should fully analyze your system for signs of any potential compromise," it said. Users are also displayed a warning on the dashboard, stating "webserver" may offer reduced security compared to "usermanager." For optimal protection, it's advised to avoid using this authentication type. "It's important to note that the underlying vulnerable code is still present and relies on authentication layers in front to provide security and access to the FreePBX instance," King said. "It still requires passing an Authorization header with a basic Base64-encoded username:password." "Depending on the endpoint, we noticed a valid username was required. In other cases, such as the file upload shared above, a valid username is not required, and you can achieve remote code execution with a few steps, as outlined. It is best practice not to use the authentication type webserver as it appears to be legacy code." Cloud threats are getting smarter—and harder to see. Join our experts to learn how code-to-cloud detection reveals hidden risks across identities, AI, and Kubernetes, helping you stop attacks before they reach production. Community patching is fast, flexible, and easy to get wrong. This session shows how to build guardrails, spot repo risks early, and balance speed with security using proven, field-tested methods. Get the latest news, expert insights, exclusive resources, and strategies from industry leaders – all for free.



{{< aff "training_partner" "Recommended course" >}}

{{< aff "vpn_vendor" "Try a VPN deal" >}}

*Updated: 2025-12-17*
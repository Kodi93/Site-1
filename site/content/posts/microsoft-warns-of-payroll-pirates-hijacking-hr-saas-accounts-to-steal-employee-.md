+++
title = "Microsoft Warns of ‘Payroll Pirates’ Hijacking HR SaaS Accounts to Steal Employee Salaries"
date = "2025-10-11T13:15:53.628910Z"
tags = ["security", "certification"]
description = "A threat actor known as Storm-2657 has been observed hijacking employee accounts with the end goal of diverting salary payments to attacker-controlled"
canonicalURL = "https://thehackernews.com/2025/10/microsoft-warns-of-payroll-pirates.html"
+++

Microsoft Warns of ‘Payroll Pirates’ Hijacking HR SaaS Accounts to Steal Employee Salaries — summary and exam-relevant notes.

## Key Points
- Key insight 1
- Key insight 2
- Key insight 3

## Details
A threat actor known as Storm-2657 has been observed hijacking employee accounts with the end goal of diverting salary payments to attacker-controlled accounts. "Storm-2657 is actively targeting a range of U.S.-based organizations, particularly employees in sectors like higher education, to gain access to third-party human resources (HR) software as a service (SaaS) platforms like Workday," the Microsoft Threat Intelligence team said in a report. However, the tech giant cautioned that any software-as-a-service (SaaS) platform storing HR or payment and bank account information could be a target of such financially motivated campaigns. Some aspects of the campaign, codenamed Payroll Pirates , were previously highlighted by Silent Push, Malwarebytes, and Hunt.io. What makes the attacks notable is that they don't exploit any security flaw in the services themselves. Rather, they leverage social engineering tactics and a lack of multi-factor authentication (MFA) protections to seize control of employee accounts and ultimately modify payment information to route them to accounts managed by the threat actors. In one campaign observed by Microsoft in the first half of 2025, the attacker is said to have obtained initial access through phishing emails that are designed to harvest their credentials and MFA codes using an adversary-in-the-middle (AitM) phishing link, thereby gaining access to their Exchange Online accounts and taking over Workday profiles through single sign-on (SSO). The threat actors have also been observed creating inbox rules to delete incoming warning notification emails from Workday so as to hide the unauthorized changes made to profiles. This includes altering the salary payment configuration to redirect future salary payments to accounts under their control. To ensure persistent access to the accounts, the attackers enroll their own phone numbers as MFA devices for victim accounts. What's more, the compromised email accounts are used to distribute further phishing emails, both within the organization and to other universities. Microsoft said it observed 11 successfully compromised accounts at three universities since March 2025 that were used to send phishing emails to nearly 6,000 email accounts across 25 universities. The email messages feature lures related to illnesses or misconduct notices on campus, inducing a false sense of urgency and tricking recipients into clicking on the fake links. To mitigate the risk posed by Storm-2657, it's recommended to adopt passwordless, phishing-resistant MFA methods such as FIDO2 security keys, and review accounts for signs of suspicious activity, such as unknown MFA devices and malicious inbox rules. Join our free webinar to master AI-powered workflows—practical steps for secure, scalable automation. Join us this Halloween for a live webinar exposing real password breaches and how to stop them. Get the latest news, expert insights, exclusive resources, and strategies from industry leaders – all for free.



{{< aff "training_partner" "Recommended course" >}}

{{< aff "vpn_vendor" "Try a VPN deal" >}}

*Updated: 2025-10-11*
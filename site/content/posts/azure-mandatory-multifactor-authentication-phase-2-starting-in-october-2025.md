+++
title = "Azure mandatory multifactor authentication: Phase 2 starting in October 2025"
date = "2025-09-25T13:23:28.883597Z"
tags = ["security", "certification"]
description = "<p>Microsoft Azure is announcing the start of Phase 2 multi-factor authentication enforcement at the Azure Resource Manager layer, starting October 1,"
canonicalURL = "https://azure.microsoft.com/en-us/blog/azure-mandatory-multifactor-authentication-phase-2-starting-in-october-2025/"
+++

Azure mandatory multifactor authentication: Phase 2 starting in October 2025 — summary and exam-relevant notes.

## Key Points
- Key insight 1
- Key insight 2
- Key insight 3

## Details
Connect with a community to find answers, ask questions, build skills, and accelerate your learning. As cyberattacks become increasingly frequent, sophisticated, and damaging, safeguarding your digital assets has never been more critical, and at Microsoft, your security is our top priority. Microsoft research shows that multifactor authentication (MFA) can block more than 99.2% of account compromise attacks, making it one of the most effective security measures available. As announced in August 2024 , Azure started to implement mandatory MFA for Azure Public Cloud sign-ins. By enforcing MFA for Azure sign-ins, we aim to provide you with the best protection against cyber threats as part of Microsoft’s commitment to enhance security for all customers, taking one step closer to a more secure future. As previously announced, Azure MFA enforcement was rolled out gradually in phases to provide customers with enough time to plan and execute their implementations: We are proud to announce that multifactor enforcement for Azure Portal sign-ins was rolled out for 100% of Azure tenants in March 2025. Now, Azure is announcing the start of Phase 2 MFA enforcement at the Azure Resource Manager layer, starting October 1, 2025 . Phase 2 enforcement will be gradually applied across Azure tenants through Azure Policy , following Microsoft safe deployment practices . Starting this week, Microsoft sent notices to all Microsoft Entra Global Administrators by email and through Azure Service Health notifications to notify the start date of enforcement and how to prepare for upcoming MFA enforcement. Users will be required to authenticate with MFA before performing resource management operations. Workload identities, such as managed identities and service principals, aren’t impacted by either phase of this MFA enforcement. Learn more about the scope of enforcement . To ensure your users can perform resource management actions, enable MFA for your users by October 1, 2025 . To identify which users in your environment are set up for mandatory MFA, follow these steps . To understand potential impact ahead of Phase 2 enforcement, assign built-in Azure Policy definitions to block resource management operations if the user has not authenticated with MFA. Customers can gradually apply this enforcement across different resource hierarchy scopes, resource types, or regions. For the best compatibility experience, users in your tenant should use Azure CLI version 2.76 and Azure PowerShell version 14.3 or later. Prepare for Phase 2 of multifactor authentication enforcement. Connect with a community to find answers, ask questions, build skills, and accelerate your learning. The future of AI starts here. Envision your next great AI app with the latest technologies. Get started with Azure. Connect with us on social



{{< aff "training_partner" "Recommended course" >}}

{{< aff "vpn_vendor" "Try a VPN deal" >}}

*Updated: 2025-09-25*
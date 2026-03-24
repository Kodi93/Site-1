+++
title = "Citrix Urges Patching Critical NetScaler Flaw Allowing Unauthenticated Data Leaks"
date = "2026-03-24T13:29:14.745717Z"
tags = ["security", "certification"]
description = "Citrix has released security updates to address two vulnerabilities in NetScaler ADC and NetScaler Gateway, including a critical flaw that could be ex"
canonicalURL = "https://thehackernews.com/2026/03/citrix-urges-patching-critical.html"
+++

Citrix Urges Patching Critical NetScaler Flaw Allowing Unauthenticated Data Leaks — summary and exam-relevant notes.

## Key Points
- Key insight 1
- Key insight 2
- Key insight 3

## Details
Citrix has released security updates to address two vulnerabilities in NetScaler ADC and NetScaler Gateway, including a critical flaw that could be exploited to leak sensitive data from the application. The vulnerabilities are listed below - Cybersecurity company Rapid7 said that CVE-2026-3055 refers to an out-of-bounds read that could be exploited by unauthenticated remote attackers to leak potentially sensitive information from the appliance's memory. However, for exploitation to be successful, the Citrix ADC or Citrix Gateway appliance must be configured as a SAML Identity Provider (SAML IDP), which means default configurations are unaffected. To determine if the device has been configured as a SAML IDP Profile, Citrix is urging customers to inspect their NetScaler Configuration for the specified string: "add authentication samlIdPProfile .\*" CVE-2026-4368, on the other hand, requires the appliance to be configured as a gateway (i.e., SSL VPN, ICA Proxy, CVPN, and RDP Proxy) or an Authentication, Authorization, and Accounting ( AAA ) server. Customers can check the NetScaler Configuration to ascertain if their devices have been configured as either of the nodes - The vulnerabilities affect NetScaler ADC and NetScaler Gateway versions 14.1 before 14.1-66.59 and 13.1 before 13.1-62.23, as well as NetScaler ADC 13.1-FIPS and 13.1-NDcPP before 13.1-37.262. Users are advised to apply the latest updates as soon as possible for optimal protection. While there is no evidence that the shortcomings have been exploited in the wild, security flaws in NetScaler devices have been repeatedly exploited by threat actors ( CVE-2023-4966 , aka Citrix Bleed, CVE-2025-5777 , aka Citrix Bleed 2, CVE-2025-6543, and CVE-2025-7775 ), making it imperative that users take steps to update their instances. "CVE-2026-3055 allows unauthenticated attackers to leak and read sensitive memory from NetScaler ADC deployments. If it sounds familiar, it's because it is – this vulnerability sounds suspiciously similar to Citrix Bleed and Citrix Bleed 2, which continue to represent a trauma event for many," watchTowr CEO and founder Benjamin Harris told The Hacker News. "NetScalers are critical solutions that have been continuously targeted for initial access into enterprise environments. While the advisory just went live, defenders need to act quickly. Anyone running impacted versions needs to patch urgently. Imminent exploitation is highly likely." A practical deep dive into securing AI agents against real-world attack paths beyond the model itself. See exactly where your controls stand against today’s threats—automated, accurate, approachable. Get the latest news, expert insights, exclusive resources, and strategies from industry leaders – all for free.



{{< aff "training_partner" "Recommended course" >}}

{{< aff "vpn_vendor" "Try a VPN deal" >}}

*Updated: 2026-03-24*
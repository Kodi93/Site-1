+++
title = "Continuing Scans for swagger.json, (Wed, Jun 3rd)"
date = "2026-06-03T14:30:39.093836Z"
tags = ["security", "certification"]
description = "Enterprise applications often still use complex standards like SOAP for web services. The big advantage of SOAP is its tight and extensive standards, "
canonicalURL = "https://isc.sans.edu/diary/rss/33044"
+++

Continuing Scans for swagger.json, (Wed, Jun 3rd) — summary and exam-relevant notes.

## Key Points
- Key insight 1
- Key insight 2
- Key insight 3

## Details
Enterprise applications often still use complex standards like SOAP for web services. The big advantage of SOAP is its tight and extensive standards, which enable interoperability across an enterprise governed by web services. The disadvantage of SOAP: First, while it is de facto usually used over HTTP, it does not leverage HTTP, leading to unnecessary complexity. Secondly, kids don't RTFM, and developers these days tend not to appreciate the art of careful system design; they rather throw code at an IDE to see what sticks, if they don't vibe code it anyway. So the answer to all of the calls for a simpler standard is the non-standard REST. REST is more a "living standard" defined by commonly used libraries that happen to be popular right now. One of these standards is Swagger, or OpenAPI [1]. A very popular part of Swagger is "swagger.json", a file that defines how to use an API. Some people here may remember "WSDL"s, or good old ".h" files in C/C++. Same idea, but now with more JSON. From a web application security perspective, swagger.json is like a directory listing for an API. It is not that they are inherently evil or insecure. They are often necessary to allow developers to connect to an API efficiently. But on the other hand, they are also a great roadmap for attackers. So it's no surprise that attackers are looking for them. Not only do they provide a list of API features, but metadata in the description will usually identify the underlying application. It is a great way to find vulnerable applications. Here are some of the top URLs attackers are scanning recently: And some that started showing up more recently: The number of requests is continuously high, but there are spikes and slow times: But the continuing interest shows that attackers see value here. What's the lesson? Should you stop using swagger.json? Probably not. Your developers need it. On the other hand, you should be scanning for swagger.json files preemptively in your environment to identify inappropriately published swagger.json files. My intro remarks about REST, while obviously an attempt to finally get someone to read these posts, also point out that with REST, some important design decisions are left up to you, and with lots of freedom comes lots of possibilities to mess things up. Any comments on good tools to do so? (yes, more engagement farming. But maybe it will cause me to fix the comment system for this site. [1] https://swagger.io/specification/ -- Johannes B. Ullrich, Ph.D. , Dean of Research, SANS.edu Twitter | Login here to join the discussion.



{{< aff "training_partner" "Recommended course" >}}

{{< aff "vpn_vendor" "Try a VPN deal" >}}

*Updated: 2026-06-03*
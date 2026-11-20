---
layout: post
title: When 5G needs more room for uploads
date: 2026-11-20
description: How Wixor adapts the uplink and downlink slot pattern to changing 5G traffic.
---

On a 5G carrier that uses time-division duplexing, uploads and downloads take turns on the same spectrum. A schedule with more downlink slots is a reasonable starting point for download-heavy traffic. A camera streaming video to an edge server has a different problem. Its packets can build up while they wait for the next uplink slot.

We built Wixor to adjust the slot pattern as demand changes. It uses signals available at the base station to anticipate traffic demand and decides both how many slots to assign in each direction and where to put them. That second choice matters because the gap between uplink slots determines how long a newly arrived packet may have to wait.

Changing the pattern also changes what a transport protocol sees. We built in a way to smooth those changes for TCP and integrated the system with srsRAN. We evaluated it with workloads including video analytics, edge perception, and live video transmission, and found improvements across most of the application metrics we tested. What stuck with me was that fitting more uploads into the schedule is only half the problem. The timing of those opportunities matters too.

[Wixor project page](/projects/wixor/) · [CoNEXT 2024 paper](/assets/pdf/wixor_conext24.pdf)

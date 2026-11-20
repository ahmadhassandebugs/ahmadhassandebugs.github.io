---
layout: post
title: What should a phone connect to?
date: 2026-11-20
description: What we learned about choosing serving cells and carriers for different 5G applications.
---

A 5G phone can see several cells and bands at once. The network has to choose which ones serve the phone and which carriers to combine. A phone downloading a large file and a phone on a video call can benefit from different choices, even at the same location.

In a measurement study across 12 cities in five countries, we explored how those choices affect performance on commercial networks. That led us to build OPCM, a connectivity-management framework that runs at the base station. It lets an operator choose what to optimize, such as throughput, latency, or energy use. The base station can tailor the serving-cell configuration to each device while coordinating the choices across users.

We evaluated OPCM in an over-the-air srsRAN testbed, trace-driven simulations, and live 5G experiments. The prototype could find better-performing cell combinations in the field, and in some evaluation settings it improved application quality of experience over the connectivity-management baselines. The project pushed me to think about connectivity management as a decision about what an application needs from its connection.

[OPCM project page](/projects/opcm/) · [CoNEXT 2025 paper](/assets/pdf/opcm_conext25.pdf)

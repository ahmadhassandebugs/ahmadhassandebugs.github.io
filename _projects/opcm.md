---
layout: page
title: OPCM
description: Performance-driven connectivity management framework for future mobile networks
img: assets/img/opcm-thumbnail.png
importance: 1
category: work
_styles: >
  .post-header {
    display: none;
  }
  .metric-card {
    background: linear-gradient(135deg, #fb923c 0%, #f87171 100%);
    color: #1a1a1a;
    padding: 1rem;
    border-radius: 15px;
    text-align: center;
    margin: 0.75rem 0;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    transition: transform 0.3s ease;
  }
  .metric-card * {
    color: #1a1a1a !important;
  }
  .metric-card:hover {
    transform: translateY(-5px);
  }
  .metric-number {
    font-size: 3rem;
    font-weight: bold;
    margin: 0.25rem 0;
    line-height: 1;
  }
  .metric-label {
    font-size: 1.1rem;
    opacity: 0.9;
    margin-top: 0.5rem;
    line-height: 1.4;
  }
  .award-badge {
    display: inline-block;
    background: #fb923c;
    color: white;
    padding: 0.5rem 1.5rem;
    border-radius: 25px;
    font-weight: bold;
    margin: 0.5rem;
    box-shadow: 0 4px 15px rgba(251, 146, 60, 0.3);
  }
  .hero-section {
    text-align: center;
    padding: 1.25rem 0;
    background: linear-gradient(135deg, #f5f7fa 0%, #fed7aa 100%);
    border-radius: 20px;
    margin: 2rem 0;
  }
  .metric-first {
    margin-left: 1rem;
  }
  .metric-last {
    margin-right: 1rem;
  }
  .video-container {
    margin: 2rem 0;
    text-align: center;
  }
  .stat-box {
    background: #f8f9fa;
    padding: 1.5rem;
    border-radius: 10px;
    border-left: 4px solid #fb923c;
    margin: 1rem 0;
  }
  .highlight-number {
    color: #fb923c;
    font-weight: bold;
    font-size: 1.3em;
  }
  .results-table {
    width: 100%;
    border-collapse: collapse;
    margin: 2rem 0;
    font-size: 0.9rem;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    border-radius: 8px;
    overflow: hidden;
  }
  .results-table th {
    background: linear-gradient(135deg, #fb923c 0%, #f87171 100%);
    color: white;
    padding: 0.75rem;
    text-align: center;
    font-weight: bold;
    border: 1px solid rgba(255,255,255,0.2);
  }
  .results-table td {
    padding: 0.75rem;
    text-align: center;
    border: 1px solid #e2e8f0;
    background: white;
  }
  .results-table tr:nth-child(even) td {
    background: #f8f9fa;
  }
  .results-table .app-name {
    font-weight: bold;
    text-align: left;
    background: #fef3e2 !important;
  }
  .results-table .metric-name {
    text-align: left;
    padding-left: 1.5rem;
    white-space: nowrap;
  }
  .results-table .best {
    background: #fed7aa !important;
    font-weight: bold;
  }
  .arrow-up {
    color: #2563eb;
  }
  .arrow-down {
    color: #f87171;
  }
  .innovation-item {
    background: #f8f9fa;
    padding: 1rem 1.25rem;
    margin-bottom: 0.75rem;
    border-radius: 8px;
    border-left: 3px solid #fb923c;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }
  .innovation-item:hover {
    transform: translateX(5px);
    box-shadow: 0 2px 8px rgba(251, 146, 60, 0.2);
  }
  .innovation-item:last-child {
    margin-bottom: 0;
  }
---

<div class="hero-section">
  <h1 style="font-size: 3rem; margin-bottom: 0.5rem; color: #2d3748;">OPCM</h1>
  <p style="font-size: 1.3rem; color: #4a5568; margin-bottom: 1rem;">
    Opportunistic Performance-driven Connectivity Management for 5G/xG Networks
  </p>
  
  <div class="row" style="margin-top: 1rem;">
    <div class="col-md-4">
      <div class="metric-card metric-first">
        <div class="metric-label">Up to</div>
        <div class="metric-number">65%</div>
        <div class="metric-label">QoE Improvement</div>
      </div>
    </div>
    <div class="col-md-4">
      <div class="metric-card">
        <div class="metric-label">Within</div>
        <div class="metric-number">10%</div>
        <div class="metric-label">of the Optimal</div>
      </div>
    </div>
    <div class="col-md-4">
      <div class="metric-card metric-last">
        <div class="metric-label">Less than</div>
        <div class="metric-number">9%</div>
        <div class="metric-label">System Overhead</div>
      </div>
    </div>
  </div>
</div>

## Awards & Recognition

<div style="text-align: center; margin: 2rem 0;">
  <span class="award-badge">🏆 CoNEXT 2025 Best Community Award</span>
</div>

## Demo Videos

<div class="video-container">
  <p style="font-style: italic; color: #718096;">
    Demo videos showcasing OPCM's performance will be added here.
  </p>
  
  <!-- Example video include syntax (uncomment and update when videos are available):
  {% include video.liquid path="assets/video/opcm-demo.mp4" class="img-fluid rounded z-depth-1" controls=true width="800" %}
  -->
</div>

## Problem & Motivation

Cellular networks deploy cells with diverse combinations of access technologies (3G, 4G, 5G, etc.), architectures (NSA, SA, etc.), and radio frequency bands/channels (e.g., Low-, Mid-, and High-Frequency bands). They also aggregate carriers for higher data access speeds. The question is: *how to intelligently and dynamically configure and reconfigure a user equipment's serving cells to deliver the best network performance*?

**Legacy Connectivity Management (CM) has three key limitations:**

1. **Performance-oblivious**: While radio link quality criterion has historically ensured seamless connectivity, legacy CM lacks support for metrics like throughput and energy efficiency.

2. **Independent procedures**: CM procedures (cell selection, reselection, handover, carrier aggregation, dual connectivity) operate independently, leading to redundant logic, increased management complexity, misconfigurations, and in extreme cases, network outages.

3. **Network-centric**: Legacy CM applies uniform criteria to all UEs. However, different traffic types demand different solutions—e.g., one cell may be better for latency-sensitive traffic, while another offers higher throughput.

These limitations contribute to the perception that 5G has been disappointing, with some even claiming it fares worse than 4G, despite its potential for higher throughput.

## Who can Benefit from OPCM?

- **Mobile Network Operators** seeking to optimize connectivity management across diverse cell deployments and improve user experience while maintaining fairness and policy compliance.
- **Enterprises** with diverse needs requiring optimized network performance for different application types.
- **Application providers** needing reliable, high-performance connectivity to support next-generation digital services.
- **End users** experiencing connectivity issues or suboptimal performance due to legacy CM limitations.

OPCM is designed as a **centralized solution deployed at the base station**, allowing it to coordinate multiple UEs, enforce operator policies, and facilitate user fairness, all while remaining backward-compatible with existing infrastructure.

## Key Innovations

<div class="row" style="align-items: center;">
  <div class="col-md-6">
    <div class="innovation-item">
      <strong>Unified performance-driven framework</strong>: Decouples CM actions from performance criteria, allowing operators to flexibly plug in diverse metrics (throughput, latency, energy, etc.).
    </div>
    <div class="innovation-item">
      <strong>Centralized base station solution</strong>: Enables coordination of multiple UEs, enforcement of operator policies, and user fairness.
    </div>
    <div class="innovation-item">
      <strong>UE-level personalization</strong>: Supports different traffic types with tailored solutions—high-bandwidth for backlogged flows, low-latency for real-time traffic, energy-efficient for lightweight workloads.
    </div>
    <div class="innovation-item">
      <strong>Backward-compatible design</strong>: Works seamlessly with existing infrastructure via higher-level abstraction over CM procedures.
    </div>
  </div>
  <div class="col-md-6" style="display: flex; flex-direction: column; align-items: center; justify-content: center;">
    <h4 style="margin: 0 0 0.25rem 0; text-align: center;">OPCM Design Overview</h4>
    {% include figure.liquid path="assets/img/opcm-design-overview.png" title="OPCM Design Overview" class="img-fluid rounded z-depth-1" %}
    <div style="margin-top: 0.5rem;">
      <h4 style="margin: 0 0 0.25rem 0; text-align: center;">OPCM Metric Registration API</h4>
      {% include figure.liquid path="assets/img/opcm-metric-api.png" title="OPCM Metric Registration API" class="img-fluid rounded z-depth-1" %}
    </div>
  </div>
</div>

<div style="margin-bottom: 2rem;"></div>

## Measurement Study & Results

We conducted a comprehensive measurement study across 12 cities in 5 North American and European countries. Key findings include:

<div class="row">
  <div class="col-md-6">
    {% include figure.liquid path="assets/img/opcm-bs-numbers.png" title="Base Station Numbers" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-md-6">
    <ul style="list-style: none; padding-left: 0; margin-top: 1rem;">
      <li style="margin-bottom: 0.75rem;">• The wide availability and heterogeneity of cell deployments across diverse geographic regions.</li>
      <li style="margin-bottom: 0.75rem;">• The spatio-temporal stability of cell deployments.</li>
      <li style="margin-bottom: 0.75rem;">• The significant, untapped performance gains enabled by the diversity of available cells.</li>
    </ul>
  </div>
</div>

We also evaluate OPCM's performance in three settings: (1) Over-the-air testbed based on srsRAN, (2) Trace-driven ns3 simulations, and (3) Live 5G experiments. A few main takeaways are:

<div class="row" style="margin-top: 2rem;">
  <div class="col-md-6">
    <ul style="list-style: none; padding-left: 0; margin-top: 1rem;">
      <li style="margin-bottom: 0.75rem;">• OPCM offers up to 65% and 28% higher average QoE than the legacy CM and a UE-side CM solution iCellSpeed.</li>
      <li style="margin-bottom: 0.75rem;">• OPCM performs as well as the legacy CM under mobility, and can effectively find the highest performing cell combinations in the wild.</li>
      <li style="margin-bottom: 0.75rem;">• OPCM satisfies operator policies: cross-UE fairness is within 98-99% of the legacy CM, while the spectral efficiency improves by 2-3%</li>
    </ul>
  </div>
  <div class="col-md-6">
    {% include figure.liquid path="assets/img/opcm-bitrate-result.png" title="OPCM Bitrate Results" class="img-fluid rounded z-depth-1" %}
  </div>
</div>

## Collaborators

This work is a collaboration between:

<div style="display: flex; align-items: center; justify-content: space-evenly; flex-wrap: wrap; margin: 0.1rem 0 0.5rem 0; gap: 1rem;">
  <div style="text-align: center;">
    <a href="https://www.usc.edu/" target="_blank" style="text-decoration: none;">
      <img src="/assets/img/logo-usc.png" alt="USC" style="max-width: 180px; height: auto; filter: grayscale(0%);">
    </a>
  </div>
  <div style="text-align: center;">
    <a href="https://cse.umn.edu/" target="_blank" style="text-decoration: none;">
      <img src="/assets/img/logo-umn.png" alt="UMN" style="max-width: 220px; height: auto; filter: grayscale(0%);">
    </a>
  </div>
  <div style="text-align: center;">
    <a href="https://www.umich.edu/" target="_blank" style="text-decoration: none;">
      <img src="/assets/img/logo-umich.png" alt="UMich" style="max-width: 180px; height: auto; filter: grayscale(0%);">
    </a>
  </div>
  <div style="text-align: center;">
    <a href="https://www.cisco.com/" target="_blank" style="text-decoration: none;">
      <img src="/assets/img/logo-cisco.png" alt="Cisco" style="max-width: 120px; height: auto; filter: grayscale(0%);">
    </a>
  </div>
</div>

## References

```
Ahmad Hassan, Wei Ye, Anlan Zhang, Rostand A. K. Fezeu, Jason Carpenter, Ruiyang Zhu, 
Shuowei Jin, Myungjin Lee, Akshay Jajoo, Morley Mao, Zhi-Li Zhang, and Feng Qian. 
2025. OPCM: Opportunistic Performance-driven Connectivity Management for 5G/xG Networks. 
Proc. ACM Netw. 3, CoNEXT4, Article 23 (December 2025), 23 pages. 
https://doi.org/10.1145/3768970
```

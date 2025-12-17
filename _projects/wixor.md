---
layout: page
title: Wixor
description: AI-driven proactive TDD policy optimization system for 5G/xG networks
img: assets/img/wixor-thumbnail.png
importance: 1
category: work
_styles: >
  .post-header {
    display: none;
  }
  .metric-card {
    background: linear-gradient(135deg, #818cf8 0%, #a78bfa 100%);
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
    background: #ff6b6b;
    color: white;
    padding: 0.5rem 1.5rem;
    border-radius: 25px;
    font-weight: bold;
    margin: 0.5rem;
    box-shadow: 0 4px 15px rgba(255,107,107,0.3);
  }
  .hero-section {
    text-align: center;
    padding: 1.25rem 0;
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
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
    border-left: 4px solid #667eea;
    margin: 1rem 0;
  }
  .highlight-number {
    color: #667eea;
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
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
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
    background: #f1f5f9 !important;
  }
  .results-table .metric-name {
    text-align: left;
    padding-left: 1.5rem;
    white-space: nowrap;
  }
  .results-table .best {
    background: #e2e8f0 !important;
    font-weight: bold;
  }
  .arrow-up {
    color: #2563eb;
  }
  .arrow-down {
    color: #dc2626;
  }
  .innovation-item {
    background: #f8f9fa;
    padding: 1rem 1.25rem;
    margin-bottom: 0.75rem;
    border-radius: 8px;
    border-left: 3px solid #667eea;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }
  .innovation-item:hover {
    transform: translateX(5px);
    box-shadow: 0 2px 8px rgba(102, 126, 234, 0.2);
  }
  .innovation-item:last-child {
    margin-bottom: 0;
  }
  .timeline-container {
    position: relative;
    padding: 3rem 1rem;
    margin: 3rem 0;
    width: 100%;
  }
  .timeline-wrapper {
    position: relative;
    width: 100%;
    max-width: 100%;
    padding: 0;
  }
  .timeline-line {
    position: absolute;
    top: 50%;
    left: 5%;
    right: 5%;
    height: 3px;
    background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    transform: translateY(-50%);
    z-index: 1;
    border-radius: 2px;
  }
  .timeline-items {
    display: flex;
    justify-content: space-between;
    position: relative;
    z-index: 2;
    width: 100%;
    padding: 0 2%;
  }
  .timeline-item {
    flex: 1;
    position: relative;
    text-align: center;
    padding: 0 0.25rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
  .timeline-item.top {
    padding-bottom: 90px;
  }
  .timeline-item.top .timeline-content {
    margin-bottom: 0.75rem;
  }
  .timeline-item.top .timeline-dot {
    margin: 0.5rem auto;
  }
  .timeline-item.top .timeline-date {
    margin-top: 0.5rem;
  }
  .timeline-item.bottom {
    padding-top: 90px;
  }
  .timeline-item.bottom .timeline-date {
    margin-bottom: 0.5rem;
  }
  .timeline-item.bottom .timeline-dot {
    margin: 0.5rem auto;
  }
  .timeline-item.bottom .timeline-content {
    margin-top: 0.75rem;
  }
  .timeline-dot {
    width: 18px;
    height: 18px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border: 3px solid var(--global-bg-color);
    border-radius: 50%;
    margin: 0.5rem auto;
    position: relative;
    z-index: 3;
    box-shadow: 0 2px 8px rgba(102, 126, 234, 0.4), 0 0 0 2px rgba(102, 126, 234, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    flex-shrink: 0;
  }
  .timeline-dot:hover {
    transform: scale(1.3);
    box-shadow: 0 4px 12px rgba(102, 126, 234, 0.6), 0 0 0 4px rgba(102, 126, 234, 0.2);
  }
  .timeline-date {
    font-size: 0.8rem;
    font-weight: bold;
    color: #667eea;
    margin: 0.25rem 0;
    white-space: nowrap;
  }
  .timeline-content {
    font-size: 0.85rem;
    color: var(--global-text-color);
    line-height: 1.4;
    background: linear-gradient(135deg, var(--global-card-bg-color) 0%, rgba(102, 126, 234, 0.05) 100%);
    padding: 0.6rem 0.5rem;
    border-radius: 10px;
    border: 1.5px solid rgba(102, 126, 234, 0.2);
    margin: 0.5rem 0;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
    max-width: 120px;
    min-height: 50px;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
  }
  .timeline-content:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(102, 126, 234, 0.15);
    border-color: rgba(102, 126, 234, 0.4);
  }
  @media (max-width: 768px) {
    .timeline-content {
      font-size: 0.75rem;
      padding: 0.5rem 0.4rem;
      max-width: 90px;
      min-height: 45px;
    }
    .timeline-date {
      font-size: 0.7rem;
    }
  }
---

<div class="hero-section">
  <h1 style="font-size: 3rem; margin-bottom: 0.5rem; color: #2d3748;">Wixor</h1>
  <p style="font-size: 1.5rem; color: #4a5568; margin-bottom: 1rem;">
    AI-Powered Dynamic TDD Policy Adaptation for 5G/xG Networks
  </p>
  
  <div class="row" style="margin-top: 1rem;">
    <div class="col-md-4">
      <div class="metric-card metric-first">
        <div class="metric-label">Up to</div>
        <div class="metric-number">96%</div>
        <div class="metric-label">QoE Improvement</div>
      </div>
    </div>
    <div class="col-md-4">
      <div class="metric-card">
        <div class="metric-label">Within</div>
        <div class="metric-number">88%</div>
        <div class="metric-label">of the Oracle</div>
      </div>
    </div>
    <div class="col-md-4">
      <div class="metric-card metric-last">
        <div class="metric-label">Less than</div>
        <div class="metric-number">10%</div>
        <div class="metric-label">System Overhead</div>
      </div>
    </div>
  </div>
</div>

## Awards & Recognition

<div style="text-align: center; margin: 2rem 0;">
  <span class="award-badge">🏆 CoNEXT 2024 Best Paper Runner-Up</span>
  <span class="award-badge">📢 Presented at HPE Tech Con 2024</span>
</div>

## Project Timeline

<div class="timeline-container">
  <div class="timeline-wrapper">
    <div class="timeline-line"></div>
    <div class="timeline-items">
      <div class="timeline-item top">
        <div class="timeline-content">Project started</div>
        <div class="timeline-dot"></div>
        <div class="timeline-date">June 2023</div>
      </div>
      <div class="timeline-item bottom">
        <div class="timeline-date">October 2023</div>
        <div class="timeline-dot"></div>
        <div class="timeline-content">Initial measurements completed</div>
      </div>
      <div class="timeline-item top">
        <div class="timeline-content">Preliminary idea presented at HPE Tech Con</div>
        <div class="timeline-dot"></div>
        <div class="timeline-date">March 2024</div>
      </div>
      <div class="timeline-item bottom">
        <div class="timeline-date">June 2024</div>
        <div class="timeline-dot"></div>
        <div class="timeline-content">Initial prototype complete</div>
      </div>
      <div class="timeline-item top">
        <div class="timeline-content">Presented at CoNEXT</div>
        <div class="timeline-dot"></div>
        <div class="timeline-date">December 2024</div>
      </div>
      <div class="timeline-item bottom">
        <div class="timeline-date">May 2025</div>
        <div class="timeline-dot"></div>
        <div class="timeline-content">Small-scale deployment at USC</div>
      </div>
      <div class="timeline-item top">
        <div class="timeline-content">Data collection on testbed</div>
        <div class="timeline-dot"></div>
        <div class="timeline-date">Ongoing</div>
      </div>
    </div>
  </div>
</div>

## Demo Videos

<div class="video-container">
  <p style="font-style: italic; color: #718096;">
    Demo videos showcasing Wixor's performance will be added here.
  </p>
  
  <!-- Example video include syntax (uncomment and update when videos are available):
  {% include video.liquid path="assets/video/wixor-demo.mp4" class="img-fluid rounded z-depth-1" controls=true width="800" %}
  -->
</div>

## Problem & Motivation

In the era of 5G and beyond, dynamic Time Division Duplex (TDD) has become essential for supporting applications that demand high bandwidth and low latency.
Traditional 5G deployments use **static, downlink-biased** TDD configurations that fail to serve emerging customer-facing applications requiring heavy uplink bandwidth or tight latency deadlines. These include AR/VR streaming, live video ingest, industrial automation, real-time perception analytics, drone telemetry, remote assistance, and high-fidelity sensor workloads.

## Who can Benefit from Wixor?

- **Mobile Network Operators** aiming to deliver superior quality-of-experience (QoE) for consumers and enterprises while improving spectrum efficiency.
- **Enterprises** deploying private 5G seeking deterministic performance for automation, robotics, analytics, and safety-critical workloads.
- **Application and cloud providers** that depend on reliable, low-latency UL connectivity to support next-generation digital services.
- **Government and smart-city operators** deploying real-time video, mobility intelligence, and IoT services.

Wixor is built as a **3GPP-compliant, operator-friendly software module** that seamlessly integrates with public 5G networks, enterprise private 5G installations, and neutral-host environments.

## Key Innovations

<div class="row" style="align-items: center;">
  <div class="col-md-6">
    <div class="innovation-item">
      <strong>Proactive RL-based optimization</strong>: Forecasts demand in advance, unlike reactive solutions
    </div>
    <div class="innovation-item">
      <strong>Cross-layer intelligence</strong>: Uses BS-level features for scalability across dense environments
    </div>
    <div class="innovation-item">
      <strong>Joint UL/DL and pattern optimization</strong>: Optimizes both slot distribution and arrangement
    </div>
    <div class="innovation-item">
      <strong>Transport-aware policy smoothing</strong>: Prevents TCP destabilization during TDD transitions
    </div>
    <div class="innovation-item">
      <strong>Deployment-ready</strong>: Fully implemented 2.3k-line C/C++ system integrated with srsRAN
    </div>
  </div>
  <div class="col-md-6" style="display: flex; align-items: center; justify-content: center;">
    {% include figure.liquid path="assets/img/wixor-design-overview.png" title="Wixor Design Overview" class="img-fluid rounded z-depth-1" %}
  </div>
</div>

<div style="margin-bottom: 2rem;"></div>

## Results

Wixor's effectiveness has been demonstrated through extensive evaluation totaling more than six hours of real workloads, including edge perception, video analytics, mobility scenarios, and live video transmissions.

<div style="text-align: center; margin: 1.5rem 0;">
  <div style="max-width: 75%; margin: 0 auto;">
    {% include figure.liquid path="assets/img/wixor-eval-setup.png" title="Evaluation Setup" class="img-fluid rounded z-depth-1" %}
  </div>
</div>


### Application-Level Performance

Overall QoE improvement for application workloads and 6+ hours of channel traces. Wixor outperforms baselines for most metrics. The up (↑) and down (↓) arrows indicate the direction of QoE improvement. The gray shaded region highlights the best performing scheme. *Default*, *SFair*, *Reactive*, and *DRP* are the baselines.

<div style="overflow-x: auto; margin: 0.08rem 0; display: flex; justify-content: center;">
<table class="results-table" style="width: 90%;">
  <thead>
    <tr>
      <th>Application</th>
      <th>Metric</th>
      <th><em>Default</em></th>
      <th><em>SFair</em></th>
      <th><em>Reactive</em></th>
      <th><em>DRP</em></th>
      <th>Wixor</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="app-name" rowspan="2">Edge Video Analytics (EVA)</td>
      <td class="metric-name">Response Latency (ms) <span class="arrow-down">↓</span></td>
      <td>93.3</td>
      <td>77.2</td>
      <td>44.9</td>
      <td>57.4</td>
      <td class="best">38.1</td>
    </tr>
    <tr>
      <td class="metric-name">Perceptive Accuracy (%) <span class="arrow-up">↑</span></td>
      <td>34.7</td>
      <td>40.1</td>
      <td>54.8</td>
      <td>47.6</td>
      <td class="best">68.2</td>
    </tr>
    <tr>
      <td class="app-name" rowspan="2">Edge-assisted Autonomous Vehicle Perception (EAVP)</td>
      <td class="metric-name">Response Latency (ms) <span class="arrow-down">↓</span></td>
      <td>67.8</td>
      <td>60.3</td>
      <td>51.7</td>
      <td>56.8</td>
      <td class="best">46.3</td>
    </tr>
    <tr>
      <td class="metric-name">Mean IoU <span class="arrow-up">↑</span></td>
      <td>0.68</td>
      <td>0.71</td>
      <td>0.77</td>
      <td>0.74</td>
      <td class="best">0.78</td>
    </tr>
    <tr>
      <td class="app-name" rowspan="2">Live Video Ingest (LVI)</td>
      <td class="metric-name">Ingest Delay (ms) <span class="arrow-down">↓</span></td>
      <td>284.9</td>
      <td>255.3</td>
      <td>246.4</td>
      <td>233.8</td>
      <td class="best">191.5</td>
    </tr>
    <tr>
      <td class="metric-name">Sending Bitrate (Mbps) <span class="arrow-up">↑</span></td>
      <td>3.8</td>
      <td>5.5</td>
      <td>5.8</td>
      <td>6.1</td>
      <td class="best">6.2</td>
    </tr>
  </tbody>
</table>
</div>

### Network-Level Improvements

<div class="row">
  <div class="col-md-8">
    {% include figure.liquid path="assets/img/wixor-network-perf.png" title="Network-Level Performance Metrics" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-md-4">
    <ul style="list-style: none; padding-left: 0; margin-top: 1rem;">
      <li style="margin-bottom: 0.75rem;">• Wixor's fairness and spectral efficiency are as high as the default TDD policy (less than 2% difference).</li>
      <li style="margin-bottom: 0.75rem;">• The gap between Wixor and the optimal TDD policy is small: Wixor is within 82.2% and 88.0% of the Oracle for per-packet latency and BS throughput, respectively.</li>
      <li style="margin-bottom: 0.75rem;">• Wixor's gains are larger for higher mobility scenarios.</li>
    </ul>
  </div>
</div>

## Collaborators

This work is a collaboration between:

<div style="display: flex; align-items: center; justify-content: center; flex-wrap: wrap; margin: 0.1rem 0 0.5rem 0; gap: 4rem;">
  <div style="text-align: center;">
    <a href="https://www.usc.edu/" target="_blank" style="text-decoration: none;">
      <img src="/assets/img/logo-usc.png" alt="USC" style="max-width: 180px; height: auto; filter: grayscale(0%);">
    </a>
  </div>
  <div style="text-align: center;">
    <a href="https://www.hpe.com/" target="_blank" style="text-decoration: none;">
      <img src="/assets/img/logo-hpe.png" alt="HPE" style="max-width: 180px; height: auto; filter: grayscale(0%);">
    </a>
  </div>
</div>

## References

```
Ahmad Hassan, Shivang Aggarwal, Mohamed Ibrahim, Puneet Sharma, and Feng Qian. 
2024. Wixor: Dynamic TDD Policy Adaptation for 5G/xG Networks. 
Proc. ACM Netw. 2, CoNEXT4, Article 38 (December 2024), 24 pages. 
https://doi.org/10.1145/3696395
```

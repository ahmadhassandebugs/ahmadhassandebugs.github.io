---
layout: page
permalink: /publications/
title: publications
description: <strong> * </strong> denotes equal contribution
years: [2021, 2022]
nav: true
---

An up-to-date list is available on [Google Scholar](https://scholar.google.de/citations?user=dGhFQesAAAAJ&hl=en).

<!-- _pages/publications.md -->
<div class="publications">

{%- for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}

</div>

---
layout: home

hero:
  name: 'Math Modeling BAO'
  text: '以赛题为入口的可复现建模教程'
  tagline: 先按 Best Practice 建立读法，再进入赛题索引，对照 Baseline、Advanced、Outstanding 和 BAO PDF。
  image:
    src: /bao-progression-banner.svg
    alt: Baseline Advanced Outstanding progression
  actions:
    - theme: brand
      text: 先读 Best Practice
      link: /best_practie/
    - theme: alt
      text: 浏览赛题库
      link: /mcm-track/problem-index
    - theme: alt
      text: 运行复现
      link: /reference/reproduce

features:
  - title: 01 Best Practice
    details: 先理解评奖标准、B/A/O 递进、混合题型、数据来源、文献综述和数模论文写法。
  - title: 02 赛题整体索引
    details: MCM/ICM 与 CUMCM 都按完整赛题组织，赛题索引已融入 Baseline、Advanced 和 Outstanding PDF。
  - title: 03 完整 B/A/O 案例
    details: 当前正式标记 15 篇 O 奖复现，分为三大题型经典 6 篇和 2023-2025 MCM ABC 9 篇。
  - title: 04 可复现代码结果
    details: 每个案例保留 solution.py、result.json、report.md 和 artifacts，支持统一 runner 批量复现。
---

<section class="bao-abstract-showcase">
  <div class="bao-section-eyebrow">MCM 2015-A Ebola</div>
  <h2>一眼看 B/A/O 论文长什么样</h2>
  <p>以正式代表案例 MCM 2015-A 为例，同一道赛题会同时提供 Baseline、Advanced 和 Outstanding 三层论文。读者可以先看摘要页差异，再进入完整案例逐层研读模型、代码和结果。</p>
  <div class="bao-preview-grid">
    <a class="bao-preview-card bao-preview-baseline" href="best_practie/bao-mcm-2015-a-ebola">
      <span class="bao-preview-level">Baseline</span>
      <span class="bao-preview-caption">能跑的基础模型</span>
      <img src="/bao-previews/mcm-2015-a-baseline-abstract.png" alt="MCM 2015-A Baseline abstract page">
    </a>
    <a class="bao-preview-card bao-preview-advanced" href="best_practie/bao-mcm-2015-a-ebola">
      <span class="bao-preview-level">Advanced</span>
      <span class="bao-preview-caption">接入题意、数据与约束</span>
      <img src="/bao-previews/mcm-2015-a-advanced-abstract.png" alt="MCM 2015-A Advanced abstract page">
    </a>
    <a class="bao-preview-card bao-preview-outstanding" href="best_practie/bao-mcm-2015-a-ebola">
      <span class="bao-preview-level">Outstanding</span>
      <span class="bao-preview-caption">对照 O 奖论文复现</span>
      <img src="/bao-previews/mcm-2015-a-outstanding-abstract.png" alt="MCM 2015-A Outstanding paper summary page">
    </a>
  </div>
</section>

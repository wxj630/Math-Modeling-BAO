import { defineConfig } from 'vitepress'

const isEdgeOne = process.env.EDGEONE === '1'
const baseConfig = isEdgeOne ? '/' : '/Math-Modeling-BAO/'

export default defineConfig({
  lang: 'zh-CN',
  title: 'Math Modeling BAO',
  description: 'MCM 与 CUMCM 可复现建模解法教程',
  base: baseConfig,
  markdown: {
    math: true
  },
  themeConfig: {
    logo: {
      light: '/bao-logo.svg',
      dark: '/bao-logo.svg',
      alt: 'Math Modeling BAO'
    },
    nav: [
      { text: 'Best Practice', link: '/best_practie/' },
      { text: '学习路线', link: '/tutorial/' },
      { text: 'MCM 赛题库', link: '/mcm-track/problem-index' },
      { text: 'CUMCM 赛题库', link: '/cumcm-track/problem-index' },
      { text: '复现指南', link: '/reference/reproduce' },
      { text: 'GitHub', link: 'https://github.com/wxj630/Math-Modeling-BAO' }
    ],
    search: {
      provider: 'local',
      options: {
        translations: {
          button: {
            buttonText: '搜索文档',
            buttonAriaLabel: '搜索文档'
          },
          modal: {
            noResultsText: '无法找到相关结果',
            resetButtonTitle: '清除查询条件',
            footer: {
              selectText: '选择',
              navigateText: '切换'
            }
          }
        }
      }
    },
    sidebar: [
      {
        text: 'Best Practice',
        items: [
          { text: '00 索引总图', link: '/best_practie/' },
          { text: '01 评奖标准', link: '/best_practie/award-evaluation-rules' },
          { text: '02 B/A/O 递进方法', link: '/best_practie/solution-levels-and-judging-rubric' },
          { text: '03 混合题型', link: '/best_practie/mixed-problem-patterns' },
          { text: '04 求解器选择', link: '/best_practie/solver-selection-guide' },
          { text: '05 数据来源', link: '/best_practie/data-source-practice' },
          { text: '06 文献综述', link: '/best_practie/literature-review-practice' },
          { text: '07 数模论文 vs 科研论文', link: '/best_practie/modeling-paper-vs-research-paper' },
          { text: '08 LLM 时代 O 奖观察', link: '/best_practie/llm-era-outstanding-patterns' }
        ]
      },
      {
        text: '教程主线',
        items: [
          { text: '从归档到论文', link: '/tutorial/' },
          { text: 'Baseline Solution', link: '/tutorial/baseline' },
          { text: 'Advanced Solution', link: '/tutorial/advanced' },
          { text: 'Outstanding Solution', link: '/tutorial/outstanding' }
        ]
      },
      {
        text: '竞赛赛道',
        items: [
          { text: 'MCM/ICM 赛题入口', link: '/mcm-track/' },
          { text: 'MCM/ICM 赛题索引（含 BAO PDF）', link: '/mcm-track/problem-index' },
          { text: 'CUMCM 赛题入口', link: '/cumcm-track/' },
          { text: 'CUMCM 赛题索引（含 BAO PDF）', link: '/cumcm-track/problem-index' }
        ]
      },
      {
        text: '完整 B/A/O 代表案例',
        items: [
          { text: '01 MCM 2015-A Ebola', link: '/best_practie/bao-mcm-2015-a-ebola' },
          { text: '02 CUMCM 2018-A 高温作业', link: '/best_practie/bao-cumcm-2018-a-heat-clothing' },
          { text: '03 MCM 2017-B Toll Plaza', link: '/best_practie/bao-mcm-2017-b-toll-plaza' },
          { text: '04 CUMCM 2020-B 穿越沙漠', link: '/best_practie/bao-cumcm-2020-b-desert-crossing' },
          { text: '05 MCM 2019-C Opioids', link: '/best_practie/bao-mcm-2019-c-opioid' },
          { text: '06 CUMCM 2020-C 信贷决策', link: '/best_practie/bao-cumcm-2020-c-credit' },
          { text: '07 MCM 2023-A Plant Community', link: '/best_practie/bao-mcm-2023-a-plant-community' },
          { text: '08 MCM 2023-B Maasai Mara', link: '/best_practie/bao-mcm-2023-b-maasai-mara' },
          { text: '09 MCM 2023-C Wordle', link: '/best_practie/bao-mcm-2023-c-wordle' },
          { text: '10 MCM 2024-A Lamprey', link: '/best_practie/bao-mcm-2024-a-lamprey' },
          { text: '11 MCM 2024-B Submersible', link: '/best_practie/bao-mcm-2024-b-submersible-search' },
          { text: '12 MCM 2024-C Tennis', link: '/best_practie/bao-mcm-2024-c-tennis-momentum' },
          { text: '13 MCM 2025-A Stair Wear', link: '/best_practie/bao-mcm-2025-a-stair-wear' },
          { text: '14 MCM 2025-B Tourism', link: '/best_practie/bao-mcm-2025-b-juneau-tourism' },
          { text: '15 MCM 2025-C Olympics', link: '/best_practie/bao-mcm-2025-c-olympic-medals' }
        ]
      },
      {
        text: '参考',
        items: [
          { text: '归档路径说明', link: '/reference/archive-map' },
          { text: '运行与复现', link: '/reference/reproduce' },
          { text: 'PDF 下载清单', link: '/reference/report-pdf-library' },
          { text: 'Outstanding 覆盖清单', link: '/reference/outstanding-coverage-audit' },
          { text: 'MCM 原始归档', link: '/mcm-2015-2025/' }
        ]
      }
    ],
    socialLinks: [
      { icon: 'github', link: 'https://github.com/wxj630/Math-Modeling-BAO' }
    ],
    editLink: {
      pattern: 'https://github.com/wxj630/Math-Modeling-BAO/blob/main/docs/:path',
      text: '在 GitHub 上编辑此页'
    },
    footer: {
      message: 'Math Modeling BAO tutorial site',
      copyright: 'Released for learning, reproducible modeling, and archive review.'
    }
  }
})

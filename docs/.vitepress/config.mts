import { defineConfig } from 'vitepress'

const isEdgeOne = process.env.EDGEONE === '1'
const baseConfig = isEdgeOne ? '/' : '/Math-Modeling-World/'

export default defineConfig({
  lang: 'zh-CN',
  title: 'Math Modeling World',
  description: 'MCM 与 CUMCM 可复现建模解法教程',
  base: baseConfig,
  markdown: {
    math: true
  },
  themeConfig: {
    nav: [
      { text: '学习路线', link: '/tutorial/' },
      { text: 'MCM', link: '/mcm-track/' },
      { text: 'CUMCM', link: '/cumcm-track/' },
      { text: '复现指南', link: '/reference/reproduce' },
      { text: 'GitHub', link: 'https://github.com/wxj630/Math-Modeling-World' }
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
          { text: 'MCM/ICM 解法教程', link: '/mcm-track/' },
          { text: 'MCM/ICM 全量索引', link: '/mcm-track/solution-index' },
          { text: 'CUMCM 解法教程', link: '/cumcm-track/' },
          { text: 'CUMCM 全量索引', link: '/cumcm-track/solution-index' }
        ]
      },
      {
        text: '代表案例',
        items: [
          { text: 'MCM 2024-C 网球势头', link: '/case-studies/mcm-2024-c' },
          { text: 'CUMCM 2024-C 农作物规划', link: '/case-studies/cumcm-2024-c' }
        ]
      },
      {
        text: '参考',
        items: [
          { text: '归档路径说明', link: '/reference/archive-map' },
          { text: '运行与复现', link: '/reference/reproduce' },
          { text: 'MCM 原始归档', link: '/mcm-2015-2025/' }
        ]
      }
    ],
    socialLinks: [
      { icon: 'github', link: 'https://github.com/wxj630/Math-Modeling-World' }
    ],
    editLink: {
      pattern: 'https://github.com/wxj630/Math-Modeling-World/blob/main/docs/:path',
      text: '在 GitHub 上编辑此页'
    },
    footer: {
      message: 'Math Modeling World tutorial site',
      copyright: 'Released for learning, reproducible modeling, and archive review.'
    }
  }
})

# 2025 CUMCM-B Outstanding 复现：B157 干涉测厚

## 复现定位
- 论文：B157，碳化硅外延层厚度的双光束和多光束干涉法测量研究。
- 本脚本直接读取附件 1-4 的红外反射谱，完成 FFT/峰间距初值、Snell-Cauchy 折射率修正、双光束非线性拟合和 Airy 多光束修正。

## 关键结果
| sample | two-beam um | Airy um | spread um | recommended |
|---|---:|---:|---:|---|
| Si | 10.5145 | 10.5144 | 1.9032 | two-beam least-squares |
| SiC | 16.4925 | 8.9815 | 2.0371 | Airy multi-beam correction |

## 相比 Advanced 的提升
从厚度公式和摘要升级为 O 奖级反演流程：直接处理四个光谱附件，先由 FFT/峰间距给初值，再做双角非线性拟合和 Airy 多光束误差校正，并输出残差图验证可靠性。

## 输出产物
- `thickness_fit_table`: `cumcm/outstanding_solutions/2025/B/B157/artifacts/thickness_fit_table.csv`
- `joint_thickness_summary`: `cumcm/outstanding_solutions/2025/B/B157/artifacts/joint_thickness_summary.csv`
- `spectra_fit_plot`: `cumcm/outstanding_solutions/2025/B/B157/artifacts/spectra_fit_plot.png`
- `residual_plot`: `cumcm/outstanding_solutions/2025/B/B157/artifacts/residual_plot.png`

# 🥋 RoboDojo 榜单资源

> RoboDojo 是首个统一"仿真+真机"的通用机器人操作评测平台（arXiv 2607.04434），由港大 MMLab 罗平教授与博士生陈天行发起，联合 UC Berkeley、清华、北大、MIT 等全球 18 所学术机构推出，RoboTwin 原班团队延续开发。采用"仿真+真机"双榜单机制，榜单治理由公益性组织 AI MMLab Club 基金会负责，双盲打分，既看结果也看过程。
>
> - 📄 论文：https://arxiv.org/abs/2607.04434
> - 🌐 主页：https://robodojo-benchmark.com/
> - 🐙 代码：https://github.com/RoboDojo-Benchmark/RoboDojo
> - 任务规模：42 仿真任务 + 18 真机任务

## 官方榜单概况（2026.08 公开）

- **仿真榜单**：集成评测 30 个代表性机器人操作策略（Hy-Embodied-0.5-VLA、Spatial Forcing、π₀.₅、X-VLA、GR00T-N1.7、π₀、OpenVLA-OFT 等）。榜首 Hy-Embodied-0.5-VLA 平均分 13.07、平均成功率 8.80%，整体表现处于很低区间，暴露 VLA"不够稳"短板。
- **真机榜单**：榜首 π₀.₅ 总体成功率 12.8%、平均分 22.9，头部梯队含 InternVLA-A1、GalaxeaVLA、Xiaomi-Robotics-0、X-VLA 等，成功率普遍仅个位数到十几个百分点。
- **人类基准**：人类专家平均成功率 76.03%、平均分 80.42，与模型差距悬殊。
- **国内登顶记录**：2026.08 重庆德讯马（Dexmal 原力灵机）DM0.5 登顶 RoboDojo 榜单（官方报道 24.90 分；榜单位次后续有更新）。

## 论文专项评测：GPT 6 Astra as an Embodied Policy

> 研究标题：**GPT 6 Astra as an Embodied Policy** — *A comparative study of direct end-effector control and hybrid control with π₀.₅*
> 作者：Yu-Mool Shu, Lipxin Zheng
> 内容：将 OpenAI 旗舰模型 GPT-6 Astra（2026.09 发布）直接接入机械臂末端执行器控制闭环，对比"直接控制"与"与 π₀.₅ 混合控制"两种范式；评测在 **RoboDojo-Sim · 10 tasks** 上进行。
> ⚠️ 以下榜单为该论文在 RoboDojo 基准上自行评测的对比结果（10 任务平均分），**非官方 RoboDojo 排行榜**。

### Mean Score Across Ten Tasks（12 个模型）

| 排名 | 模型 | 平均分 |
|:---:|:-----|:---:|
| 1 | **π₀.₅ + GPT 6 Astra（混合控制）** | **62.6** |
| 2 | Galaxea G0.5 | 38.26 |
| 3 | GPT 6 Astra Direct（直接末端控制） | 37.81 |
| 4 | Xiaomi R1 | 33.97 |
| 5 | OpenWAM-α | 32.73 |
| 6 | DM0.5 | 31.82 |
| 7 | Meituan R0 | 28.33 |
| 8 | Spatial Forcing | 24.96 |
| 9 | π₀.₅ | 24.43 |
| 10 | StarVLA-PI | 22.36 |
| 11 | InternVLA A1.5 | 21.74 |
| 12 | Hy-VLA 0.5 | 21.16 |

### 要点解读

- **混合控制增益显著**：π₀.₅ + GPT 6 Astra（62.6）相比单独 π₀.₅（24.43）提升 **38.17 分（+156%）**，说明 LLM 作为高层策略与 VLA 低层控制的组合能大幅改善任务达成率。
- **直接控制也能打**：GPT 6 Astra 直接输出末端执行器动作（37.81）即超过所有专用 VLA 基线（除 Galaxea G0.5 外），验证通用大模型作为具身策略基座的可行性，但逊于 Galaxea 专用模型。
- **榜单系论文内部评测**：得分与官方 RoboDojo 仿真榜单（榜首 13.07 分）口径不同（10 任务子集 vs 42 任务全集），不直接可比。

---

*资源来源：论文/项目页截图（2026-09-14 收录）；RoboDojo 官方论文 arXiv:2607.04434 与主页 robodojo-benchmark.com。GitHub 链接为论文公开渠道，具体仓库地址以论文原文为准。*
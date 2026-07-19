# Awesome Agent World Model 🧠🌍

> **智能体世界模型（Agent World Model）**——让 AI 在"想象"中试错、在虚拟中成长的前沿技术栈。
> 本列表全面覆盖从环境生成管线到神经世界模拟器、从学术论文到工业落地的全生态资源，涵盖 **920+** 高质量条目。内容按主题拆分为 5 个子文档，便于浏览。
> 由 [isLinXu](https://github.com/isLinXu) 维护，持续更新中。欢迎 Star ⭐ 与贡献！

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![GitHub Stars](https://img.shields.io/github/stars/isLinXu/Awesome-Agent-World-Model?style=social)](https://github.com/isLinXu/Awesome-Agent-World-Model)
[![Last Update](https://img.shields.io/badge/Last%20Update-2026-07-18-brightgreen)]()
[![Version](https://img.shields.io/badge/Version-8.0-blue)]()
[![Coverage](https://img.shields.io/badge/Coverage-99%25%2B-brightgreen)]()
[![Entries](https://img.shields.io/badge/Entries-904%2B-orange)]()

---

## 📊 执行摘要

本 Awesome List 经过十二轮深度调研与系统性质量审查，已从初始的 **79 个条目** 扩展至 **904 个高质量资源条目（覆盖率 99.5%+）**。v8.0 将内容按主题拆分为 5 个子文档，从"单一长文档"升级为"模块化文档体系"。

**v7.2 核心改进**：

- **结构修复**：清理"奠基性工作 (2018-2022)"章节中混入的 47 篇未来年份论文，保留真正的 5 篇奠基性工作（World Models、PlaNet、DreamerV1/V2、IRIS）
- **去重优化**：移除 32 个跨章节重复条目，提升内容质量与可读性
- **安全与对齐**：新增 8 篇安全论文，从 1 篇扩充至 9 篇，覆盖对抗攻击、形式化验证、物理合理性检测等方向
- **历史完整性**：补充 8 篇 2023-2024 里程碑论文（Diffusion Policy、RT-2、Octo、OpenVLA、π₀ 等）
- **理论基础**：新增 5 篇 Model-Based RL 经典工作（PILCO、PETS、MBPO、MuZero、SVG）
- **GitHub Actions**：完善自动化论文追踪系统的配置指南


**v8.0 核心改进**（文档架构重构）：

- **文档拆分**：将 2600+ 行的单一 README 按主题拆分为 5 个子文档，主 README 精简至 ~200 行，保留执行摘要、核心项目和文档导航
- **GitHub Actions 生效**：自动化论文追踪系统已成功运行，每日自动拉取 arXiv/HuggingFace/Papers with Code 新论文并写入 `docs/papers.md`
- **脚本适配**：`auto_update.py` 和 `update_metadata.py` 已适配新文档结构，跨子文档统计条目数

<details>
<summary>📜 查看历史版本记录 (v6.0–v7.7)</summary>

**v7.7** — ICLR 2025 World Models Workshop 系统整合（30 篇 Workshop 论文 + 3 个评测基准）

**v7.6** — Qwen-Robot Suite 具身智能三件套（Nav/Manip/World/Claw + 4 个评测基准）

**v7.5** — Xun Huang 视频世界模型五大属性框架（因果性/交互性/持久性/实时性/物理准确性 + 23 篇论文）

**v7.4** — Themesis 五大竞争路线深度对比（Genie 3 / Marble / LeJEPA / AXIOM / 神经符号）

**v7.3** — 深度内容补充（经典视频预测、时间线、评估指标、科学应用、阅读路线图、开放问题、术语表）

**v7.2** — 结构修复（清理 47 篇错年份论文 + 安全论文 1→9 篇 + MBRL 经典理论补充）

**v7.0** — 六大流派分类、NVIDIA Cosmos 3、World Labs Marble 1.1、类脑 VLA、WAIC 2026 产业拐点、4D 世界模型突破

**v6.0** — 占位符修复、代码示例与实战指南、性能对比矩阵、产业报告整合、全球融资生态更新

> 完整版本历程详见 [docs/references.md](docs/references.md)

</details>

---

## 📖 目录

### 本文件
- [执行摘要](#-执行摘要)
- [微信交流群](#-微信交流群)
- [核心项目](#核心项目)
- [文档导航](#-文档导航)

### 子文档（点击进入）
- [🔧 工具与框架](docs/frameworks.md) — 世界模型框架、VLA 模型、RL 训练、物理仿真、数据集、评测基准
- [📚 研究论文](docs/papers.md) — 奠基性工作、2023-2026 论文、ICLR Workshop、流派对比、综述
- [🏭 业界应用](docs/industry.md) — 自动驾驶、机器人、初创公司、学习资源、社区生态
- [📈 技术深度](docs/technical.md) — 技术全景对比、发展时间线、挑战与开放问题、快速入门、架构图示
- [📝 附录](docs/references.md) — BibTeX、评估报告、贡献指南、术语表、参考文献、版本历程

---

## 💬 微信交流群

欢迎加入【World Model】we are the world 交流群，与全球世界模型研究者共同探讨前沿技术！

> 群聊：【World Model】we are the world
> 该二维码7天内（7月24日前）有效，过期后请通过 GitHub Issues 获取最新二维码

<img src="assets/wechat-group-qr.jpg" alt="World Model 微信交流群" width="240" />

---

## 核心项目

> 两个定义"Agent World Model"概念的开源旗舰项目，分别代表了**环境生成**与**环境预测**两条技术路线。

### 🏭 Snowflake-Labs/agent-world-model
[![GitHub Stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https://api.github.com/repos/Snowflake-Labs/agent-world-model)](https://github.com/Snowflake-Labs/agent-world-model)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue)](https://github.com/Snowflake-Labs/agent-world-model)
[![Status](https://img.shields.io/badge/Status-🟢%20Active-brightgreen)]()

- **全称**：Agent World Model — 全自动合成环境生成管线
- **核心定位**：通过代码生成 + SQL 数据库后端，为智能体 RL 训练提供**无限、可验证、零幻觉**的合成环境 [20]
- **关键能力**：
  - 基于种子集扩展生成 1,000 个独特场景与 10,000+ 任务
  - 自动合成符合 **MCP 协议** 的环境接口与验证器
  - 产出 35,000+ 可执行工具调用
- **模型系列**：Arctic-AWM (4B / 8B / 14B)，其中 14B 基于 Qwen2.5 架构专为 MCP 优化
- **数据集**：[Snowflake/AgentWorldModel-1K](https://huggingface.co/datasets/Snowflake/AgentWorldModel-1K) — 1,000 个预合成环境
- **论文**：*Agent World Model: Infinity Synthetic Environments for Agentic Reinforcement Learning* — ICML 2026 接收
- **生态集成**：已并入 [meta-pytorch/OpenEnv](https://github.com/meta-pytorch/OpenEnv)，成为 PyTorch 生态标准组件
- **商业落地**：支撑 Snowflake CoWork、CoCo 等商业智能体产品
- **仓库**：[github.com/Snowflake-Labs/agent-world-model](https://github.com/Snowflake-Labs/agent-world-model)

### 🌏 QwenLM/Qwen-AgentWorld
[![GitHub Stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https://api.github.com/repos/QwenLM/Qwen-AgentWorld)](https://github.com/QwenLM/Qwen-AgentWorld)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue)](https://github.com/QwenLM/Qwen-AgentWorld)
[![Status](https://img.shields.io/badge/Status-🟢%20Active-brightgreen)]()

- **全称**：Qwen-AgentWorld — 原生语言世界模型 (Native Language World Model)
- **核心定位**：通过单一 MoE 模型模拟 **MCP、Search、Terminal、SWE、Android、Web、OS** 七大数字交互领域，预测"世界如何反应" [21]
- **关键能力**：
  - 256K 超长上下文窗口，维持长程多轮交互状态一致性
  - 对未见环境（如 OpenClaw）具备零样本泛化能力
  - 支持可控扰动注入（网络超时、磁盘满等）以训练智能体鲁棒性
- **模型系列**：Qwen-AgentWorld-35B-A3B (开源) / 397B-A17B (旗舰)
- **训练流程**：三阶段 CPT → SFT → RL (GSPO 算法，1000 万条真实交互轨迹)
- **基准**：发布 **AgentWorldBench**，旗舰模型得分 58.71，超越 GPT-5.4 (58.25)
- **论文**：*Qwen-AgentWorld: Language World Models for General Agents* — arXiv:2606.24597
- **仓库**：[github.com/QwenLM/Qwen-AgentWorld](https://github.com/QwenLM/Qwen-AgentWorld)

---


---

## 📂 文档导航

> 本项目内容已按主题拆分为多个子文档，便于浏览和维护。点击下方链接进入对应章节。

| 文档 | 内容 | 链接 |
|:-----|:-----|:-----|
| **🔧 工具与框架** | 世界模型框架、多模态世界模型、VLA 模型、Agent 编排、RL 训练、物理仿真、边缘部署、数据集、评测基准、评估指标 | [docs/frameworks.md](docs/frameworks.md) |
| **📚 研究论文** | 奠基性工作、经典视频预测、2023-2026 论文、ICLR Workshop 论文、Agent 范式、安全对齐、综述、流派对比 | [docs/papers.md](docs/papers.md) |
| **🏭 业界应用** | 自动驾驶、机器人、游戏 VR、工业应用、科学应用、初创独角兽、学习资源、社区生态 | [docs/industry.md](docs/industry.md) |
| **📈 技术深度** | 技术全景对比、发展时间线、关键挑战与开放问题、快速入门指南、架构图示 | [docs/technical.md](docs/technical.md) |
| **📝 附录** | BibTeX 引用导出、全面性评估报告、贡献指南、术语表、参考文献、版本演进历程 | [docs/references.md](docs/references.md) |

---


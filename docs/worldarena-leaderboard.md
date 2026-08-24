> [⬅ 返回主目录](../README.md)  |  [📖 文档导航](../README.md#-文档导航)

## 🏆 WorldArena 榜单模型资源汇总

> [WorldArena](https://worldarena.ai) 是 CVPR 2026 官方设立的世界模型评测平台，IROS 2026 Challenge 赛道涵盖视频质量评测、在线 RL 环境与真实机器人 WAM 任务。截至 2026 年 7 月，已有 126+ 模型参评。
>
> 本页面系统整理 WorldArena 榜单登顶模型的论文、项目主页、代码仓库与模型权重链接。

### 榜单总览

| 排名 | 模型 | 团队 | 登顶时间 | 综合得分 | 关键维度 |
|:---:|:-----|:-----|:-------:|:------:|:--------|
| 🥇 | **Xiaomi-Robotics-U0** | 小米机器人 | 2026.07 | **73.64** | WorldArena 2.0 总分第一（126 模型参评） |
| 🥈 | **PAIWorld** | 中科院工业 AI 研究所 | 2026.06 | **72.31** | 综合得分登顶 |
| 🥉 | **GE-Sim 2.0** | 智元机器人 (AGIBOT) | 2026.07 | **68.26** | CVPR 2026 Track-1 冠军，Action Following 48.23 |
| 4 | **Pelican-Unify 1.0** | 北京人形 (X-Humanoid) | 2026.06 | **66.03** | 3D Accuracy 98.12 |
| 5 | **GigaWorld-1** | 极佳视界 | 2026.05 | **>60** | 首个综合得分突破 60 |
| 6 | **PhysBrain 1.0** | 深度机智 (DeepCybo) | 2026.05 | — | 榜单榜首 |
| 7 | **ABot-PhysWorld** | 高德/阿里巴巴 | 2026.04 | — | WorldArena 榜单第一（物理对齐维度） |
| 8 | **WorldScape 0.2** | Manifold AI | 2026.04 | — | 物理可信维度第一 |
| 9 | **FlowWAM** | 中科第五纪 | 2026.04 | — | Physics Adherence + 3D Accuracy 双维度第一 |
| 10 | **Ctrl-World** | 清华 + 斯坦福 | 2026.02 | — | 具身任务能力维度第一 |

---

### 模型详细信息

#### 1. Xiaomi-Robotics-U0

> 小米机器人推出的统一具身合成世界基础模型，2026 年 7 月以 73.64 分登顶 WorldArena 2.0 总分第一（126 模型参评）。

| 资源 | 链接 |
|:-----|:-----|
| 📄 论文 | [Xiaomi-Robotics-U0: Unified Embodied Synthesis with World Foundation Model](https://arxiv.org/abs/2607.11643) |
| 🌐 项目主页 | [robotics.xiaomi.com/xiaomi-robotics-u0](https://robotics.xiaomi.com/xiaomi-robotics-u0.html) |
| 💻 代码仓库 | [github.com/XiaomiRobotics/Xiaomi-Robotics-U0](https://github.com/XiaomiRobotics/Xiaomi-Robotics-U0) |
| 🤗 模型权重 | [huggingface.co/collections/XiaomiRobotics/xiaomi-robotics-u0](https://huggingface.co/collections/XiaomiRobotics/xiaomi-robotics-u0) |

---

#### 2. PAIWorld

> 中科院工业人工智能研究所（PAI Lab）推出，2026 年 6 月以 72.31 分登顶 WorldArena 综合得分第一。

| 资源 | 链接 |
|:-----|:-----|
| 📄 论文 | [arXiv:2606.18375](https://arxiv.org/abs/2606.18375) |
| 🌐 项目主页 | [guhuangai.github.io/PAIWorld-Proj](https://guhuangai.github.io/PAIWorld-Proj/) |
| 💻 代码仓库 | 未公开 |
| 🤗 模型权重 | 未公开 |

---

#### 3. Genie Envisioner-Sim 2.0 (GE 2.0)

> 智元机器人（AGIBOT）推出的统一世界基础平台，CVPR 2026 WorldArena Track-1 总分冠军（68.26 分），Action Following 维度 48.23。

| 资源 | 链接 |
|:-----|:-----|
| 📄 论文 | [Genie Envisioner: A Unified World Foundation Platform for Robotic Manipulation](https://arxiv.org/abs/2605.27491) |
| 🌐 项目主页 | [ge-sim-v2.github.io](https://ge-sim-v2.github.io/) |
| 💻 代码仓库 | [github.com/AgibotTech/GE-Sim-V2](https://github.com/AgibotTech/GE-Sim-V2) |
| 🤗 模型权重 | 见 [AgibotTech HuggingFace](https://huggingface.co/AgibotTech)（Genie-Envisioner 系列） |

---

#### 4. Pelican-Unify 1.0 / Pelican-VL

> 北京人形机器人创新中心（X-Humanoid）推出的具身大一统模型，2026 年 6 月以 66.03 分登顶，3D Accuracy 维度 98.12。支持 7B-72B 参数系列。

| 资源 | 链接 |
|:-----|:-----|
| 📄 论文 | [Pelican-Unified 1.0](https://arxiv.org/abs/2605.15153) |
| 🌐 项目主页 | [pelican-vl.github.io](https://pelican-vl.github.io/) |
| 💻 代码仓库 | [github.com/Open-X-Humanoid/pelican-vl](https://github.com/Open-X-Humanoid/pelican-vl) |
| 🤗 模型权重 | [huggingface.co/X-Humanoid/Pelican1.0-VL-72B](https://huggingface.co/X-Humanoid/Pelican1.0-VL-72B)<br>合集：[collections/X-Humanoid/pelican-vl-10](https://huggingface.co/collections/X-Humanoid/pelican-vl-10) |

---

#### 5. GigaWorld-1

> 极佳视界推出，2026 年 5 月登顶，首个综合得分突破 60 分的模型。国内首个世界模型独角兽。

| 资源 | 链接 |
|:-----|:-----|
| 📄 论文 | [GigaWorld-1: A Roadmap to Build World Models for Robot Policy Evaluation](https://arxiv.org/abs/2607.02642) |
| 🌐 项目主页 | [open-gigaai.github.io/giga-world-1](https://open-gigaai.github.io/giga-world-1/) |
| 💻 代码仓库 | [github.com/open-gigaai/giga-world-1](https://github.com/open-gigaai/giga-world-1) |
| 🤗 模型权重 | [huggingface.co/open-gigaai/Giga-World-1](https://huggingface.co/open-gigaai/Giga-World-1)<br>合集：[collections/open-gigaai/cvpr-2026-worldmodel-track](https://huggingface.co/collections/open-gigaai/cvpr-2026-worldmodel-track) |

---

#### 6. PhysBrain 1.0

> 深度机智（DeepCybo）推出，2026 年 5 月登顶 WorldArena 榜首。核心架构为 TwinBrainVLA 双脑融合 + LangForce 训练策略，基于人本位数据连接 VLM 与物理智能。

| 资源 | 链接 |
|:-----|:-----|
| 📄 论文 | [PhysBrain: Human Egocentric Data as a Bridge from Vision Language Models to Physical Intelligence](https://arxiv.org/abs/2512.16793) |
| 🌐 项目主页 | [phys-brain.github.io](https://phys-brain.github.io/)（产品）<br>[zgc-embodyai.github.io/PhysBrain](https://zgc-embodyai.github.io/PhysBrain/)（论文） |
| 💻 代码仓库 | [github.com/Phys-Brain/PhysBrain-VLA](https://github.com/Phys-Brain/PhysBrain-VLA) |
| 🤗 模型权重 | 已开源（含 RoboCasa/LIBERO/SIMPLER 多个 fine-tuned 版本），详见 GitHub 仓库 |

---

#### 7. ABot-PhysWorld

> 高德/阿里巴巴 AMAP CV Lab 推出的 14B 扩散 Transformer 世界模型，2026 年 4 月登顶 WorldArena 榜单第一。物理对齐的交互式世界基础模型。

| 资源 | 链接 |
|:-----|:-----|
| 📄 论文 | [ABot-PhysWorld: Interactive World Foundation Model for Robotic Manipulation with Physics Alignment](https://arxiv.org/abs/2603.23376) |
| 🌐 项目主页 | [github.com/amap-cvlab/ABot-PhysWorld](https://github.com/amap-cvlab/ABot-PhysWorld) |
| 💻 代码仓库 | [github.com/amap-cvlab/ABot-PhysWorld](https://github.com/amap-cvlab/ABot-PhysWorld) |
| 🤗 模型权重 | [ModelScope: amap_cvlab/ABot-PhysWorld](https://www.modelscope.cn/models/amap_cvlab/ABot-PhysWorld)（含训练数据与 EZS-Bench 评测基准） |

---

#### 8. WorldScape 0.2

> Manifold AI（流形空间）推出的统一实时世界模型，2026 年 4 月登顶 WorldArena 物理可信维度第一，WorldScore 榜单总分第一。MoE 架构融合移动与操控。

| 资源 | 链接 |
|:-----|:-----|
| 📄 论文 | [WorldScape: A Unified Real-time World Model Integrating Locomotion And Manipulation](https://manifoldai.cn/assets/file/WorldScape.pdf)（PDF，未上 arXiv） |
| 🌐 项目主页 | [manifoldai.cn/blogs/WorldScape](https://manifoldai.cn/blogs/WorldScape.html)<br>Policy 主页：[manifoldai-research.github.io/WorldScape-Policy](https://manifoldai-research.github.io/WorldScape-Policy/) |
| 💻 代码仓库 | 未公开 |
| 🤗 模型权重 | 未公开 |
| 📌 关联工作 | [RoboScape](https://arxiv.org/abs/2506.23135)（NeurIPS 2025 Spotlight） |

---

#### 9. FlowWAM

> 中科第五纪推出的世界动作模型，2026 年 4 月 23 日登顶 WorldArena 榜单，Physics Adherence（物理遵循）和 3D Accuracy（3D 准确度）两大维度第一。技术路径为 FAM-1 → BridgeV2W → FlowWAM（第三代）。

| 资源 | 链接 |
|:-----|:-----|
| 📄 论文 | 未公开 |
| 🌐 项目主页 | 未公开 |
| 💻 代码仓库 | 未公开 |
| 🤗 模型权重 | 未公开 |
| 📌 备注 | 阿里云 PAI 提供算力支持；关联中科院自动化所；目前仅有新闻报道，论文/代码/权重均未公开 |

---

#### 10. Ctrl-World

> 清华大学（陈建宇团队）+ 斯坦福大学（Chelsea Finn 团队）联合推出，2026 年 2 月登顶 WorldArena 具身任务能力维度第一。ICLR 2026 发表。

| 资源 | 链接 |
|:-----|:-----|
| 📄 论文 | [CTRL-WORLD: A Controllable Generative World Model for Robot Manipulation](https://arxiv.org/abs/2510.10125)（ICLR 2026） |
| 🌐 项目主页 | [ctrl-world.github.io](https://ctrl-world.github.io/) |
| 💻 代码仓库 | [github.com/Robert-gyj/Ctrl-World](https://github.com/Robert-gyj/Ctrl-World) |
| 🤗 模型权重 | 未公开 |

---

### 资源覆盖率统计

| 资源类型 | 已公开 | 未公开 | 覆盖率 |
|:--------|:------:|:------:|:-----:|
| 论文 (arXiv/PDF) | 8 | 2 | 80% |
| 项目主页 | 9 | 1 | 90% |
| 代码仓库 | 7 | 3 | 70% |
| 模型权重 | 5 | 5 | 50% |

> **说明**：FlowWAM 和 WorldScape 0.2 的论文/代码/权重尚未完全公开；Ctrl-World 和 PAIWorld 未公开模型权重；ABot-PhysWorld 的权重发布在 ModelScope 而非 HuggingFace。

---

### 相关评测基准

| 基准 | 描述 | 链接 |
|:-----|:-----|:-----|
| WorldArena 2.0 | CVPR 2026 官方世界模型评测平台 | [worldarena.ai](https://worldarena.ai) |
| WorldArena HF Space | HuggingFace 在线榜单 | [huggingface.co/spaces/WorldArena/WorldArena](https://huggingface.co/spaces/WorldArena/WorldArena) |
| WorldScore | 统一世界生成评测 | [worldscore.github.io](https://worldscore.github.io/) |
| WBench | 交互式世界模型评测（美团+复旦） | [wbench.github.io](https://wbench.github.io/) |

---

*最后更新：2026-08-24 | 数据来源：WorldArena 公开榜单及各模型官方发布*

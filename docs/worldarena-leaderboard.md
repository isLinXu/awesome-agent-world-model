> [⬅ 返回主目录](../README.md)  |  [📖 文档导航](../README.md#-文档导航)

## 🏆 WorldArena 榜单模型资源汇总

> [WorldArena](https://worldarena.ai) 是 CVPR 2026 官方设立的世界模型评测平台，IROS 2026 Challenge 赛道涵盖视频质量评测、在线 RL 环境与真实机器人 WAM 任务。截至 2026 年 7 月，已有 126+ 模型参评。
>
> 本页面按**代码仓库开源程度与托管平台**对 WorldArena 榜单登顶模型进行分类整理，便于研究者按需筛选可复现、可下载的模型资源。

---

### 📊 分类总览

| 类别 | 数量 | 说明 |
|:-----|:----:|:-----|
| 🟢 **全栈开源**（GitHub + HuggingFace） | 6 | 论文、代码、权重全部公开，可直接复现 |
| 🟡 **代码开源 + 国内权重**（GitHub + ModelScope） | 1 | 代码在 GitHub，权重托管于 ModelScope |
| 🟠 **论文公开、代码未开源** | 2 | 有论文或项目页，但代码仓库未开放 |
| 🔴 **完全未公开** | 1 | 仅新闻报道，论文/代码/权重均未公开 |

---

## 🟢 全栈开源（GitHub + HuggingFace）

> 论文、代码仓库、HuggingFace 模型权重全部公开，可完整复现实验。

### Xiaomi-Robotics-U0

> 小米机器人统一具身合成世界基础模型，2026.07 以 73.64 分登顶总分第一（126 模型参评）。

| 资源 | 链接 |
|:-----|:-----|
| 📄 论文 | [Xiaomi-Robotics-U0: Unified Embodied Synthesis with World Foundation Model](https://arxiv.org/abs/2607.11643) |
| 🌐 项目主页 | [robotics.xiaomi.com/xiaomi-robotics-u0](https://robotics.xiaomi.com/xiaomi-robotics-u0.html) |
| 💻 代码仓库 | [github.com/XiaomiRobotics/Xiaomi-Robotics-U0](https://github.com/XiaomiRobotics/Xiaomi-Robotics-U0) |
| 🤗 HuggingFace | [collections/XiaomiRobotics/xiaomi-robotics-u0](https://huggingface.co/collections/XiaomiRobotics/xiaomi-robotics-u0) |

---

### Genie Envisioner-Sim 2.0 (GE 2.0)

> 智元机器人（AGIBOT）统一世界基础平台，CVPR 2026 WorldArena Track-1 冠军（68.26 分），Action Following 48.23。

| 资源 | 链接 |
|:-----|:-----|
| 📄 论文 | [Genie Envisioner: A Unified World Foundation Platform for Robotic Manipulation](https://arxiv.org/abs/2605.27491) |
| 🌐 项目主页 | [ge-sim-v2.github.io](https://ge-sim-v2.github.io/) |
| 💻 代码仓库 | [github.com/AgibotTech/GE-Sim-V2](https://github.com/AgibotTech/GE-Sim-V2) |
| 🤗 HuggingFace | [huggingface.co/AgibotTech](https://huggingface.co/AgibotTech)（Genie-Envisioner 系列） |

---

### Pelican-Unify 1.0 / Pelican-VL

> 北京人形机器人创新中心（X-Humanoid）具身大一统模型，66.03 分，3D Accuracy 98.12。支持 7B-72B 参数系列。

| 资源 | 链接 |
|:-----|:-----|
| 📄 论文 | [Pelican-Unified 1.0](https://arxiv.org/abs/2605.15153) |
| 🌐 项目主页 | [pelican-vl.github.io](https://pelican-vl.github.io/) |
| 💻 代码仓库 | [github.com/Open-X-Humanoid/pelican-vl](https://github.com/Open-X-Humanoid/pelican-vl) |
| 🤗 HuggingFace | [X-Humanoid/Pelican1.0-VL-72B](https://huggingface.co/X-Humanoid/Pelican1.0-VL-72B)<br>合集：[collections/X-Humanoid/pelican-vl-10](https://huggingface.co/collections/X-Humanoid/pelican-vl-10) |

---

### GigaWorld-1

> 极佳视界，首个综合得分突破 60 分的模型，国内首个世界模型独角兽。

| 资源 | 链接 |
|:-----|:-----|
| 📄 论文 | [GigaWorld-1: A Roadmap to Build World Models for Robot Policy Evaluation](https://arxiv.org/abs/2607.02642) |
| 🌐 项目主页 | [open-gigaai.github.io/giga-world-1](https://open-gigaai.github.io/giga-world-1/) |
| 💻 代码仓库 | [github.com/open-gigaai/giga-world-1](https://github.com/open-gigaai/giga-world-1) |
| 🤗 HuggingFace | [open-gigaai/Giga-World-1](https://huggingface.co/open-gigaai/Giga-World-1)<br>合集：[collections/open-gigaai/cvpr-2026-worldmodel-track](https://huggingface.co/collections/open-gigaai/cvpr-2026-worldmodel-track) |

---

### PhysBrain 1.0

> 深度机智（DeepCybo），TwinBrainVLA 双脑融合 + LangForce 训练策略，基于人本位数据连接 VLM 与物理智能。

| 资源 | 链接 |
|:-----|:-----|
| 📄 论文 | [PhysBrain: Human Egocentric Data as a Bridge from Vision Language Models to Physical Intelligence](https://arxiv.org/abs/2512.16793) |
| 🌐 项目主页 | [phys-brain.github.io](https://phys-brain.github.io/)（产品）<br>[zgc-embodyai.github.io/PhysBrain](https://zgc-embodyai.github.io/PhysBrain/)（论文） |
| 💻 代码仓库 | [github.com/Phys-Brain/PhysBrain-VLA](https://github.com/Phys-Brain/PhysBrain-VLA) |
| 🤗 HuggingFace | 已开源（含 RoboCasa/LIBERO/SIMPLER 多个 fine-tuned 版本），详见 GitHub 仓库 |

---

### Ctrl-World

> 清华大学（陈建宇）+ 斯坦福大学（Chelsea Finn），ICLR 2026。具身任务能力维度第一。

| 资源 | 链接 |
|:-----|:-----|
| 📄 论文 | [CTRL-WORLD: A Controllable Generative World Model for Robot Manipulation](https://arxiv.org/abs/2510.10125) |
| 🌐 项目主页 | [ctrl-world.github.io](https://ctrl-world.github.io/) |
| 💻 代码仓库 | [github.com/Robert-gyj/Ctrl-World](https://github.com/Robert-gyj/Ctrl-World) |
| 🤗 HuggingFace | 未公开 |

---

## 🟡 代码开源 + 国内权重（GitHub + ModelScope）

> 代码仓库在 GitHub 开放，但模型权重托管于国内平台 ModelScope。

### ABot-PhysWorld

> 高德/阿里巴巴 AMAP CV Lab，14B 扩散 Transformer 世界模型，物理对齐交互式世界基础模型。

| 资源 | 链接 |
|:-----|:-----|
| 📄 论文 | [ABot-PhysWorld: Interactive World Foundation Model for Robotic Manipulation with Physics Alignment](https://arxiv.org/abs/2603.23376) |
| 🌐 项目主页 | [github.com/amap-cvlab/ABot-PhysWorld](https://github.com/amap-cvlab/ABot-PhysWorld) |
| 💻 代码仓库 | [github.com/amap-cvlab/ABot-PhysWorld](https://github.com/amap-cvlab/ABot-PhysWorld) |
| 🔶 ModelScope | [amap_cvlab/ABot-PhysWorld](https://www.modelscope.cn/models/amap_cvlab/ABot-PhysWorld)（含训练数据与 EZS-Bench 评测基准） |

---

## 🟠 论文公开、代码未开源

> 有 arXiv 论文或官方项目页，但代码仓库与模型权重尚未开放。

### PAIWorld

> 中科院工业人工智能研究所（PAI Lab），72.31 分，综合得分登顶。

| 资源 | 链接 | 状态 |
|:-----|:-----|:----:|
| 📄 论文 | [arXiv:2606.18375](https://arxiv.org/abs/2606.18375) | ✅ 已公开 |
| 🌐 项目主页 | [guhuangai.github.io/PAIWorld-Proj](https://guhuangai.github.io/PAIWorld-Proj/) | ✅ 已公开 |
| 💻 代码仓库 | — | ❌ 未开源 |
| 🤗 模型权重 | — | ❌ 未公开 |

---

### WorldScape 0.2

> Manifold AI（流形空间），物理可信维度第一，WorldScore 总分第一。MoE 架构融合移动与操控。

| 资源 | 链接 | 状态 |
|:-----|:-----|:----:|
| 📄 论文 | [WorldScape PDF](https://manifoldai.cn/assets/file/WorldScape.pdf)（官网 PDF，未上 arXiv） | ⚠️ 非 arXiv |
| 🌐 项目主页 | [manifoldai.cn/blogs/WorldScape](https://manifoldai.cn/blogs/WorldScape.html)<br>Policy：[manifoldai-research.github.io/WorldScape-Policy](https://manifoldai-research.github.io/WorldScape-Policy/) | ✅ 已公开 |
| 💻 代码仓库 | — | ❌ 未开源 |
| 🤗 模型权重 | — | ❌ 未公开 |
| 📌 关联工作 | [RoboScape](https://arxiv.org/abs/2506.23135)（NeurIPS 2025 Spotlight） | ✅ 已发表 |

---

## 🔴 完全未公开

> 仅新闻报道或官方宣传提及，论文、代码、权重均未公开。

### FlowWAM

> 中科第五纪（关联中科院自动化所），Physics Adherence + 3D Accuracy 双维度第一。技术路径：FAM-1 → BridgeV2W → FlowWAM（第三代）。

| 资源 | 链接 | 状态 |
|:-----|:-----|:----:|
| 📄 论文 | — | ❌ 未公开 |
| 🌐 项目主页 | — | ❌ 未公开 |
| 💻 代码仓库 | — | ❌ 未开源 |
| 🤗 模型权重 | — | ❌ 未公开 |
| 📌 备注 | 阿里云 PAI 提供算力支持；仅新闻报道提及 | 🔍 待追踪 |

---

## 📈 资源覆盖率统计

| 类别 | 模型数 | 论文 | 代码 | 权重 |
|:-----|:------:|:----:|:----:|:----:|
| 🟢 全栈开源（GitHub + HF） | 6 | 6/6 | 6/6 | 5/6 |
| 🟡 代码开源 + 国内权重 | 1 | 1/1 | 1/1 | 1/1 |
| 🟠 论文公开、代码未开源 | 2 | 2/2 | 0/2 | 0/2 |
| 🔴 完全未公开 | 1 | 0/1 | 0/1 | 0/1 |
| **合计** | **10** | **9/10** | **7/10** | **6/10** |

> **说明**：WorldArena 榜单顶尖模型中，70% 已公开代码仓库，60% 已公开模型权重。未开源模型多为企业/国家队背景（PAIWorld、WorldScape、FlowWAM），可能与商业竞争或技术保密有关。

---

### 相关评测基准

| 基准 | 描述 | 链接 |
|:-----|:-----|:-----|
| WorldArena 2.0 | CVPR 2026 官方世界模型评测平台 | [worldarena.ai](https://worldarena.ai) |
| WorldArena HF Space | HuggingFace 在线榜单 | [huggingface.co/spaces/WorldArena/WorldArena](https://huggingface.co/spaces/WorldArena/WorldArena) |
| WorldScore | 统一世界生成评测 | [worldscore.github.io](https://worldscore.github.io/) |
| WBench | 交互式世界模型评测（美团+复旦） | [wbench.github.io](https://wbench.github.io/) |

---

*最后更新：2026-08-25 | 数据来源：WorldArena 公开榜单及各模型官方发布*


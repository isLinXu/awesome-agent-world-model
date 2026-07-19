> [⬅ 返回主目录](../README.md)  |  [📖 文档导航](../README.md#-文档导航)

## 🏭 业界应用与初创公司

### 自动驾驶

| 企业 | 项目 | 核心能力 | 状态 |
|:-----|:-----|:-----|:-----|
| **Tesla** | FSD v12.5 世界模拟器 | 城市/高速栈统一，生成逆行、极端天气等边缘场景 | 🟢 量产 |
| **NIO (蔚来)** | NWM 世界模型 | 每 0.1 秒推演 216 条轨迹，AEB 覆盖场景提升 6.7 倍 | 🟢 量产 |
| **Wayve** | GAIA-1 / GAIA-2 | 9B→15B 参数生成式世界模型，多视角视频生成，获 $12 亿 D 轮融资 | 🟢 研发 |
| **Momenta** | R7 世界模型 + 港交所 IPO | "物理 AI 第一股"，06880.HK，$3.76 亿基石（奔驰/BYD/BlackRock/GIC），2026.7.8 上市，市值超 700 亿港元，R7 世界模型量产首发 | 🟢 上市 |
| **吉利** | WAM 世界行为模型 | 统一智驾、智能座舱和底盘控制的世界行为模型 | 🟢 研发 |
| **华为乾崑** | WA (World Action) 路线 | 拒绝 VLA，坚持 World Action 路线，车 BU 负责人直言"VLA 不是自动驾驶的真正解" | 🟢 研发 |

### 机器人

| 企业 | 项目 | 核心能力 | 状态 |
|:-----|:-----|:-----|:-----|
| **Figure AI** | Figure 03 + Helix VLA | BMW 工厂完全自主零件排序，无硬编码，$10 亿 C 轮/$390 亿估值 | 🟢 量产 |
| **Tesla Bot** | Optimus Gen 3 | 22-DoF 灵巧手，触觉传感器密度超人类指尖 | 🟢 研发 |
| **Agility Robotics** | Digit v5 | 亚马逊仓库累计作业超 6.5 万小时，SPAC 上市/$25 亿估值 | 🟢 量产 |
| **ANYbotics** | ANYmal X | 全球首款 Zone 1 防爆认证四足机器人，工业巡检 | 🟢 量产 |
| **PAL Robotics** | Kangaroo Pro | 线性执行器实现 2m/s 奔跑速度 | 🟢 研发 |
| **阿里巴巴 (Qwen)** | Qwen-Robot Suite (LAWR) | 三件套具身大模型：Nav（VLN 统一五类导航任务，宇树 Go2 零样本部署 196ms）+ Manip（VLA 80 维统一动作表征，38100h 开源数据，RoboChallenge Table30 第一）+ World（世界模型，860 万视频-文本对，四大基准全面第一，物理规律满分）+ Claw 智能体框架 | 🟢 研发 |

### 游戏与虚拟现实

| 企业 | 项目 | 核心能力 | 状态 |
|:-----|:-----|:-----|:-----|
| **Google DeepMind** | Genie 2 / Genie 3 | 24FPS 实时交互式世界生成，维持数分钟环境一致性 | 🟢 研发 |
| **NVIDIA** | Cosmos + Isaac Sim 6.0 | 物理 AI 平台 + 多后端物理引擎仿真 | 🟢 活跃 |
| **Etched AI** | Sohu 芯片 | 专为 Transformer 推理优化的 ASIC，支持实时世界模型推理 | 🟢 研发 |
| **World Labs** | 3D 空间智能 | 3D 高斯溅射构建内部 3D 地图，$10B 估值 | 🟢 研发 |

### 工业垂直应用

| 企业 | 项目 | 核心能力 | 状态 |
|:-----|:-----|:-----|:-----|
| **ArcelorMittal** | 数字孪生 | 高炉内部化学反应实时模拟，预测性维护 | 🟢 部署 |
| **SurgWorld** | 手术机器人世界模型 | 预测器械与人体组织交互，SATA 数据集训练 | 🟢 研发 |
| **Aigen** | 精准农业机器人 | 基于世界模型的作物生长预测与病虫害预警 | 🟢 部署 |
| **Samsung** | 全 AI 驱动工厂 | 2030 年目标，2026 年量产通用人形机器人 | 🟢 部署 |

### 科学与生物医学应用

> 世界模型正在从"工业执行"向"科学发现"延伸，成为 AI for Science 的新基础设施。以下应用展示了世界模型在分子、生物、气候等领域的潜力 [28]。

| 领域 | 项目/企业 | 核心能力 | 状态 |
|:-----|:-----|:-----|:-----|
| **蛋白质结构预测** | AlphaFold 3 (DeepMind) | 蛋白质-配体复合物结构预测，可视为生物大分子的"世界模型" | 🟢 部署 |
| **分子动力学** | MACE / Allegro | 等变神经网络学习原子间作用势，模拟分子演化轨迹，速度超 DFT 1000 倍 | 🟢 活跃 |
| **药物发现** | Isomorphic Labs | AlphaFold 衍生，预测药物-靶点结合动力学，世界模型驱动虚拟筛选 | 🟢 研发 |
| **手术机器人** | SurgWorld | 预测器械与人体组织交互，SATA 数据集训练，首个手术世界模型 | 🟢 研发 |
| **生物医学文献** | Biomedical WM | 从海量文献学习生物医学知识的世界模型，辅助新发现假设生成 | 🟡 研究 |
| **气候预测** | GraphCast (DeepMind) | 图神经网络学习大气动力学，10 天预测精度超 HRES | 🟢 部署 |
| **天气生成** | AIFS (ECMWF) | 欧洲中期天气预报中心 AI 预测系统，全球大气世界模型 | 🟢 部署 |
| **地球观测** | EO-WM | 地球观测世界模型，将地表视为概率性天气条件环境 | 🟡 研究 |
| **材料科学** | GNoME (DeepMind) | 发现 220 万种新晶体材料，材料空间的"世界模型"探索 | 🟢 部署 |
| **核聚变控制** | DeepMind × EPFL | 强化学习控制托卡马克等离子体，等离子体世界模型 | 🟢 部署 |
| **基因组学** | Nucleotide Transformer | DNA 序列的语言世界模型，预测基因表达与变异影响 | 🟢 活跃 |
| **流行病学** | EpiWM | 传播动力学的世界模型，预测疫情扩散与干预效果 | 🟡 研究 |

### 具身智能初创独角兽

| 企业 | 估值/融资 | 核心亮点 | 状态 |
|:-----|:-----|:-----|:-----|
| **Skild AI** | $14B | 通用机器人基础模型，软银/红杉领投 | 🟢 研发 |
| **World Labs** | $10B | 3D 空间智能，李飞飞创立 | 🟢 研发 |
| **AMI Labs** | €10.3 亿种子轮 | Yann LeCun 创立，押注 JEPA 架构世界模型，LeWM 15M 参数模型，2026.3 成立 | 🟢 研发 |
| **Physical Intelligence** | $2B+ | π₀ 系列 VLA 模型，Flow Matching 技术 | 🟢 研发 |
| **宇树科技 (Unitree)** | 科创板 IPO 获批 | 2025 年人形机器人出货量全球第一（5500+ 台） | 🟢 量产 |
| **智元机器人 (Agibot)** | $10B | 第 15000 台机器人下线，全球 39% 市场份额 | 🟢 量产 |
| **银河通用** | $7B | 具身智能通用操作平台 | 🟢 研发 |
| **戴盟机器人** | — | 触觉传感器与灵巧手技术领先 | 🟢 研发 |
| **X Square Robot (智平方)** | $28 亿估值 | 阿里/美团/字节/小米四巨头联投 | 🟢 研发 |
| **AI² Robotics** | $29 亿估值 | 通用人形机器人 | 🟢 研发 |
| **Neura Robotics** | $14 亿 C 轮 | Tether 领投，认知机器人平台 | 🟢 研发 |
| **Prometheus** | $120 亿/$410 亿估值 | 2026.6.30 年度最大单轮融资 | 🟢 研发 |
| **CarbonSix** | $4000 万 A 轮 | 世界模型驱动的工业机器人 | 🟢 研发 |
| **Preferred Networks** | ¥3873 亿日本政府资助 | 主权级机器人多模态大模型，与三菱重工战略联盟 | 🟢 研发 |
| **MEIL-Analog** | $5 亿合资 | 印度与 Analog Devices 合资，芯片级世界模型 | 🟢 研发 |
| **极佳视界** | 35 亿元融资 | GigaWorld-1 在 WorldArena 登顶（全球唯一 >60 分），国内首个世界模型独角兽 | 🟢 研发 |
| **Verses.ai** | TSXV 上市 | Karl Friston 任首席科学家，AXIOM 主动推断世界模型 + Genius 平台，对象中心建模 | 🟢 研发 |
| **星海图** | 近 30 亿元 (B+B+) | Fast-WAM 世界模型，2 月近 10 亿 B 轮 + 4 月近 20 亿 B+ 轮 | 🟢 研发 |
| **千寻智能** | 45 亿元 (四轮融资) | 2026 年开年三个月内完成四轮融资 | 🟢 研发 |
| **生数科技** | 26 亿元融资 | 投后估值超 120 亿元，传出 2026 港股 IPO 消息 | 🟢 研发 |
| **群核科技** | 港股上市 | 全球首家以空间智能为核心技术底座的上市公司，上市首日大涨 144% | 🟢 上市 |
| **它石智航** | — | AWE 3.5 具身原生模型，1:1 复刻汽车线束产线，千台级工业机器人集群 | 🟢 研发 |
| **General Intuition** | $1.337 亿种子轮 | 游戏数据公司 Medal 衍生，从带动作标签游戏片段学习预测近未来 | 🟢 研发 |
| **Waymo** | Waymo 世界模型 | CVPR 2026 首次曝光，基于 Genie 3 底座，自动驾驶进入"Genie 时代" | 🟢 研发 |

---


## 🎓 学习资源

### 综述与教程

| 资源 | 描述 | 链接 |
|:-----|:-----|:-----|
| **Stanford CS224R** | 深度强化学习与机器人控制，含世界模型专题 | [cs224r.stanford.edu](https://cs224r.stanford.edu) |
| **CMU 16-831** | 机器人学习与规划，含世界模型与 VLA 模块 | [16-831.cmu.edu](https://16-831.cmu.edu) |
| **Lil'Log (Lilian Weng)** | 《Why We Think》深度探讨测试时计算与世界模型模拟 | [lilianweng.github.io](https://lilianweng.github.io/posts/2025-05-01-thinking/) |
| **HuggingFace LeRobot 课程** | 从 SO-100 机械臂数据采集到 VLA 部署的全流程 | [huggingface.co/lerobot](https://huggingface.co/lerobot) |
| **Natural Dreamer** | DreamerV3 PyTorch 简易实现，含 RSSM 逻辑追踪图示 | [github.com/natural-dreamer](https://github.com/natural-dreamer) |
| **AwesomeWorldModels** | "A Comprehensive Survey on World Models for Embodied AI" 综述配套，三轴分类法+GitHub 资源汇总 | [github.com/Li-Zn-H](https://github.com/Li-Zn-H/AwesomeWorldModels) |
| **Themesis: Five Competing Approaches** | 世界模型五大竞争路线深度对比（Genie 3 / Marble / LeJEPA / AXIOM / 神经符号），含融资、首席科学家、架构原理四维分析 | [themesis.com](https://themesis.com/2026/01/07/world-models-five-competing-approaches/) |
| **EntropyTown: World Model Bets** | 李飞飞 vs LeCun vs DeepMind 世界模型路线对比分析 | [entropytown.com](https://entropytown.com/articles/2025-11-13-world-model-lecun-feifei-li/) |
| **Turing Post: LeJEPA 详解** | LeJEPA 理论升级：JEPA 缺失的理论基石是什么 | [turingpost.com](https://www.turingpost.com/p/lejepa) |
| **Latent Space: 李飞飞访谈** | "After LLMs: Spatial Intelligence and World Models" — 李飞飞 & Justin Johnson 深度访谈 | [latent.space](https://www.latent.space/) |
| **Xun Huang: Towards Video World Models** | Stanford 技术博客，提出视频世界模型五大属性框架（因果/交互/持久/实时/物理准确），系统梳理从视频生成到世界模型的路径 | [xunhuang.me](https://www.xunhuang.me/blogs/world_model.html) |
| **Qwen-Robot Suite** | 阿里千问具身智能三件套（Nav+Manip+World），统一语言-导航-操作-世界预测，含 Claw 智能体框架 | [qwen.ai](https://qwen.ai/blog?id=qwen-robotsuite) |

### 视频与课程

| 资源 | 描述 | 链接 |
|:-----|:-----|:-----|
| **Natural Dreamer 视频教程** | 2025 年发布的 RSSM 架构深度拆解教程 | [YouTube](https://youtube.com/@natural-dreamer) |
| **NVIDIA Cosmos 开发者日** | 物理 AI 平台实战工作坊 | [NVIDIA Developer](https://developer.nvidia.com/cosmos) |
| **ICRA 2026 工作坊** | COMPASS/SPARR 等前沿论文作者现场讲解 | [ICRA 2026](https://icra-2026.org) |

### 深度技术博客

| 博客 | 描述 | 链接 |
|:-----|:-----|:-----|
| **Lil'Log** | OpenAI 前安全负责人 Lilian Weng 的技术博客，世界模型与 Agent 系统深度解析 | [lilianweng.github.io](https://lilianweng.github.io) |
| **Meta AI Blog** | V-JEPA 2 官方技术解读 | [ai.meta.com](https://ai.meta.com/blog/v-jepa-at-scale-self-supervised-learning-from-video/) |
| **Wayve Blog** | GAIA-1/GAIA-2 自动驾驶世界模型技术细节 | [wayve.ai](https://wayve.ai/thinking/) |
| **Physical Intelligence Blog** | π₀ 系列 VLA 模型设计哲学与实现细节 | [physicalintelligence.company](https://www.physicalintelligence.company/blog) |
| **Figure AI Blog** | Helix 双系统架构详解 | [figure.ai](https://www.figure.ai/blog/helix-announcement) |
| **DeepMind Blog** | Genie 2/3 交互式世界生成技术 | [deepmind.google](https://deepmind.google/research/genie-3/) |
| **World Labs Blog** | 李飞飞团队空间智能与 3D 世界模型技术解读 | [worldlabs.ai](https://worldlabs.ai/blog) |
| **智元 Genie Blog** | GE-Sim 2.0 世界模型与 GO-2 具身大模型技术细节 | [agibot.com](https://www.agibot.com) |
| **Verses.ai Blog** | AXIOM 主动推断世界模型与 Genius 平台技术解读 | [verses.ai](https://www.verses.ai/blog) |
| **Ben Dickson (TechTalks)** | VL-JEPA 2 技术深度解析：LeCun 的世界模型路线 | [bdtechtalks.com](https://bdtechtalks.com/) |
| **Themesis Blog** | 世界模型五大竞争路线追踪与产业分析 | [themesis.com](https://themesis.com/) |
| **Xun Huang Blog** | Stanford 研究者"Towards Video World Models"深度技术博客，提出视频世界模型五大属性框架 | [xunhuang.me](https://www.xunhuang.me/blogs/world_model.html) |
| **Qwen Blog (Robot Suite)** | 阿里千问具身智能三件套官方技术解读：Nav/Manip/World 架构设计与基准结果 | [qwen.ai](https://qwen.ai/blog?id=qwen-robotsuite) |

### 阅读路线图

> 针对不同背景的读者，提供差异化的阅读路径，避免在海量资源中迷失方向。

#### 🌱 初学者路径（0-3 个月入门）

**目标**：建立世界模型直觉，能跑通一个端到端示例。

| 步骤 | 资源 | 预计时间 | 学习重点 |
|:-----|:-----|:-----|:-----|
| 1 | [Ha & Schmidhuber《World Models》(2018)](https://arxiv.org/abs/1803.10122) | 1 周 | 理解 VAE+MDN-RNN 架构，建立"在想象中训练"的直觉 |
| 2 | [Lil'Log《Why We Think》](https://lilianweng.github.io/posts/2025-05-01-thinking/) | 3 天 | 测试时计算与世界模型模拟的关系 |
| 3 | [Stanford CS224R](https://cs224r.stanford.edu) 前半部分 | 2 周 | 深度 RL 基础 + 世界模型入门 |
| 4 | [HuggingFace LeRobot 课程](https://huggingface.co/lerobot) | 1 周 | 实操：SO-100 机械臂数据采集到 VLA 部署 |
| 5 | 本文档「快速入门指南」第 3 节 | 2 天 | DreamerV3 在 Atari 100k 上训练 |
| 6 | [《A Definition and Roadmap for World Models》](https://arxiv.org/abs/2607.06401) | 3 天 | 最新路线图综述，建立领域全景认知 |

#### 🔬 研究者路径（深入前沿）

**目标**：找到研究空白，产出高质量论文。

| 步骤 | 资源 | 学习重点 |
|:-----|:-----|:-----|
| 1 | **奠基性工作**全表（World Models→IRIS）+ **经典视频预测**（PredRNN→VideoGPT） | 建立完整历史脉络 |
| 2 | **世界模型综述专区**全部 9 篇综述 | 掌握分类法与研究范式 |
| 3 | **世界模型六大流派**对比表 | 选定研究方向（JEPA/空间智能/生成式视频/语言 WM/物理仿真/类脑） |
| 4 | **物理 AI 元年 (2025-2026)** 论文中筛选与自身方向相关的 20 篇精读 | 紧跟前沿 |
| 5 | **关键技术挑战与开放问题**章节 | 定位研究空白 |
| 6 | **安全与对齐论文** | 关注可信世界模型方向 |
| 7 | 顶会 Workshop：[NeurIPS WM Workshop](https://proceedings.neurips.cc)、[ICLR Embodied AI](https://iclr.cc) | 建立学术连接 |

#### 🛠️ 工程师路径（产品落地）

**目标**：选型、部署、优化世界模型系统。

| 步骤 | 资源 | 学习重点 |
|:-----|:-----|:-----|
| 1 | **核心项目**：Snowflake AWM + Qwen-AgentWorld | 理解两条技术路线与适用场景 |
| 2 | **工具与框架**全表 + **物理仿真平台性能对比** | 选型依据 |
| 3 | **VLA 模型推理延迟对比** + **边缘侧部署工具** | 部署优化 |
| 4 | 本文档「快速入门指南」全部 4 个示例 | OpenVLA/OFT/DreamerV3/Isaac Lab 实操 |
| 5 | **评测基准**全表 + **评估指标详解** | 建立评估体系 |
| 6 | **业界应用与初创公司** | 了解产业格局与竞品 |
| 7 | **Sim-to-Real 迁移流程**架构图 | 解决部署核心痛点 |

#### 📊 决策者路径（投资/管理）

**目标**：快速建立产业认知，辅助决策。

| 步骤 | 资源 | 学习重点 |
|:-----|:-----|:-----|
| 1 | **执行摘要** + **历史发展时间线** | 5 分钟掌握领域全貌 |
| 2 | **世界模型六大流派** | 理解技术路线竞争格局 |
| 3 | **业界应用与初创公司** + **具身智能独角兽**全表 | 投资标的扫描 |
| 4 | **两条技术路线对比** | 生态选型 |
| 5 | **全面性评估报告** | 领域成熟度判断 |
| 6 | **中文生态资源** | 中国市场机会 |

---


## 🤝 社区与生态

### 开源社区

| 社区 | 描述 | 链接 |
|:-----|:-----|:-----|
| **HuggingFace** | 世界模型与 VLA 模型权重托管与分发 | [huggingface.co](https://huggingface.co) |
| **Meta PyTorch** | OpenEnv 标准化环境接口生态 | [github.com/meta-pytorch](https://github.com/meta-pytorch) |
| **LangChain** | Agent 编排框架与 MCP 协议生态 | [github.com/langchain-ai](https://github.com/langchain-ai) |
| **LMD0311/Awesome-World-Model** | 收录近 500 篇世界模型论文的元列表 | [github.com/LMD0311](https://github.com/LMD0311/Awesome-World-Model) |

### 会议与活动

| 会议 | 描述 | 时间 |
|:-----|:-----|:-----|
| **ICML 2026** | AWM 论文接收，世界模型专题 | 2026.07 |
| **NeurIPS 2025** | RLVR-World 等前沿论文发表 | 2025.12 |
| **ICLR 2026** | Gaia2 异步环境 Agent 评测 Workshop | 2026.04 |
| **CoRL 2025** | RISE 自我改进机器人策略框架 | 2025.11 |
| **ICRA 2026** | COMPASS/SPARR/SEAL VLA 等论文发表 | 2026.05 |
| **CVPR 2025** | WorldModelBench 首个物理遵循度基准发布 | 2025.06 |
| **WAIC 2026** | 世界模型展示区、300+ 全球首发产品、具身智能 200+ 厂商 | 2026.07.17-20 |
| **ECCV 2026** | 小米 12 篇入选，含自动驾驶世界模型、VLA 决策、安全规划 | 2026.09.08-12 |
| **智源大会 2026** | 世界模型四条路线定义、NeuroVLA 发布、具身产业 CEO 论坛 | 2026.06.13 |

### 学术 Workshop 专区

| Workshop | 会议 | 主题 | 链接 |
|:-----|:-----|:-----|:-----|
| **World Models: Understanding, Modelling and Scaling** | ICLR 2025 | 世界模型理解、建模与扩展——涵盖世界规则理解、训练与评测、跨语言/视觉/控制扩展、通用领域应用；9 位主题演讲者（Schmidhuber、Chelsea Finn、Jeff Clune、Stefano Ermon、Tim Rocktäschel 等），6 篇 Oral + ~50 篇 Poster，Jürgen Schmidhuber 参与 Panel [70] | [ICLR 2025](https://iclr.cc/virtual/2025/workshop/24000) |
| **World Model Workshop** | NeurIPS 2025 | 世界模型从被动预测到主动决策的范式突破 | [NeurIPS 2025](https://proceedings.neurips.cc) |
| **Embodied AI Workshop** | ICLR 2026 | 具身智能与世界模型交叉研究 | [ICLR 2026](https://iclr.cc) |
| **Robot Learning Workshop** | ICRA 2026 | VLA 模型与 Sim-to-Real 迁移 | [ICRA 2026](https://icra-2026.org) |
| **Physical AI Workshop** | CoRL 2025 | 物理仿真与真实世界部署 | [CoRL 2025](https://corl.org) |

### 中文生态资源

| 资源 | 描述 | 链接 |
|:-----|:-----|:-----|
| **智源研究院** | 2026 智源大会"智能体×世界模型×具身智能"终极路线图 | [智源公众号](http://mp.weixin.qq.com/s?__biz=MzY5MzI2NzA5Nw==&mid=2247483908&idx=1) |
| **机器之心** | 世界模型与具身智能前沿报道 | [jiqizhixin.com](https://jiqizhixin.com) |
| **中国信通院 (CAICT)** | 中国首个具身 AI 国家标准（2026.6.1 生效） | [caict.ac.cn](https://www.caict.ac.cn) |
| **工信部 (MIIT)** | 具身智能实景实训专项行动，万台级部署计划 | [miit.gov.cn](https://www.miit.gov.cn) |
| **宇树科技** | 科创板 IPO 获批，全球出货量第一 | [unitree.com](https://www.unitree.com) |
| **智元机器人** | 第 15000 台下线，灵巧手"临界点"独立融资 | [agibot.com](https://www.agibot.com) |
| **戴盟机器人** | 触觉传感器与灵巧手技术领先 | [daimeng.com](https://www.daimeng.com) |
| **擎朗智能** | 融合世界模型的 VLA 架构，商超/咖啡厅/酒店岗位化具身服务 | [keenon.com](https://www.keenon.com) |
| **光轮智能** | SimFoundry 物理仿真基础设施，机器人"数据-评测-部署反馈"闭环 | [simfoundry.ai](https://www.simfoundry.ai) |
| **WorldArena** | 世界模型评测平台，Track-1 视频质量赛道，智元 Genie Envisioner-Sim 2.0 登顶 | [worldarena.ai](https://worldarena.ai) |

---
---

> [⬅ 返回主目录](../README.md)  |  [📖 文档导航](../README.md#-文档导航)

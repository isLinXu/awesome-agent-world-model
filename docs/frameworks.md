> [⬅ 返回主目录](../README.md)  |  [📖 文档导航](../README.md#-文档导航)

## 🔧 工具与框架

### 世界模型框架

> 从像素预测到物理因果推理，覆盖 JEPA、Dreamer、Genie 等主流架构范式。

| 项目 | 描述 | Stars | 状态 |
|:-----|:-----|:------|:-----|
| [danijar/dreamerv3](https://github.com/danijar/dreamerv3) | DreamerV3 官方 JAX 实现，首个在 Minecraft 无人类演示挖到钻石的算法，Nature 2025 正式发表 | ~1.5k | 🟢 活跃 |
| [r2dreamer](https://github.com/r2dreamer/r2dreamer) | PyTorch 版 DreamerV3，推理速度提升 5 倍，2026 年发布 | ~3.5k | 🟢 活跃 |
| [facebookresearch/vjepa](https://github.com/facebookresearch/vjepa) | Meta 官方 V-JEPA / V-JEPA 2 开源实现，联合嵌入预测架构 | ~2k | 🟢 活跃 |
| [hpcaitech/Open-Sora](https://github.com/hpcaitech/Open-Sora) | Colossal-AI 团队维护的低成本大规模视频生成流水线 | ~20k | 🟢 活跃 |
| [NVIDIA/Cosmos](https://www.nvidia.com/en-us/ai-data-science/foundation-models/) | 物理 AI 平台，含 Cosmos Predict 与 Cosmos Reason，14 天处理 2000 万小时视频 | — | 🟢 活跃 |
| [google-deepmind/unisim](https://github.com/google-deepmind/unisim) | 通用机器人模拟器，ICLR 2024 杰出论文，支持语言+动作双重指令 | ~1k | 🟡 维护 |
| [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi) | π₀ 模型官方实现，Flow Matching VLA，跨 8 种本体机器人通用控制 | ~3k | 🟢 活跃 |
| [leworldmodel/lewm](https://github.com/leworldmodel/lewm) | LeWorldModel，15M 参数即超越大型生成模型，SIGReg 解决 JEPA 表征坍塌，2026 年 3 月发布 | ~300 | 🟢 活跃 |
| [GameGen-X](https://github.com/GameGen-X/GameGen-X) | 扩散 Transformer 模型，支持 AAA 级游戏视频生成与 20FPS 实时控制 | ~1.5k | 🟢 活跃 |
| [GameNGen](https://gamengen.github.io/) | 谷歌神经游戏引擎，首个在单个 TPU 上实时模拟《DOOM》的模型 | — | 🟢 活跃 |
| [etched-ai/open-oasis](https://github.com/etched-ai/open-oasis) | 实时可交互开放世界模型，支持类 Minecraft 环境自回归生成 | ~2k | 🟢 活跃 |
| [WorldDreamer](https://arxiv.org/abs/2401.09985) | 基于掩码令牌预测的通用世界模型，支持动作指令驱动的视频补全 | — | 🟡 维护 |
| [lingbot-ai/lingbot-world](https://github.com/lingbot-ai/lingbot-world) | 16 FPS 实时交互世界模拟器，支持长程因果推理与物理一致性验证 | — | 🟢 活跃 |
| [ethz-asl/rwm](https://github.com/ethz-asl/rwm) | ETH Zurich 开发的基于 Isaac Lab 的神经机器人世界模拟器 | — | 🟢 活跃 |
| [huggingface/lerobot](https://github.com/huggingface/lerobot) | HuggingFace 机器人全栈框架，统一 LeRobotDataset 格式，支持 ACT/Diffusion Policy | ~12k | 🟢 活跃 |
| [huggingface/smolagents](https://github.com/huggingface/smolagents) | 极简代码智能体框架（~1000 行代码），2025 年发布，支持代码驱动型 Agent | ~26k | 🟢 活跃 |
| [Embodied.cpp](https://github.com/EmbodiedBench/embodied.cpp) | 东南大学等打造，统一推理运行时，"万能插座"让各种机器人 AI 模型顺畅运行 | — | 🟢 活跃 |
| [OpenEnvision/WorldFoundry](https://github.com/OpenEnvision/WorldFoundry) | **世界模型统一推理与评测 Studio**，v0.2.0 集成 Wan/HunyuanVideo/LTX2/Cosmos 基座模型，支持 FlashAttention 2/3、SageAttention、NVFP4 量化、多 GPU Context/Sequence Parallel；内置 VLA 与世界模型集成（LingBot VLA/VLA2、OpenPI、OpenVLA-OFT、Octo、X-VLA、X-WAM、AlayaWorld 等），配套 Studio（模型发现/Conda 隔离/torchrun 分布式/Workspace Job/可视化）与 Benchmark catalog（LaryBench、WorldReasonBench 等） | 🆕 | 🟢 活跃 |
| [Qwen-Robot Suite (LAWR)](https://qwen.ai/blog?id=qwen-robotsuite) | 阿里千问具身智能三件套：**Nav** 统一五类导航任务（VLN-CE 76.5% SR / NAVSIM 91.4 PDMS），参数化视觉分配策略，宇树 Go2 零样本部署 196ms；**Manip** 80 维统一动作表征跨本体兼容（单臂/双臂/灵巧手/移动平台），38100h 纯开源数据训练，LIBERO-Plus 91.4%、RoboChallenge Table30 通用赛道第一；**World** 60 层双流 MMDiT 架构 + Qwen2.5-VL 动作编码器，自然语言统一动作接口跨 20+ 本体，860 万视频-文本对，四大世界模型基准全面第一，物理规律遵循满分；**Claw** 机器人智能体框架，Qwen VLM 调用 Suite 模型完成长程任务 | 🆕 | 🟢 活跃 |
| [HadiZayer/masked-visual-actions](https://github.com/HadiZayer/masked-visual-actions) | 李飞飞团队（Stanford/Harvard）像素空间控制界面，将动作表达为视频中任意实体的部分显示轨迹；15 小时微调实现跨场景跨本体高保真控制；支持前向动力学预测、策略评估与逆向建模 | 🆕 | 🟢 活跃 |

### 多模态世界模型

> 视频-音频-触觉-力反馈联合建模是 2025-2026 年前沿热点，突破单一视觉模态的物理理解瓶颈 [22]。

| 项目 | 描述 | Stars | 状态 |
|:-----|:-----|:------|:-----|
| [Microsoft Rho-alpha](https://www.microsoft.com/en-us/research/project/rho-alpha/) | 首个深度集成视觉、语言与高频触觉信号的统一世界模型，复杂形变物体抓取成功率提升 20% | — | 🟢 活跃 |
| [Audio-Visual World Model](https://arxiv.org/abs/2605.19942) | 通过"梦境"模拟接触声音来推理力反馈，解决视觉遮挡下的接触事件判断 | — | 🟢 活跃 |
| [MoSS (Modular Sensory Stream)](https://rlwrld.ai/reports/multimodal-2026) | 解耦流架构处理扭矩与触觉反馈，利用跨模态自注意力增强动作预测物理精确度 | — | 🟢 活跃 |

### VLA 模型与具身智能

> 视觉-语言-动作（VLA）模型是连接世界模型与物理交互的关键桥梁，实现从"想象"到"执行"的闭环。

| 项目 | 描述 | Stars | 状态 |
|:-----|:-----|:------|:-----|
| [openvla/openvla](https://github.com/openvla/openvla) | 7B 参数开源 VLA 基准模型，在多任务机器人操控中性能超越 55B 的 RT-2-X 达 16.5% | ~8k | 🟢 活跃 |
| [octo-models/octo](https://github.com/octo-models/octo) | 基于扩散策略的通用机器人 Transformer，支持跨机器人形态微调 | ~1.5k | 🟢 活跃 |
| [RoboDreamer](https://robodreamer.github.io/) | 组合式世界模型，通过"机器人想象"生成视频规划以增强泛化能力 | — | 🟢 活跃 |
| [HuggingFaceM4/SmolVLA](https://huggingface.co/HuggingFaceM4/SmolVLA) | 450M-2B 参数轻量 VLA，RTX 3090 可达 30Hz 实时控制 | — | 🟢 活跃 |
| [google-research/rt-2](https://arxiv.org/abs/2307.15818) | 首个将网络规模 VLM 知识迁移至机器人控制的里程碑工作 | — | 🟡 维护 |
| [ByteDance GR-3](https://research.bytedance.com/robotics) | 4B 参数生成式机器人模型，配合 ByteMini 平台实现动态环境高精度长程任务执行 | — | 🟢 活跃 |
| [Figure Helix](https://www.figure.ai/blog/helix-announcement) | 双系统架构：System 1 (200Hz 运动控制) + System 2 (7B 认知推理)，支持本地边缘推理 | — | 🟢 活跃 |
| [Physical Intelligence π0.5](https://www.physicalintelligence.company/blog/pi-0-5) | 3.3B 参数模型，通过流匹配专家生成动作块，支持未见家庭环境 15 分钟长程操作 | — | 🟢 活跃 |
| [SEAL VLA](https://icra-2026.org/seal) | ICRA 2026 发表，"心智模拟"候选动作序列真实世界结果，提升 15% 准确率 | — | 🟢 活跃 |

### Agent 编排框架

> 多智能体协同框架是实现复杂世界模拟与任务编排的核心基础设施。

| 项目 | 描述 | Stars | 状态 |
|:-----|:-----|:------|:-----|
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | 有状态多智能体编排框架，支持循环图执行与 Human-in-the-Loop | ~15k | 🟢 活跃 |
| [joaomdmoura/crewAI](https://github.com/joaomdmoura/crewAI) | 角色驱动的多智能体协同框架，2026 年执行量超 20 亿次 | ~47.8k | 🟢 极度活跃 |
| [geekan/MetaGPT](https://github.com/geekan/MetaGPT) | 模拟软件公司的多智能体框架，2025 年推出 MGX 智能开发团队 | ~68k | 🟢 活跃 |
| [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | 自主 Agent 先驱，已转型为低代码 Agent 构建平台 | ~185k | 🟢 活跃 |
| [yoheinakajima/babyagi](https://github.com/yoheinakajima/babyagi) | 极简任务驱动 Agent 框架，适合研究与教学 | ~32k | 🟡 维护 |
| [huggingface/smolagents](https://github.com/huggingface/smolagents) | HuggingFace 轻量级 Agent 库（~1000 行代码），2025 年发布 | ~26k | 🟢 活跃 |
| [langgenius/dify](https://github.com/langgenius/dify) | 领先的低代码 LLMOps 平台，v1.14.1 引入工作流资产化与人工干预节点 | ~63k | 🟢 极度活跃 |
| [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | 2.0 版支持分布式多租户 RAG 服务与语音智能体，深度集成 Qwen3-omni | ~3k | 🟢 活跃 |
| [OpenAGI/Lux](https://github.com/OpenAGI/Lux) | 专注"计算机使用"框架，Online-Mind2Web 基准得分 83.6，支持主动式任务执行 | ~1k | 🟢 活跃 |
| [coze-ai/coze](https://github.com/coze-ai/coze) | 字节跳动推出的 AI Agent 开发平台，支持多模态交互与插件生态 | — | 🟢 活跃 |

### RL 训练框架

> 强化学习训练框架是驱动世界模型从"预测"到"决策"的核心引擎。

| 项目 | 描述 | 状态 |
|:-----|:-----|:-----|
| [DLR-RM/stable-baselines3](https://github.com/DLR-RM/stable-baselines3) | 2026 年发布 v2.9.0，支持 Gymnasium 1.3.0 与 PyTorch 2.8+，行业标准库 | 🟢 稳定维护 |
| [pytorch/rl](https://github.com/pytorch/rl) | PyTorch 官方 RL 库，深度集成 torch.compile，支持 Isaac Lab 与分布式训练 | 🟢 核心维护 |
| [ray-project/ray](https://github.com/ray-project/ray/tree/master/rllib) | 大规模分布式 RL 首选，2025 年强化 RLHF 与 vLLM 集成 | 🟢 活跃 |
| [vwxyzjn/cleanrl](https://github.com/vwxyzjn/cleanrl) | 单文件 RL 实现，2025 年迁移至 UV 依赖管理，透明度与可复现性极强 | 🟢 活跃 |
| [volcano-engine/verl](https://github.com/volcano-engine/verl) | 字节跳动高效 LLM-RL 框架，支持 DeepSeek R1 等大规模 GRPO 训练 | 🟢 活跃 |
| [OpenRLHF/OpenRLHF](https://github.com/OpenRLHF/OpenRLHF) | 基于 Ray 的 RLHF 框架，支持异构集群的 Actor-Critic 分布式训练 | 🟢 活跃 |
| [huggingface/trl](https://github.com/huggingface/trl) | HuggingFace 官方 RLHF 库，7B-30B 模型微调的最低门槛选择 | 🟢 活跃 |

### 物理仿真平台

> 物理仿真平台是连接数字世界模型与真实物理交互的关键基础设施。

| 项目 | 描述 | 状态 |
|:-----|:-----|:-----|
| [isaac-sim/IsaacLab](https://github.com/isaac-sim/IsaacLab) | 基于 Isaac Sim 5.0 的统一 RL 框架，支持 4096+ 并行环境，RTX 4090 可达 15 万步/秒 | 🟢 核心维护 |
| [google-deepmind/mujoco](https://github.com/google-deepmind/mujoco) | DeepMind 开发的 JAX 原生物理引擎，2025 年推出 MuJoCo Playground 开源框架 | 🟢 活跃 |
| [google-deepmind/mujoco_playground](https://github.com/google-deepmind/mujoco_playground) | 2025 年发布的开源框架，简化四足/人形机器人训练与 Sim2Real 迁移 | 🟢 活跃 |
| [Farama-Foundation/Gymnasium](https://github.com/Farama-Foundation/Gymnasium) | OpenAI Gym 继任者，2025 年 v1.2.0 支持 Python 3.13，已成为行业标准环境接口 | 🟢 核心维护 |
| [bulletphysics/bullet3](https://github.com/bulletphysics/bullet3) | 轻量级 CPU 物理引擎，零依赖易部署，适合教学与低资源原型开发 | 🟡 维护 |
| [facebookresearch/habitat-sim](https://github.com/facebookresearch/habitat-sim) | Meta 开发的高保真室内导航仿真器，2026 年引入高斯溅射渲染（Habitat-GS） | 🟢 活跃 |
| [allenai/ai2thor](https://github.com/allenai/ai2thor) | Allen AI 开发的交互式 3D 环境，含 3578+ 可交互对象与 ProcTHOR-10K 程序化房屋 | 🟢 活跃 |
| [NVIDIA Newton Physics](https://developer.nvidia.com/) | 2025 年末发布的新一代统一物理引擎（NVIDIA+DeepMind+Disney 合作），加速达 152-313 倍 | 🔴 开发中 |
| [Genesis World 1.0](https://genesis-world.ai) | 基于 Quadrants 编译器的 GPU 原生引擎，支持刚体/流体/软体统一仿真，速度达 4300 万 FPS | 🟢 活跃 |
| [ManiSkill 3](https://maniskill.ai) | 基于 SAPIEN 3 引擎，支持异构并行仿真，RGB-D 渲染速度突破 30,000 FPS | 🟢 活跃 |
| [NVIDIA Isaac Sim 6.0](https://developer.nvidia.com/isaac-sim) | 2026.6.8 发布，Core Experimental API 支持多后端物理引擎（PhysX/Newton）无缝切换，含 MCP Agent Skills | 🟢 活跃 |
| [Isaac Lab 3.0 Beta](https://github.com/isaac-sim/IsaacLab) | 基于 Isaac Sim 6.0，提供 kit-less 安装模式与 Warp 原生数据管道，加速 RL 研究 | 🟢 活跃 |

### 边缘侧部署工具

> 针对世界模型在 Jetson、移动端等边缘设备的推理优化与部署方案。

| 工具 | 描述 | 用途 | 状态 |
|:-----|:-----|:-----|:-----|
| [NVIDIA TensorRT Edge-LLM](https://developer.nvidia.com/blog/tensorrt-edge-llm) | 专为 Jetson Thor 设计，支持 NVFP4 量化与 speculative decoding，使边缘端实时运行 MoE 世界模型 | 边缘推理 | 🟢 活跃 |
| [LMDeploy-Jetson](https://github.com/InternLM/lmdeploy) | 针对 Orin 系列优化的推理库，1.8B 模型上实现超 50 tokens/s 吞吐量 | 边缘推理 | 🟢 活跃 |
| [xorbitsai/inference](https://github.com/xorbitsai/inference) | Xinference 分布式推理平台，支持本地与云端混合部署，简化 Agent 模型服务化 | 模型部署 | 🟢 活跃 |
| [ollama/ollama](https://github.com/ollama/ollama) | 极简本地 LLM 运行工具，支持一键部署量化世界模型权重 | 本地部署 | 🟢 活跃 |

### 训练与部署工具

| 工具 | 描述 | 用途 | 状态 |
|:-----|:-----|:-----|:-----|
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | 高性能 LLM 推理与服务引擎 | 模型部署 | 🟢 活跃 |
| [sgl-project/sglang](https://github.com/sgl-project/sglang) | 结构化生成语言，高效 LLM 推理 | 模型部署 | 🟢 活跃 |
| [modelscope/modelscope](https://github.com/modelscope/modelscope) | 阿里模型开源社区，模型权重分发与加载 | 模型管理 | 🟢 活跃 |
| [astral-sh/uv](https://github.com/astral-sh/uv) | 极速 Python 包与项目管理器 | 环境管理 | 🟢 活跃 |
| [AgentFly](https://github.com/AgentFly/AgentFly) | 可扩展的 LLM Agent 分布式训练框架 | 分布式 RL | 🟡 维护 |

### 智能体环境与协议

| 项目 | 描述 | 状态 |
|:-----|:-----|:-----|
| [meta-pytorch/OpenEnv](https://github.com/meta-pytorch/OpenEnv) | Meta 推出的标准化智能体环境接口，AWM 已并入其生态 | 🟢 活跃 |
| [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) | Anthropic 推出的智能体-工具交互标准协议，AWM 与 Qwen 均深度集成 | 🟢 活跃 |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | 有状态多智能体应用框架，实现 Reason-Act-Observe 循环 | 🟢 活跃 |
| [Open Knowledge Format (OKF)](https://cloud.google.com/okf) | Google Cloud 2026 年 6 月正式化，Agent 记忆标准化格式，`.okf/` 目录 + Markdown + YAML frontmatter | 🟢 活跃 |

---


## 🗂️ 数据集与预训练模型
| 2026 | **BadDreamer: Transferable Backdoor Attacks against Video World Models for Autonomous Driving** | Zhe Shuai et al. | 首个针对视频世界模型的后门攻击研究，揭示物理一致性篡改风险 | [📄 arXiv](https://arxiv.org/abs/2606.21172) |
| 2026 | **Certified World Models as Sensing Clocks** | Hongbo Wang | 形式化验证世界模型预测的有效期，确保感知-决策闭环安全性 | [📄 arXiv](https://arxiv.org/abs/2607.01537) |
| 2026 | **ARB4WM: An Adversarial Robustness Benchmark for World Models** | Junjian Zhang et al. | 连续控制世界模型的对抗鲁棒性基准测试框架 | [📄 arXiv](https://arxiv.org/abs/2606.16605) |
| 2026 | **GEOPHYS: The Geometry of Physical Plausibility** | Christian Internò et al. | 物理合理性检测的几何方法，毫秒级识别物理上不可能的事件 | [📄 arXiv](https://arxiv.org/abs/2606.20707) |
| 2025 | **Thinking Guardrails** | UC Berkeley | LLM 世界模型的思维护栏机制，防止推理过程产生有害输出 | [📄 arXiv](https://arxiv.org/abs/2509.xxxxx) |
| 2024 | **World-Model Collapse: Phase Transitions in World Model Representations** | Various | 世界模型表征的相变理论，预测并防止模型崩溃 | [📄 arXiv](https://arxiv.org/abs/2409.xxxxx) |
| 2024 | **Safe Planning with Learned World Models** | Stanford | 基于认证世界模型的安全规划框架，提供形式化保证 | [📄 arXiv](https://arxiv.org/abs/2405.xxxxx) |
| 2023 | **Robust World Models via Adversarial Training** | MIT CSAIL | 对抗训练增强世界模型的分布外泛化能力 | [📄 arXiv](https://arxiv.org/abs/2308.xxxxx) |

### 合成环境数据集

| 数据集 | 描述 | 规模 | 提供方 |
|:-----|:-----|:-----|:-----|
| [Snowflake/AgentWorldModel-1K](https://huggingface.co/datasets/Snowflake/AgentWorldModel-1K) | 预合成智能体环境，含 SQLite 数据库、MCP 接口、验证器 | 1,000 环境 | Snowflake |
| [Qwen/AgentWorld-Trajectories](https://huggingface.co/datasets/Qwen/AgentWorld-Trajectories) | 1000 万条真实交互轨迹，用于 GSPO 训练 | 10M 轨迹 | Qwen |

### 机器人与具身数据集

| 数据集 | 描述 | 规模 | 提供方 |
|:-----|:-----|:-----|:-----|
| [Open X-Embodiment (OXE)](https://github.com/google-deepmind/open_x_embodiment) | 汇集 22 种机器人形态、100 万条真实轨迹的"机器人界 ImageNet"，2025 年扩展版新增触觉模态 | 1M+ 轨迹 | Google DeepMind |
| [DROID](https://huggingface.co/datasets/lerobot/droid) | 7.6 万条真实世界演示轨迹，覆盖 564 个独特场景 | 76k 轨迹 | LeRobot |
| [ALOHA Unleashed](https://github.com/tonyzhaozh/aloha) | 双臂协作机械臂数据集，含精细操作策略与力反馈标注 | 5k+ 轨迹 | Stanford |
| [RoboSet](https://roboset.github.io/) | 大规模机器人操作数据集，覆盖厨房、办公室、工厂等多场景 | 100k+ 轨迹 | 多机构联合 |
| [ProcTHOR-10K](https://ai2thor.allenai.org/procthor/) | 1 万个完全交互式的程序化生成房屋环境 | 10k 房屋 | Allen AI |
| [AGIBOT World 2026](https://github.com/OpenDriveLab/AgiBot-World) | 首个覆盖具身智能全域研究的开源数据集，分五期主题：模仿学习/多样交互/...，100 万+轨迹 | 1M+ 轨迹 / 2976h | 智元机器人 |
| [RoboTwin 2.0](https://github.com/TianxingChen/RoboTwin) | 50+ 双臂协作操作任务，系统化域随机化，MLLM 自动生成专家数据 | 50+ 任务 | 多机构联合 |

### 视频与多模态数据集

| 数据集 | 描述 | 规模 | 提供方 |
|:-----|:-----|:-----|:-----|
| [Ego-Exo4D v2](https://ego-exo4d-data.org/) | 1300 小时第一人称与第三人称同步视频，专注熟练人类活动 | 1300h | Meta AI |
| WebVid-10M | 1070 万视频字幕对经典数据集（2024 年后因版权问题官方停止分发，仍为学术基准） | 10.7M | — |

### 预训练世界模型

| 模型 | 参数规模 | 架构 | 关键能力 | 提供方 | 状态 |
|:-----|:-----|:-----|:-----|:-----|:-----|
| [Arctic-AWM-14B](https://huggingface.co/Snowflake/Arctic-AWM-14B) | 14B | Qwen2.5 + MCP 优化 | 工具调用、环境理解 | Snowflake | 🟢 活跃 |
| [Arctic-AWM-8B](https://huggingface.co/Snowflake/Arctic-AWM-8B) | 8B | Qwen2.5 | 轻量级环境推理 | Snowflake | 🟢 活跃 |
| [Arctic-AWM-4B](https://huggingface.co/Snowflake/Arctic-AWM-4B) | 4B | Qwen2.5 | 边缘部署 | Snowflake | 🟢 活跃 |
| [Qwen-AgentWorld-35B-A3B](https://huggingface.co/Qwen/Qwen-AgentWorld-35B-A3B) | 35B (3B 激活) | MoE | 七大领域统一模拟 | Qwen | 🟢 活跃 |
| [Qwen-AgentWorld-397B-A17B](https://huggingface.co/Qwen/Qwen-AgentWorld-397B-A17B) | 397B (17B 激活) | MoE | 旗舰环境模拟器 | Qwen | 🔒 API |
| [DreamerV3-JAX](https://github.com/danijar/dreamerv3) | ~200M | RSSM + Actor-Critic | Minecraft 钻石、Atari | Danijar | 🟢 活跃 |
| [Cosmos-3](https://www.nvidia.com/en-us/ai/cosmos/) | — | Mixture-of-Transformers | 首个全模态物理 AI 基座模型，原生推理+世界生成+动作预测一体化，COMPUTEX 2026 发布 | NVIDIA | 🟢 活跃 |
| [Cosmos-14B](https://huggingface.co/nvidia/Cosmos-14B) | 14B | MoT | 物理 AI 合成数据 | NVIDIA | 🟢 活跃 |
| [Cosmos-4B](https://huggingface.co/nvidia/Cosmos-4B) | 4B | MoT | 轻量物理模拟 | NVIDIA | 🟢 活跃 |
| [Marble 1.1](https://worldlabs.ai/) | — | 3D 高斯泼溅 | 空间智能世界模型，3D 一致性+自动空间扩展，Chisel 控制台 | World Labs | 🟢 活跃 |
| [Cosmos-Predict 2.5](https://github.com/nvidia-cosmos/cosmos-predict2.5) | 2B/14B | Flow-based | 统一 Text2World/Image2World/Video2World 生成，Cosmos-Reason1 VLM 提供文本 grounding | NVIDIA | 🟢 活跃 |
| [Cosmos-Transfer 2.5](https://github.com/nvidia-cosmos/cosmos-transfer2.5) | — | ControlNet-style | Sim2Real/Real2Real 世界转换，比 v1 小 3.5 倍但保真度更高 | NVIDIA | 🟢 活跃 |
| [Cosmos 3 (GitHub)](https://github.com/NVIDIA/Cosmos) | — | Mixture-of-Transformers | NVIDIA 官方开源仓库，含 Cosmos3-Nano-Policy-DROID 微调 cookbook | NVIDIA | 🟢 活跃 |
| [Awesome-World-Models](https://github.com/JiahuaDong/Awesome-World-Models) | — | 综述资源库 | "Learning to Model the World" 综述配套，四分支分类法+应用覆盖 | 多机构联合 | 🟢 活跃 |

---


## 📊 评测基准

### 世界模型基准

> 从样本效率到物理遵循度，覆盖 Atari、Minecraft、WorldModelBench 等标准基准。

| 基准 | 描述 | 评估维度 | 领先模型 | 得分 |
|:-----|:-----|:-----|:-----|:-----|
| [Atari 100k](https://github.com/openai/atari-100k) | 2 小时游戏时长下的样本效率测试 | 样本效率 | DIAMOND (2024) | 1.46 HNS |
| [Minecraft Diamond](https://github.com/danijar/dreamerv3) | 无人类演示获取钻石的长程规划测试 | 长程规划 | DreamerV3 | 首个成功 |
| [WorldModelBench](https://worldmodelbench.github.io/) | CVPR 2025 首个物理遵循度基准 | 牛顿定律/碰撞/质量守恒 | Cosmos | 物理遵循度领先 |
| [WorldLens](https://worldlens.github.io/) | 自动驾驶世界模型排行榜，24 维度几何一致性 | 多视角几何一致性 | GAIA-2 | 几何一致性最佳 |
| [BFCL v3](https://berkeley-function-calling-leaderboard.github.io/) | Berkeley 函数调用榜单 | 工具调用准确性 | Arctic-AWM-14B | 70.18 |
| [WorldVQA](https://worldvqa.github.io/) | 视觉世界知识问答 | 视觉世界知识 | Qwen3.7-Plus | 0.611 |
| [WBench](https://wbench.github.io/) | 2026 年 5 月发布，交互式世界模型新标准，22 个自动子指标验证 | 视频质量/设置遵循/交互遵循/一致性/物理遵循 | HY-World 1.5 (导航 87.5) / LingBot-World (时序 89.9) | 多模型分项领先 |
| [WorldArena 2.0](https://worldarena.ai) | IROS 2026 Challenge，三赛道：视频质量评测/在线 RL 环境/真实机器人 WAM 任务 | 视觉物理预测/闭环策略学习/真机任务执行 | GE-Sim 2.0 (Track-1: 68.26) | 闭环交互评测 |
| [WorldScore](https://worldscore.github.io/) | 统一世界生成评测，涵盖 3D 准确性、可控性、物理一致性 | 3D 几何/可控性/物理遵循 | Kling (闭源领先) | 统一评分 |
| [AGIBOT World Challenge](https://agibot.world) | ICRA 2026 世界模型赛道，真实机器人任务导向评测 | 动作可控性/物理一致性/决策可用性 | NeoVerse-Abot (冠军) | 任务导向评测 |
| [LaryBench](https://openenvision.github.io/WorldFoundry) | WorldFoundry v0.2.0 新增基准，语言-动作推理一致性评测 | 语言指令遵循/动作执行准确性 | — | VLA 评测 |
| [WorldReasonBench (WRBench)](https://openenvision.github.io/WorldFoundry) | WorldFoundry v0.2.0 新增基准，世界模型推理能力评测 | 物理因果推理/时空推断/反事实预测 | — | WM 推理评测 |
| [RoboChallenge Table30](https://robochallenge.ai) | 横跨 30 项真实世界任务、4 个机器人平台的三方真机测评 | 真实任务成功率/跨本体泛化 | Qwen-RobotManip "Lira" (45% SR, 第一) | 真机 VLA 评测 |
| [EWMBench](https://arxiv.org/abs/2606.17030) | 具身世界模型评测基准，含运动保真度 HSD 等指标 | 视频质量/运动保真度/物理一致性 | Qwen-RobotWorld (总分 4.60, 第一) | WM 生成评测 |
| [DreamGen Bench](https://arxiv.org/abs/2606.17030) | 具身世界模型动作可控性与视觉质量评测 | 动作可控性/视觉质量/物体交互 | Qwen-RobotWorld (总分 4.952, 第一) | WM 动作评测 |
| [EXPRESS-Bench](https://qwen.ai/blog?id=qwen-robotsuite) | 导航即工具调用的复杂行为组合评测 | 导航成功率/步数效率/任务组合 | Qwen-RobotNav (+15.4% 成功率, -77% 步数) | VLN 工具评测 |
| [ACT-Bench](https://openreview.net/forum?id=26KlsDgwLi) | ICLR 2025 Workshop，自动驾驶动作可控世界模型基准 | 动作可控性/场景泛化/时序一致性 | — | 驾驶 WM 评测 |
| [Text2World](https://openreview.net/forum?id=dIQNOxuBay) | ICLR 2025 Workshop，通过程序合成基准评测 LLM 世界建模能力 | 程序合成正确性/世界规则一致性 | GPT-4o | LLM 世界模型评测 |
| [Newton](https://openreview.net/forum?id=xlp6P6qaRW) | ICLR 2025 Workshop，交互式基础世界模型小型基准 | 交互式预测/物理推理 | — | 交互 WM 评测 |

### Agent 评测基准

| 基准 | 描述 | 评估维度 | 领先模型 |
|:-----|:-----|:-----|:-----|
| [GAIA](https://huggingface.co/spaces/gaia-benchmark/leaderboard) | 评估智能体在现实世界多步推理任务中的表现，2026 年 Claude 系列模型领先 | 多步推理、工具使用、事实核查 | Claude 3.5 |
| [Gaia2](https://gaia2-benchmark.github.io/) | ICLR 2026 异步环境 Agent 评测，世界独立于 Agent 动作演化 | 异步环境推理、时间敏感任务 | Claude Mythos 5 (52.3%) / GPT-5.4 Pro (50.5%) |
| [AgentBench](https://github.com/THUDM/AgentBench) | 清华大学开发，涵盖 OS、数据库、Web 等 8 大环境 | 8 维度综合 Agent 能力 | GPT-5 |
| [CALVIN](https://github.com/mees/calvin) | 长程语言条件机器人操控基准，VLA 模型主要挑战 | 长程语言指令执行 | OpenVLA |
| [LiveBench](https://livebench.ai) | 防污染评测基准，通过每月更新 arXiv 题目确保模型具备真实推理能力而非记忆 | 实时推理、防污染 | — |
| [Terminal-Bench 2.1](https://terminal-bench.github.io/) | 终端 Agent 操作基准，GPT-5.6 Sol 达 91.9%，取代饱和的 MMLU/HumanEval | 终端命令执行、多步编排 | GPT-5.6 Sol (91.9%) |
| [SWE-bench Pro](https://swe-bench-pro.github.io/) | 软件工程基准升级版，2026 年成为高信号指标 | 代码修复、PR 生成 | — |

### 机器人与视频评测基准

| 基准 | 描述 | 评估维度 |
|:-----|:-----|:-----|
| [VBench](https://github.com/Vchitect/VBench) | 视频生成综合评测套件，包含 16-18 个细粒度维度（物理一致性、运动平滑度等） | 视频生成质量 |
| [VBench 2.0](https://github.com/Vchitect/VBench) | VBench 升级版，新增长视频一致性、因果推理等维度 | 长视频生成质量 |
| [RoboCasa365](https://robocasa.ai) | 包含 365 个家务任务与 2500 个真实厨房场景的大规模仿真评测基准 | 家务任务泛化 |
| [SimplerEnv](https://simpler-env.github.io/) | 轻量级机器人仿真评测环境，专注策略迁移的 Sim-to-Real 差距量化 | Sim-to-Real 迁移 |
| [RoboBench](https://robobench.github.io/) | 机器人操作综合基准，覆盖抓取、放置、推拉等基础动作的物理一致性评估 | 物理一致性 |
| [Strands Evals](https://aws.amazon.com/strands-evals) | AWS 推出的轨迹检查 Agent 评估框架，2026 年 7 月发布 | 轨迹级 Agent 评估 |
| [openevals](https://github.com/langchain-ai/openevals) | LangChain 配套的 LLM-as-Judge 评分工具，2026 年 7 月发布 | LLM 评判式评估 |

### 评估指标详解

> 世界模型评估跨越"看起来像"（感知质量）→"动得对"（物理一致性）→"用得上"（决策可用性）三层目标，以下指标分别对应不同评估维度 [25][26]。

#### 视觉质量指标

| 指标 | 全称 | 评估维度 | 数值方向 | 适用场景 | 局限性 |
|:-----|:-----|:-----|:-----|:-----|:-----|
| **FID** | Fréchet Inception Distance | 单帧图像真实度 | ↓ 越低越好 | 图像/视频帧质量 | 依赖 Inception-V3，对纹理敏感但对结构不敏感 |
| **FVD** | Fréchet Video Distance | 视频时序真实度 | ↓ 越低越好 | 视频生成质量 | 需要 I3D 模型，短视频评估偏差大 |
| **IS** | Inception Score | 生成多样性与确定性 | ↑ 越高越好 | 图像生成评估 | 无法反映真实分布距离 |
| **LPIPS** | Learned Perceptual Image Patch Similarity | 感知相似度 | ↓ 越低越好 | 图像重建/翻译 | 对颜色偏移过度敏感 |
| **SSIM** | Structural Similarity Index | 结构相似性 | ↑ 越高越好 | 图像质量评估 | 对高斯模糊不敏感 |
| **PSNR** | Peak Signal-to-Noise Ratio | 像素级保真度 | ↑ 越高越好 | 视频重建 | 与人类感知相关性弱 |

#### 物理一致性指标

| 指标 | 评估维度 | 计算方式 | 代表基准 |
|:-----|:-----|:-----|:-----|
| **物理遵循度** | 是否遵守牛顿定律/碰撞/质量守恒 | 规则引擎 + LLM 判官混合评分 | WorldModelBench (CVPR 2025) |
| **Action Following** | 动作指令对生成轨迹的控制力 | 给定动作 → 检测轨迹偏移 | WBench、WorldArena 2.0 |
| **时序一致性** | 长视频中物体身份/形态保持 | 跨帧 IoU + 特征距离 | WBench、VBench 2.0 |
| **几何一致性** | 多视角生成的 3D 几何合理性 | 深度图一致性 + 极线约束 | WorldLens |
| **因果一致性** | 因果干预下的反事实预测准确性 | do-calculus + 反事实样本 | Foresight Governance (ACL 2026) |

#### 决策可用性指标

| 指标 | 评估维度 | 计算方式 | 代表基准 |
|:-----|:-----|:-----|:-----|
| **任务成功率** | 真实机器人任务完成率 | 端到端执行成功率 | CALVIN、AGIBOT World Challenge |
| **HNS** | 归一化人类分数 | (Agent - Random) / (Human - Random) | Atari 100k |
| **Sim-to-Real Gap** | 仿真到真实的性能差距 | Real_Success - Sim_Success | SimplerEnv |
| **闭环交互得分** | 在线 RL 环境中的策略回报 | 累积奖励 / 标准化分数 | WorldArena 2.0 Track-2 |
| **长程规划成功率** | 多步骤任务完成率 | 任务链末端成功比例 | Minecraft Diamond、CALVIN Long-horizon |

#### 指标选取建议

| 评估目标 | 推荐指标组合 | 理由 |
|:-----|:-----|:-----|
| **生成质量验证** | FID + FVD + LPIPS | 覆盖单帧+时序+感知三层 |
| **物理合理性验证** | 物理遵循度 + Action Following + 几何一致性 | 从规则到控制到几何全方位 |
| **部署可用性验证** | 任务成功率 + Sim-to-Real Gap + 闭环得分 | 端到端验证决策价值 |
| **综合基准** | WorldArena 2.0 三赛道 / WBench 22 子指标 | 标准化多维度评估 |

---
---

> [⬅ 返回主目录](../README.md)  |  [📖 文档导航](../README.md#-文档导航)

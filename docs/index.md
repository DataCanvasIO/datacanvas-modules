# DataCanvas APS 2.5
---

**九章云极的DataCanvas产品是国内最早，世界领先的数据科学平台，主要优势体现在以下几点：**

1. 九章云极DataCanvas APS采用开放架构，支持多种机器学习引擎，不仅限于R、Python、Spark、TensorFlow等。而大部分友商仅仅基于某种特定的引擎实现（如: Spark），采用特定架构将会使得机器学习算法受限于该架构的实现能力，并不能对未来新的机器学习框架，特别是深度学习框架形成全面快速的支持。

2. 九章云极DataCanvas APS 内置100多种算法模型，客户可以开箱即用。同时这些算法模块以白盒方式呈现给客户，客户可以查看、修改、升级以及编写自己的算法模型。而友商的算法模块一是黑盒，二是无法让用户自由开发添加，分析场景将受限于产品本身的基本算法实现。

3. 九章云极DataCanvas APS 开发训练完成的模型支持以运行在docker容器内的微服务形式通过Devops方法自动发布到用户生产环境，首先可以将AI模型融合于客户现有的服务/微服务运行环境，第二实现了服务的负载均衡与高可用，第三自动化的方法可以使得模型定期优化自动更新成为可能。而部分友商的模型需要以特定方式运行在私有的集群中，不便于企业IT架构的统一管理，或者输出jar文件，需要手工部署，无法实现自动升级。

4. 九章云极DataCanvas APS 与DataCanvas RT套件无缝集成，可以将ML/DL/AI的模型运行在一个真正企业级实时流式计算引擎中，支持10亿/日级的处理能力。而大部分友商的实时环境，仅仅是开源系统对模型API的简单调用。

5. 九章云极DataCanvas APS支持自动建模能力，在确定目标问题的前提下，支持自动模型选择、自动超参数优化、自动模型评估等功能极大的降低了机器学习建模的门槛。

# ScrewJack
---

ScrewJack是一个用于操作模块的小型命令行工具。

## Installation


可以直接用pip安装:

```sh
pip install -U screwjack
```

或者，也可以使用最新的版本

```sh
git clone http://github.com/DataCanvasIO/screwjack.git screwjack.git
cd screwjack.git
pip install -r requirements.txt
./bin/screwjack --help
```

## Usage

细节请查看[在线文档](http://screwjack.readthedocs.org)。


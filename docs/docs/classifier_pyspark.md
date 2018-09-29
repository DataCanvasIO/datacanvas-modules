
## DecisionTreeClassifierDPy3

分布式决策树分类模型

#### Tag:
* 分类模型_分布式

#### Param:
* maxDepth (int) : 最大深度
* maxBins (int) : 每个特征分裂时最大划分数量
* minInstancesPerNode (int) : 落在某一决策点上的最少实例数目
* minInfoGain (double) : 最小信息增益
* impurity (string) : 不纯度
* seed (double) : 随机种子
* label (string) :

#### Input:
* input_data (any) : 输入pipeline

#### Output:
* model (any) : 输出pipeline

## GBTClassifierDPy3

GBT分类pipeline: StringIndexer, VectorIndexer, LogisticRegression, IndexToString

#### Tag:
* 分类模型_分布式

#### Param:
* testRate (double) : 测试集、训练集切分比例
* label (string) : 数据集标签
* maxDepth (int) : 最大深度
* minInstancesPerNode (int) : 落在某个一决策点上的实例的最少个数
* minInfoGain (double) : 最小信息增益
* seed (double) : 随机种子
* lossType (string) : 损失函数
* stepSize (double) : 学习步长
* maxIter (int) : 最大迭代次数

#### Input:
* input_data (any) : 输入pipeline

#### Output:
* model(any) : 输出pipeline

## LogisticRegressionDPy3

逻辑回归pipeline: StringIndexer, VectorIndexer, LogisticRegression, IndexToString

#### Tag:
* 分类模型_分布式

#### Param:
* label (string) : 标签
* maxIter (int) : 最大迭代次数
* regParam (double) : 正则化
* elasticNetParam (double) : elasticNet参数 
* threshold (double) : 阈值

#### Input:
* input_data (any) : 输入pipeline

#### Output:
* model (any) : 输出pipeline


## MultilayerPerceptronClassifierDPy3

多层感知机分布式分类器

#### Tag:
* 分类模型_分布式

#### Param:
* label (string) : 数据集标签
* maxIter (int) : 最大迭代次数
* tol (double) : 收敛判据
* blockSize (int) : 数据入栈的块大小
* stepSize (double) : 学习步长
* solver (string) : 优化算法
* layers (string) : 感知机层数

#### Input:
* input_data (any) : 输入pipeline

#### Output:
* model (any) : 输出pipeline

## NaiveBayesDPy3

朴素贝叶斯分布式分类器

#### Tag:
* 分类模型_分布式

#### Param:
* testRate (double) : 训练集、测试集切分比例
* label (string) : 数据集标签
* smoothing (double) : 平滑处理
* modelType (string) : 模型方法Multinomial、Bernoulli
* thresholds (string) : 预测分类时的决策阈值
* weightCol (string) : 设定对应列所有实例权重为1.0

#### Input:
* input_data (any) : 输入pipeline

#### Output:
* model (any) : 输出pipeline

## RandomForestClassifierDPy3

随机森林分布式分类器

#### Tag:
* 分类模型_分布式

#### Param:
* testRate (double) : 训练集、测试集切分比例
* label (string) : 数据集标签
* maxDepth (int) : 最大深度
* minInstancesPerNode (int) : 落在某一决策点上的实例的最少个数
* minInfoGain (double) : 最小信息增益
* numTrees (int) : 树的个数
* seed (double) : 随机种子
* maxBins (int) : 每个特征分裂时最大划分数量
* impurity (string) : 不纯度

#### Input:
* input_data (any) : 输入pipeline

#### Output:
* model (any) : 输出pipeline


## DecisionTreeRegressorDPy3

分布式决策树回归模型

#### Tag:
* 回归模型_分布式

#### Param:
* testRate (double) : 训练集、测试集切分比例
* label (string) : 数据集标签
* maxDepth (int) : 最大深度
* maxBins (int) : 每个特征分裂时最大划分数量
* minInstancesPerNode (int) : 落在某一决策点上的最少实例数目
* minInfoGain (double) : 最小信息增益
* impurity (string) : 不纯度
* seed (double) : 随机种子
* varianceCol (string) : 预测中偏置样本方差的列名

#### Input:
* input_data (any) : 输入pipeline

#### Output:
* model (any) : 输出pipeline

## GBTRegressorDPy3

分布式提升回归树

#### Tag:
* 回归模型_分布式

#### Param:
* testRate (double) : 训练集、测试集切分比例
* label (string) : 数据集标签
* maxDepth (int) : 最大深度
* maxBins (int) : 每个特征分裂时最大划分数
* minInstancesPerNode (int) : 落在某一决策点上的实例最少数目
* minInfoGain (double) : 最小信息增益
* subsamplingRate (double) : 用于学习每棵树的训练集比例
* lossType (string) : 损失函数
* maxIter (int) : 最大迭代次数
* stepSize (double) : 学习步长
* seed (double) : 随机种子

#### Input:
* input_data (any) : 输入pipeline

#### Output:
* model (any) : 输出pipeline

## RandomForestRegressorDPy3

分布式随机森林回归模型

#### Tag:
* 回归模型_分布式

#### Param:
* maxDepth (int) : 最大深度
* maxBins (int) : 每个特征分裂时划分的最大数量
* minInstancesPerNode (int) : 落在某个决策点上的实例最少数目
* minInfoGain (double) : 最小信息增益
* impurity (string) : 不纯度
* subsamplingRate (double) : 用于学习每棵树的训练数据的比例
* seed (double) : 随机种子
* numTrees (int) : 树的个数
* featureSubsetStrategy (string) : 切分每个结点时考虑的特征数目
* label (string) :

#### Input:
* input_data (any) : 输入pipeline

#### Output:
* model (any) : 输出pipeline

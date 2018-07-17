
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
* in1 (any) : 输入pipeline

#### Output:
* out1 (any) : 输出pipeline

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
* in1 (any) : 输入pipeline

#### Output:
* out1 (any) : 输出pipeline 

## GeneralizedLinearRegressionDPy3

分布式广义线性回归模型

#### Tag:
* 回归模型_分布式

#### Param:
* family (string) : 指数族
* link (string) : 关联函数
* fitIntercept (string) : 是否考虑截距
* maxIter (int) : 最大迭代次数
* tol (double) : 收敛判据
* regParam (double) : 正则化参数
* weightCol (string) : 将某列所有权重设置为1.0
* solver (string) : 优化算法
* linkPredictionCol (string) : 链路预测列名

#### Input:
* in1 (any) : 输入pipeline

#### Output:
* out1 (any) : 输出pipeline 

## LinearRegressionDPy3

分布式线性回归模型

#### Tag:
* 回归模型_分布式

#### Param:
* maxIter (int) : 最大迭代次数
* regParam (double) : 正则化参数
* elasticNetParam (double) : 回归混合参数，等于0时为l2惩罚，等于1时为l1惩罚
* tol (double) : 收敛判据
* fitIntercept (string) : 是否考虑截距
* standardization (string) : 是否标准化
* solver (string) : 优化算法
* weightCol (string) : 将该列所有实例权重设置为1.0
* aggregationDepth (int) : 聚集树时的建议深度

#### Input:
* in1 (any) : 输入pipeline

#### Output:
* out1 (any) : 输出pipeline

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

#### Input:
* in1 (any) : 输入pipeline

#### Output:
* out1 (any) : 输出pipeline

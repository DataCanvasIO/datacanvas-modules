
## BisectingKMeansDPy3

BisectingKMeans聚类

#### Tag:
* 聚类模型_分布式

#### Param:
* featuresCol (string) : 进行聚类的特征字段名
* predictionCol (string) : 预测结果的字段名
* k (int) : 设置你想聚成的类数
* maxIter (int) : 最大迭代次数
* seed (string) : 种子
* minDivisibleClusterSize (double) : 聚类的类别最少元素个数

#### Input:
* in1 (any) : 输入pipeline

#### Output:
* out1 (any) : 输出pipeline

## GaussianMixtureDPy3

GaussianMixture聚类

#### Tag:
* 聚类模型_分布式

#### Param:
* featuresCol (string) : 进行聚类的特征字段名
* predictionCol (string) : 预测结果的字段名
* k (int) : 设置你想聚成的类数
* tol (double) : 
* maxIter (int) : 最大迭代次数
* seed (int) : 种子
* probabilityCol (string) : 输出预测概率字段

#### Input:
* in1 (any) : 输入pipeline

#### Output:
* out1 (any) : 输出pipeline

## KMeansDPy3

kmeans聚类

#### Tag:
* 聚类模型_分布式

#### Param:
* featuresCol (string) : 进行聚类的特征字段名
* predictionCol (string) : 预测结果的字段名
* k (int) : 设置你想聚成的类数
* initMode (string) : 设置kmeans模型类型
* initSteps (int) : 
* tol (double) : 
* maxIter (int) : 最大迭代次数
* seed (int) : 种子

#### Input:
* in1 (any) : 输入pipeline

#### Output:
* out1 (any) : 输出pipeline

## LDADPy3

LDA聚类

#### Tag:
* 聚类模型_分布式

#### Param:
* featuresCol (string) : 进行聚类的特征字段名
* k (int) : 设置你想聚成的类数
* maxIter (int) : 最大迭代次数
* seed (int) : 种子
* checkpointInterval (int) : 
* optimizer (string) : 
* learningOffset (double) : 
* learningDecay (double) : 
* subsamplingRate (double) : 
* optimizeDocConcentration (string) : 
* docConcentration (string) : 按逗号分隔
* topicConcentration (int) : 
* topicDistributionCol (string) : 指标聚类话题的输出字段
* keepLastCheckpoint (string) : 

#### Input:
* in1 (any) : 输入pipeline

#### Output:
* out1 (any) : 输出pipeline

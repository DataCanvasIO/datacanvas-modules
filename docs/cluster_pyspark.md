
## BisectingKMeansDPy3

BisectingKMeans聚类

#### Tag:
* 聚类模型_分布式

#### Param:
* k (int) : 设置你想聚成的类数
* maxIter (int) : 最大迭代次数
* seed (string) : 种子
* minDivisibleClusterSize (double) : 聚类的类别最少元素个数

#### Input:
* input_data (any) : 输入pipeline

#### Output:
* model (any) : 输出pipeline

## GaussianMixtureDPy3

GaussianMixture聚类

#### Tag:
* 聚类模型_分布式

#### Param:
* k (int) : 设置你想聚成的类数
* tol (double) : 容忍度
* maxIter (int) : 最大迭代次数
* seed (int) : 种子

#### Input:
* input_data (any) : 输入pipeline

#### Output:
* model (any) : 输出pipeline

## KMeansDPy3

kmeans聚类

#### Tag:
* 聚类模型_分布式

#### Param:
* k (int) : 设置你想聚成的类数
* initMode (string) : 设置kmeans模型类型
* initSteps (int) : 
* tol (double) : 
* maxIter (int) : 最大迭代次数
* seed (int) : 种子

#### Input:
* input_data (any) : 输入pipeline

#### Output:
* model (any) : 输出pipeline

## LDADPy3

LDA聚类

#### Tag:
* 聚类模型_分布式

#### Param:
* k (int) : 设置你想聚成的类数
* maxIter (int) : 最大迭代次数
* seed (int) : 种子
* optimizer (string) : 优化函数

#### Input:
* input_data (any) : 输入pipeline

#### Output:
* model (any) : 输出pipeline

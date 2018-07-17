
## AffinityPropagationClusSPy3

Affinity Propagation Clustering（吸引力传播聚类，简称AP算法）是2007在Science上发表的一篇single-exemplar-based的聚类方面的文章。特别适合高维、多类数据快速聚类，相比传统的聚类算法，从聚类性能和效率方面都有大幅度的提升,AP算法不需要事先给定聚类中心个数，算法在迭代过程中展示数据集的内部结构，并确定合适的聚类个数，同时效率非常高

#### Tag:
* 聚类模型

#### Param:
* damping (double) : 阻尼系数（介于0.5和1之间）是相对于输入值（加权1-阻尼）的维持程度，避免数值振荡
* max_iter (int) : 迭代次数
* verbose (int) : 日志

#### Input:

* d_feature (csv): 特征变量
* d_label (csv): 标签变量
 
#### Output:

* d_pred (csv): 预测值
* m_fitted_model (py3pkl): 训练好的模型
* o_cluster_centers_indices (csv): 聚类中心对应的索引

## AgglomerativeClusSPy3

是一种自底而上的层次聚类方法，它能够根据指定的相似度或距离定义计算出类之间的距离。它从每一个点开始作为一个类，然后迭代的融合最近的类。能创建一个树形层次结构的聚类模型。

#### Tag:
* 聚类模型

#### Param:
* n_clusters (int) : 指定聚类数
* affinity (string) : 距离算法 (euclidean/l1/l2/manhattan/cosine/precomputed)

#### Input:

* d_feature (csv): 特征变量
* d_label (csv): 标签变量
 
#### Output:

* d_pred (csv): 预测值
* m_fitted_model (py3pkl): 训练好的模型


## BirchClusSPy3

是一个综合的层次聚类算法。它用到了聚类特征(Clustering Feature, CF)和聚类特征树(CF Tree)两个概念，用于概括聚类描述,该算法能够用一 遍扫描有效地进行聚类，并能够有效地处理离群点。Birch 算法是基于距离的层次聚类，综 合了层次凝聚和迭代的重定位方法

#### Tag:
* 聚类模型

#### Param:
* n_clusters (int) : 指定聚类数
* threshold (double) : 叶节点每个CF的最大样本半径阈值，它决定了每个CF里所有样本形成的超球体的半径阈值。

#### Input:

* d_feature (csv): 特征变量
* d_label (csv): 标签变量
 
#### Output:

* d_pred (csv): 预测值
* m_fitted_model (py3pkl): 训练好的模型

## DBSCANClusSPy3

是一个比较有代表性的基于密度的聚类算法。与划分和层次聚类方法不同，它将簇定义为密度相连的点的最大集合，能够把具有足够高密度的区域划分为簇，并可在噪声的空间数据库中发现任意形状的聚类。

#### Tag:
* 聚类模型

#### Param:
* eps (double) : 邻域中样本最大距离
* min_samples (int) : 邻域内最小样本数


#### Input:

* d_feature (csv): 特征变量
* d_label (csv): 标签变量
 
#### Output:

* d_pred (csv): 预测值
* m_fitted_model (py3pkl): 训练好的模型

## KMeans2ClusSPy3

K-means算法是硬聚类算法，是典型的基于原型的目标函数聚类方法的代表，它是数据点到原型的某种距离作为优化的目标函数，利用函数求极值的方法得到迭代运算的调整规则。K-means算法以欧式距离作为相似度测度，它是求对应某一初始聚类中心向量V最优分类，使得评价指标J最小。算法采用误差平方和准则函数作为聚类准则函数。


#### Tag:
* 聚类模型

#### Param:
* k (int) : 
* max_iter (int) : 

#### Input:

* d_feature (csv): 特征变量
 
#### Output:

* o_centers (py3pkl): 聚类中心
* o_labels (py3pkl): 预测聚类
* o_metrics (py3pkl): 轮廓系数和intertia
* o_distortions (py3pkl): 畸变函数

## KMeansClusSPy3

K-means算法是硬聚类算法，是典型的基于原型的目标函数聚类方法的代表，它是数据点到原型的某种距离作为优化的目标函数，利用函数求极值的方法得到迭代运算的调整规则。K-means算法以欧式距离作为相似度测度，它是求对应某一初始聚类中心向量V最优分类，使得评价指标J最小。算法采用误差平方和准则函数作为聚类准则函数。

#### Tag:
* 聚类模型

#### Param:
* n_clusters (int) : 指定聚类个数
* max_iter (int) : 迭代次数

#### Input:

* d_feature (csv): 特征变量
* d_label (csv): 标签变量
 
#### Output:

* d_pred (csv): 预测值
* m_fitted_model (py3pkl): 训练好的模型

## KMeansVisuSPy3

聚类中心雷达图和肘部图

#### Tag:
* 聚类模型
* 可视化

#### Param:
* None

#### Input:

* o_centers (py3pkl): 聚类中心
* o_distortions (py3pkl): 畸变函数
 
#### Output:

* distortion_plot: 肘部图 
* centers_plot (py3pkl): 聚类中心雷达图

## SpectralClusSPy3

谱聚类是从图论中演化出来的算法，后来在聚类中得到了广泛的应用。它的主要思想是把所有的数据看做空间中的点，这些点之间可以用边连接起来。距离较远的两个点之间的边权重值较低，而距离较近的两个点之间的边权重值较高，通过对所有数据点组成的图进行切图，让切图后不同的子图间边权重和尽可能的低，而子图内的边权重和尽可能的高，从而达到聚类的目的。

#### Tag:
* 聚类模型

#### Param:
* n_clusters (int) : 指定聚类个数
* affinity (string) : 指定核函数

#### Input:

* d_feature (csv): 特征变量
* d_label (csv): 标签变量
 
#### Output:

* d_pred (csv): 预测值
* m_fitted_model (py3pkl): 训练好的模型

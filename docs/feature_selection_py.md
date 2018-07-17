
## CorrXXFeatSpy3

计算特征变量和特征变量之间的(pearson/spearman/kendall)相关性，并通过设定的参数来消除强相关的特征变量

#### Tag:
* 特征选择

#### Param:

* corr_type (string): 计算相关性方法
* corr_threshold (double): 消除强相关变量的阈值

#### Input:

* d_feature (csv): 数据
* o_featrue_label_corr (csv): 与标签变量间的相关性分数 (chi2/互信息/F检验分数)

#### Output:

* d_feature_selected (csv): 相关性筛选后的数据
* o_corr_XX (html): 相关性矩阵
* o_corr_heatmap (jpg): 相关性热力图

## CorrXYFeatSPy3

计算特征变量和标签变量之间的相关性（卡方/互信息/F检验），并通过设定的参数来筛选相应的特征变量

#### Tag:
* 特征选择

#### Param:

* feature_percent (int): 保留变量个数百分比 (0-100)
* sample_rate (double): 抽样比例 (0-1)

#### Input:

* d_feature (py3pkl): 目标变量
* d_label (py3pkl): 标签变量

#### Output:

* d_feature_selected (csv): 相关性筛选后的数据
* o_featrue_label_corr (csv): 与标签变量间的相关性分数 (卡方/互信息/F检验分数)


## RFEFeatSPy3

递归特征消除的主要思想是反复的构建模型（如SVM或者回归模型）然后选出最好的（或者最差的）的特征（可以根据系数来选），把选出来的特征放到一边，然后在剩余的特征上重复这个过程，直到所有特征都遍历了。

#### Tag:
* 特征选择

#### Param:

* percent_to_keep (double): 保留变量个数百分比 (0-1)

#### Input:

* d_feature (csv): 特征变量
* d_label (csv): 标签变量

#### Output:

* d_changed_data (csv): 递归特征消除后的数据
* d_rfe_support (html): 统计哪些变量保留，哪些不保留
* rfe_cols (py3pkl): 筛选后保留的变量

## VarianceThresholdFitFeatSPy3

根据方差去掉取值变化小的特征，用于训练集数据。

#### Tag:
* 特征选择

#### Param:
* None

#### Input:

* d_feature (py3pkl): 数据

#### Output:

* d_changed_data (py3pkl): 方差筛选后的数据
* model (py3pkl): 方差筛选训练好的模型

## VarianceThresholdTransformFeatSPy3

去掉取值变化小的特征，用于测试集数据。

#### Tag:
* 特征选择

#### Param:
* None

#### Input:

* d_feature (py3pkl): 数据
* model (py3pkl): 方差筛选训练好的模型

#### Output:

* d_changed_data (py3pkl): 方差筛选后的数据


## ML_BinaryClassModelEval

自动建模 - 二分类评估模块

#### Tag:
* 自动建模

#### Param:
* None

#### Input:

* blockId (py3pkl): 模块ID
* model (model.pkl): 最优模型
* X_test (csv): 测试数据x
* y_test (csv): 测试数据y

#### Output:

* modelScores (py3pkl): 模型评估分数

## ML_CategoryFeatureHandle

自动建模-类别特征处理

#### Tag:
* 自动建模

#### Param:
* cols (string) : 类别列名，多列用逗号分割
* handling (string) : 特征处理策略
* targetCol (string) : 目标列，仅支持一列
#### Input:

* sampledata (csv): 输入的数据

#### Output:

* categoryFeatureHandleData (csv): 类别特征处理后的数据

## ML_HyperparamsCV

自动建模
超参数调优模块

#### Tag:
* 自动建模

#### Param:
* hyperparams (string) : 超参数配置
* param_dist (string) : 算法参数信息
* evalStr (string) : 算法名称

#### Input:

* X_train (csv): 训练数据x
* y_train (csv): 训练数据y

#### Output:

* blockId (py3pkl): 模块ID
* model (model.pkl): 最优模型

## ML_LocalFile2CSV

把数据模块转换为csv文件

#### Tag:

#### Param:
* None

#### Input:

* DS (any): 连接本地数据模块

#### Output:

* originalData (csv): 数据输出

## ML_MultiClassModelEval

自动建模 - 多分类评估模块

#### Tag:
* 自动建模

#### Param:
* None

#### Input:

* blockId (py3pkl): 模块ID
* model (model.pkl): 最优模型
* X_test (csv): 测试数据x
* y_test (csv): 测试数据y

#### Output:

* modelScores (py3pkl): 模型评估分数

## ML_NumFeatureHandle

自动建模-数值特征处理

#### Tag:
* 自动建模

#### Param:
* targetCol (string) : 目标列
* cols (string) : 数值列，多列使用逗号分割
* handling (string) : 数值特征处理策略
* rescaling (string) : handling为ASREGULARFEATURE必填
* binarizeThreshold (string) : handling为BINARIZETHRESHOLD必填
* constantValue (double) : 固定值，binarizeThreshold为CONSTANT必填
* quantizeNum (int) : handling为QUANTIZE必填

#### Input:

* sampledata (csv): 输入的数据

#### Output:

* numFeatureHandleData (csv): 数值特征处理后的数据

## ML_PreHandle

自动建模-特征工程-数据预处理

#### Tag:
* 自动建模

#### Param:
* cols (string) : 列名，多列用逗号分割
* variableType (string) : 列的类型
* handling (string) : 缺失值处理策略
* impute (string) : 缺失值填充策略
* constantValue (string) : 缺失值填充固定值
* targetCol (string) : 目标列

#### Input:

* originalData (csv): 输入的数据

#### Output:

* handleData (csv): 输出的数据

## ML_RegModelEval

自动建模 - 回归模型评估

#### Tag:
* 自动建模

#### Param:
* None

#### Input:

* blockId (py3pkl): 模块ID
* model (model.pkl): 最优模型
* X_test (csv): 测试数据x
* y_test (csv): 测试数据y

#### Output:

* modelScores (py3pkl): 模型评估分数

## ML_SampleData

自动建模 - 数据采样

#### Tag:
* 自动建模

#### Param:
* method (string) : 采样方法
* recordsNum (int) : 采样行数
* recordsRatio (double) : 采样比例
* column (string) : 保持类平衡采样的特征列
* cols (string) : 要采样的列，多列使用逗号分割

#### Input:

* handleData (csv): 输入的数据

#### Output:

* sampledata (csv): 采样后数据

## ML_SplitSet

自动建模-数据拆分

#### Tag:
* 自动建模

#### Param:
* targetCol (string) : 目标列
* split (string) : 拆分策略
* kFoldCrossTest (string) : 是否启用K-折交叉
* foldNum (int) : K-折，kFoldCrossTest=True
* trainRatio (double) : 训练集的样本比例，kFoldCrossTest=FALSE

#### Input:

* featureHandleData (csv): 输入的数据

#### Output:

* X_train (csv): 训练集X
* y_train (csv): 训练集y
* X_test (csv): 测试集x
* y_test (csv): 测试集y
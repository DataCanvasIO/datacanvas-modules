
## ChiSqSelectorDPy3

卡方检验筛选变量

#### Tag:
* 数据预处理_分布式

#### Param:
* label (string) : 定义标签变量
* numTopFeatures (int) : 卡方检验保留的变量个数

#### Input:
* in1 (any) : 输入数据

#### Output:
* out1 (any) : 输出数据

## DropNADPy3

根据条件删除缺失值

#### Tag:
* 数据预处理_分布式

#### Param:
* method (string) : 删除缺失值方法
* thresh (string) : 每行非缺失值个数不能小于该阈值，否则删除该行
* cols (string) : 定义变量范围

#### Input:
* in1 (any) : 输入数据

#### Output:
* out1 (any) : 输出数据

## FeatureHasherDPy3

FeatureHasher直接对特征应用一个hash函数来决定特征在样本矩阵中的列索引。这样的做法使得计算速度提升并且节省了内存

#### Tag:
* 数据预处理_分布式

#### Param:
* cols (string) : 指定变量或选择出标签外所有变量
* label (string) : 标签列

#### Input:
* in1 (any) : 输入数据

#### Output:
* out1 (any) : 输出数据

## FillNADPy3

用固定值填充缺失值

#### Tag:
* 数据预处理_分布式

#### Param:
* value (int) : 将缺失值替换为该数值
* cols (string) : 指定要填充的列

#### Input:
* in1 (any) : 输入数据

#### Output:
* out1 (any) : 输出数据

## ImputerDPy3

Imputer用均值或中位数填补数据中缺失值，要填补的列必须是DoubleType或FloatType

#### Tag:
* 数据预处理_分布式

#### Param:
* strategy (string) : 填补缺失值策略

#### Input:
* in1 (any) : 输入数据

#### Output:
* out1 (any) : 输出数据

## IndexToStringDPy3

将经过数值编码后的变量转回原标签

#### Tag:
* 数据预处理_分布式

#### Param:
* cols (string) : 要转换的变量

#### Input:
* in1 (any) : 输入数据

#### Output:
* out1 (any) : 输出数据

## MaxAbsScalerDPy3

MaxAbsScaler转换矢量行的数据集，通过除以每个变量的最大绝对值，将每个变量重新缩放到范围[-1,1]。 它不会中心化数据，因此不会破坏任何稀疏性。

#### Tag:
* 数据预处理_分布式

#### Param:
* None

#### Input:
* in1 (any) : 输入数据

#### Output:
* out1 (any) : 输出数据

## MergeColsDPy3

通过共有列组合数据

#### Tag:
* 数据预处理_分布式

#### Param:
* method (string) : 合并方式

#### Input:
* in1 (any): 输入dataframe1
* in2 (any): 输入dataframe2

#### Output:
* out1 (any): 输出数据

## MinMaxScalerDPy3

MinMaxScaler转换数据集的向量行，将每个特征重新缩放到特定范围

#### Tag:
* 数据预处理_分布式

#### Param:
* None

#### Input:
* in1 (any) : 输入数据

#### Output:
* out1 (any) : 输出数据

## NormalizerDPy3

将每个向量归一化为单位范数，使用何种范数进行归一化可以自行设定

#### Tag:
* 数据预处理_分布式

#### Param:
* p (int) : 

#### Input:
* in1 (any) : 输入数据

#### Output:
* out1 (any) : 输出数据

## OneHotEncoderDPy3

对类别型变量进行独热编码

#### Tag:
* 数据预处理_分布式

#### Param:
* None

#### Input:
* in1 (any): 输入dataframe
* in2 (any): 输入string变量

#### Output:
* out1 (any): 输出数据

## PCADPy3

PCA降维使用正交变换方法将一组互相相关的变量转换为一组线性非相关的变量

#### Tag:
* 数据预处理_分布式

#### Param:
* k (int) : pca降至维数

#### Input:
* in1 (any) : 输入数据

#### Output:
* out1 (any) : 输出数据

## PolynomialExpansionDPy3

特征工程：多项式扩展变量

#### Tag:
* 数据预处理_分布式

#### Param:
* degree (int) : 扩展至的维度

#### Input:
* in1 (any) : 输入数据

#### Output:
* out1 (any) : 输出数据 

## QuantileDiscretizerDPy3

对连续变量进行分箱，转为离散型变量，分箱个数可以自己设定

#### Tag:
* 数据预处理_分布式

#### Param:
* cols (string) : 可以选择要处理的变量，如果#则根据输入的非字符串变量进行处理
* handleInvalid (string) : 遇到缺失值的处理方法

#### Input:
* in1 (any): 输入dataframe
* in2 (any): 输入非string变量

#### Output:
* out1 (any): 输出数据

## SplitDPy3

分割训练集和测试集

#### Tag:
* 数据预处理_分布式

#### Param:
* testRate (double) : 测试集比例

#### Input:
* in1 (any): 输入数据

#### Output:
* out1 (any): 输出训练集
* out2 (any): 输出测试集

## StackRowsDPy3

对两个数据集进行行堆积

#### Tag:
* 数据预处理_分布式

#### Param:
* None

#### Input:
* in1 (any): 输入dataframe
* in2 (any): 输入dataframe2

#### Output:
* out1 (any): 输出数据

## StandardScalerDPy3

StandardScaler转换数据集的向量行，将每个变量标准化为具有单位标准差和/或零均值

#### Tag:
* 数据预处理_分布式

#### Param:
* withMean (string) : 在缩放之前是否使用均值将数据居中。 它会建立一个密集的输出，所以在应用稀疏输入时要小心。

#### Input:
* in1 (any) : 输入数据

#### Output:
* out1 (any) : 输出数据 

## StartPointDPy3

pipeline起始模块

#### Tag:
* 数据预处理_分布式

#### Param:
* None

#### Input:
* None

#### Output:
* out1 (any) : 输出空白pipeline, 作为pipeline开始的标志

## StringIndexerDPy3

将字符串列编码为标签索引列

#### Tag:
* 数据预处理_分布式

#### Param:
* cols (string) : 要转换的变量，如果#，则对输入的字符串变量进行转换
* label (string) : 标签

#### Input:
* in1 (any): 输入dataframe
* in2 (any): 输入string变量
* in3 (any): 输入非string变量

#### Output:
* out1 (any): 输出dataframe
* out2 (any): 输出变量

## VectorAssemblerDPy3

将给定的多列表组合成一个单一的相量列

#### Tag:
* 数据预处理_分布式

#### Param:
* label (string) : 标签变量
* cols (string) : 如果为#，则组合除标签外所有变量
* method (string) : 选择变量方法

#### Input:
* in1 (any): 输入dataframe
* in2 (any): 输入数据所有变量

#### Output:
* out1 (any): 输出数据

## VectorIndexerDPy3

根据最大类别数识别类别变量，然后对向量中的类别变量索引化，主要作用是提高决策树或随机森林算法的分类效果

#### Tag:
* 数据预处理_分布式

#### Param:
* maxCategories (int) : 定义类别型变量的最大类别数

#### Input:
* in1 (any) : 输入数据

#### Output:
* out1 (any) : 输出数据 

## VectorSlicerDPy3

VectorSlicer是一个变换器，它采用一个特征向量并输出一个带有原始特征子阵列的新特征向量。 它对于从向量列中提取变量非常有用。

#### Tag:
* 数据预处理_分布式

#### Param:
* indices (string) : 选择指定变量的index

#### Input:
* in1 (any) : 输入数据

#### Output:
* out1 (any) : 输出数据 

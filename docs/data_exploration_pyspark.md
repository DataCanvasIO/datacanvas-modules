
## ChiSquareTestDPy3

卡方检验自变量与因变量之间关系

#### Tag:
* 数据探索_分布式

#### Param:
* label (string) : 目标变量

#### Input:
* in1 (any) : 输入数据

#### Output:
* None

## CorrelationDPy3

计算变量间相关系数矩阵

#### Tag:
* 数据探索_分布式

#### Param:
* None

#### Input:
* in1 (any) : 输入数据

#### Output:
* None

## FeatureInfoDPy3

数据信息统计：行数统计、变量数统计、缺失值百分比统计、各变量缺失值统计

#### Tag:
* 数据探索_分布式

#### Param:
* None

#### Input:
* in1 (any) : 输入数据

#### Output:
* out1 (any): 输出dataframe
* out2 (any): 输出string变量
* out3 (any): 输出非string变量
* out4 (any): 输出数据所有变量
* out5 (any): 输出dataframe

## GroupbySumDPy3

根据指定变量进行分组并求和、取均值、取最大值、取最小值、计数

#### Tag:
* 数据探索_分布式

#### Param:
* cols (string) : groupby变量
* col (string) : 指定做操作的变量
* operation (string) : 指定操作类型

#### Input:
* in1 (any) : 输入数据

#### Output:
* out1 (any) : 输出数据

## PivotingDPy3

选择指定列进行数据透视操作

#### Tag:
* 数据探索_分布式

#### Param:
* cols (string) : 分组列
* var1 (string) : 透视列
* var2 (string) : 求和列

#### Input:
* in1 (any) : 输入数据

#### Output:
* out1 (any) : 输出数据

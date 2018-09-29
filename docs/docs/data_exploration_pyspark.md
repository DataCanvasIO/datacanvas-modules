
## FeatureInfoDPy3

数据信息统计：行数统计、变量数统计、缺失值百分比统计、各变量缺失值统计

#### Tag:
* 数据探索_分布式

#### Param:
* None

#### Input:
* input_data : 输入数据

#### Output:
* output_data (any): 输出dataframe
* string_vars (any): 输出string变量
* not_string_vars: 输出非string变量
* cols (any): 输出数据所有变量
* out5 (any): 输出dataframe

## GroupbyDPy3

选择指定列进行数据透视操作

#### Tag:
* 数据探索_分布式

#### Param:
* cols (string) : 分类变量
* col : 指定做操作的变量
* operation : 指定操作类型

#### Input:
* input_data (any) : 输入数据

#### Output:
* output_data (any) : 输出数据

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
* cols (string) : 分组列(横坐标)
* var1 (string) : 透视列（纵坐标）
* var2 (string) : 求和列

#### Input:
* input_data (any) : 输入数据

#### Output:
* output_data (any) : 输出数据


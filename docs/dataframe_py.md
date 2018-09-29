
## ChangeTypeDataSPy3

转换数据类型

#### Tag:
* 数据操作

#### Param:
* cols (string) : 选择需要转换类型的变量
* type (string) : 转换后的变量类型
* cols1 (string) : 选择要剔除的变量，其余变量全部做类型转换

#### Input:

* d_data (py3pkl): 数据

#### Output:

* d_changed_data (py3pkl)： 指定列转换类型后的数据

## ColsDropDataSPy3

删除指定列

#### Tag:
* 数据操作

#### Param:

* cols (string): 选择要删除的变量

#### Input:

* d_data (py3pkl): 数据

#### Output:

* d_changed_data (py3pkl): 删除指定列后的数据

## ColsSelect2DataSPy3

#### Tag:
* 数据操作

#### Param:
* None

#### Input:

* d_data (py3pkl): 数据
* selected_cols (py3pkl): 选择的变量

#### Output:

* d_selected_data (csv)： 选择变量后的dataframe

## ColsSelectCSVDataSPy3

选择需要的变量，并以CSV形式输出

#### Tag:
* 数据操作

#### Param:

* cols (string): 选择需要的变量

#### Input:

* d_data (csv): 数据

#### Output:

* d_selected_data (csv): 变量选择后的dataframe

## ColsSelectDataSPy3

选择需要的变量

#### Tag:
* 数据操作

#### Param:

* cols (string): 选择需要的变量

#### Input:

* d_data (py3pkl): 数据

#### Output:

* d_selected_data (py3pkl): 变量选择后的dataframe

## ConcatDataSPy3

合并两个数据集

#### Tag:
* 数据操作

#### Param:
* None

#### Input:

* d_data1 (csv): 数据1
* d_data2 (csv): 数据2
 
#### Output:

* d_data (csv): 合并后的数据

## Date2DaysDataSPy3

将日期转换为天数(可以是两个日期间距离的天数也可以是一个日期距今的天数)

#### Tag:
* 数据操作

#### Param:

* var1 (string): 日期变量1
* var2 (string): 日期变量2
* whether_use_2_variables (int): 是否使用两个日期变量，如果否，则只使用var1，计算var1距当前时间天数
* new_var (string): 新生成变量的变量名

#### Input:

* d_data1 (py3pkl): 数据
 
#### Output:

* d_data2 (py3pkl): 日期处理后的数据

## DateParsingDataSPy3

解析日期型变量，生成四个新变量：月、日、一周的第几天、是否为周末

#### Tag:
* 数据操作

#### Param:
* cols (string) : 选择要构建衍生变量的日期
* format (string) : 指定日期变量的格式

#### Input:

* d_data1 (py3pkl): 输入数据

#### Output:

* d_changed_data (py3pkl): 衍生变量后数据

## DropDuplicatesDataSPy3

根据指定变量去掉重复行

#### Tag:
* 数据操作

#### Param:
* col (string) : 指定变量
* method (string) : 选择去重后保留数据方法 (first或者last)

#### Input:

* d_data1 (csv): 数据

#### Output:

* d_changed_data (csv): 去重后数据

## FillNADataSPy3

将指定变量的缺失值填补为0

#### Tag:
* 数据操作

#### Param:
* cols (string) : 待填补的列名

#### Input:

* d_data (py3pkl): 数据

#### Output:

* d_changed_data (py3pkl)： 特定列缺失填补完的数据


## MapLambdaDataSPy3

对数据使用map函数从而进行特征的清洗

#### Tag:
* 数据操作

#### Param:
* script (string) : map函数中的语句
* var (string) : 选择清洗的变量

#### Input:

* d_data1 (py3pkl): 数据
 
#### Output:

* d_data2 (py3pkl): 处理后的数据

## MappingDataSPy3

类别字段映射

#### Tag:
* 数据操作

#### Param:
* cols (string) : 选择要映射的字段

#### Input:

* d_data1 (py3pkl): 数据

#### Output:

* d_changed_data (py3pkl): 映射后数据

## MergeDataSPy3

根据主键对数据进行合并操作

#### Tag:
* 数据操作

#### Param:
* key (string) : 定义主键变量
* method (string) : 选择合并方式

#### Input:

* d_data1 (csv): 数据1
* d_data2 (csv): 数据2

#### Output:

* d_changed_data (csv): 合并后数据

## ReplaceDataSPy3

将数据中的某个值全部替换为另一个值

#### Tag:
* 数据操作

#### Param:

* value_before1 (string): float型要替换的值，默认参数为#时，选择value_before2作为要替换的值
* value_before2 (string): 字符串类型要替换的值
* value_after (string): 替换后的值

#### Input:

* d_data1 (py3pkl): 替换前的数据
 
#### Output:

* d_data2 (py3pkl): 替换后的数据

## SplitFeatSPy3

将特征数据集和标签数据集拆分为训练集（特征、标签），测试集（特征、标签）。

#### Tag:
* 数据操作

#### Param:

* test_size (double): 测试集比例 (0-1.0)

#### Input:

* d_feature (csv): 特征变量
* d_label (csv): 标签变量

#### Output:

* d_feature_train (csv): 训练集特征变量
* d_feature_test (csv): 标签集特征变量
* d_label_train (csv): 训练集标签变量
* d_label_test (csv): 标签集特征变量
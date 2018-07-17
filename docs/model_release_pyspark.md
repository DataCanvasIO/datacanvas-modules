
## PipelineFitDPy3

读入管道并根据数据训练出管道模型

#### Tag:
* 模型发布_分布式

#### Param:
* None

#### Input:
* in1 (json): 输入pipeline
* in2 (any): 输入dataframe

#### Output:
* out1 (any): 输出训练好的pipeline

## Spark2PmmlDPy3

模型转换为pmml格式

#### Tag:
* 模型发布_分布式

#### Param:
* None

#### Input:
* in1 (any): 输入数据
* in2 (model.pkl): 输入模型

#### Output:
* None : 输出pmml模型

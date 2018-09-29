
## ClasPredictSPy3

通过已训练好的模型进行预测

#### Tag:
* 模型预测

#### Param:
* None

#### Input:

* d_feature (csv): 特征变量
* m_fitted_model (py3pkl): 算法训练好的模型

#### Output:

* d_predict (csv): 预测值及预测概率
* d_pred (csv): 预测值
* d_prob (csv): 预测概率

## LogisticPredSPy3

使用训练好的逻辑回归模型进行预测 (在原有预测数据上要先添加截距)

#### Tag:
* 模型预测

#### Param:
* None

#### Input:

* d_data1 (csv): 测试数据
* cols (py3pkl): 训练逻辑回归模型后筛选的变量
* m_fitted_model (py3pkl): 训练好的模型

#### Output:

* d_pred (csv): 预测值
* d_prob (csv): 预测概率
* d_feature (csv): 特征筛选后的自变量

## StackingPredictSPy3

根据训练好的Stacking模型对数据进行预测

#### Tag:
* 模型预测

#### Param:
* None

#### Input:

* d_feature (csv): 特征变量
* m_fitted_model (py3pkl): 训练好的模型
 
#### Output:

* d_pred (csv): 预测值
* d_prob (csv): 预测概率
* d_predict (CSV): 预测值和预测概率

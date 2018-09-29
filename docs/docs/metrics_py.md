
## ClasEvalNewSPy3

对二分类及多分类模型进行评估（包括AUC，Kappa，评估报告及混淆矩阵等）

#### Tag:
* 模型评估
* 可视化

#### Param:
* None

#### Input:

* d_true (csv): 真实标签
* d_pred (csv): 预测的标签变量
* d_prob (csv): 预测概率

#### Output:

* o_metric (csv): 各评估指标（准确率、Kappa分数、F分数、ROC值等）
* o_classification_report (txt): 评估报告(F分数、精确率、召回率)
* o_confusion_matrix (jpg): 混淆矩阵图

## ClasRocEvalSPy3a

输出分类模型的ROC曲线

#### Tag:
* 模型评估
* 可视化

#### Param:
* None

#### Input:

* d_feature (csv): 特征变量
* d_label (csv): 目标变量
* m_fitted_model (py3pkl): 训练好的模型

#### Output:

* o_roc_curve (jpg): ROC曲线图

## PlotLearningCurveSPy3_BestModel

画出学习曲线，根据训练集和测试集分数判断是否过拟合或欠拟合。

#### Tag:
* 模型评估
* 可视化

#### Param:

* n_jobs (int): 平行化运行工作的个数
* n_splits (int): 交叉验证时使用折数
* test_size (double): 验证集百分比

#### Input:

* d_feature (csv): 特征变量
* d_label (csv): 目标变量
* best_model (py3pkl): 训练好的模型

#### Output:

* learning_curve (jpg): 学习曲线图

## PlotLearningCurveSPy3

画出学习曲线，根据训练集和测试集分数判断是否过拟合或欠拟合。

#### Tag:
* 模型评估
* 可视化

#### Param:

* n_jobs (int): 平行化运行工作的个数
* n_splits (int): 交叉验证时使用折数
* test_size (double): 验证集百分比
* model (string) : 输入模型estimator, 例如GaussianNB()

#### Input:

* d_feature (csv): 特征变量
* d_label (csv): 目标变量

#### Output:

* learning_curve (jpg): 学习曲线图

## RegrEvalSPy3

对回归模型进行评估（包括mae,mse,r2等）

#### Tag:
* 模型评估

#### Param:
* multioutput (string) : 计分算法

#### Input:

* d_true (csv): 真实标签
* d_pred (csv): 预测标签

#### Output:

* o_metric (csv): 返回的模型各评估值

## ReportPDFClasEvalSPy3

输出分类评估报告

#### Tag:
* 模型评估
* 可视化

#### Param:
* None

#### Input:

* o_metric (csv): 各评估指标（准确率、Kappa分数、F分数、ROC值等）
* o_classification_report (txt): 评估报告(F分数、精确率、召回率)
* o_confusion_matrix (jpg): 混淆矩阵图
* o_roc_curve (jpg): ROC曲线图
* o_metric_2 (csv): 各评估指标（准确率、Kappa分数、F分数、ROC值等）
* o_classification_report_2 (txt): 评估报告(F分数、精确率、召回率)
* o_confusion_matrix_2 (jpg): 混淆矩阵图
* o_roc_curve_2 (jpg): ROC曲线图

#### Output:

* evaluation_report (pdf): 评估报告

## ScoresSendSPy3

发送评估数据

#### Tag:
* 模型评估

#### Param:
* None

#### Input:

* Scores (csv): 分数
* model (any): 最优模型

#### Output:

* modelScores (	py3pkl): 模型评估分数

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

## ClasRocEvalSPy3

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

## FormShowCSVUnivSPy3

以HTML形式显示DataFrame

#### Tag:
* 可视化

#### Param:
* None

#### Input:
* d_data (csv): csv形式的数据

#### Output:
* d_form (html): html形式的数据

## FormShowUnivSPy3

以HTML形式显示DataFrame

#### Tag:
* 可视化

#### Param:
* None

#### Input:
* d_data (py3pkl): pickle形式的数据

#### Output:
* d_form (html): html形式的数据 

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

* distortion_plot (html): 肘部图 
* centers_plot (html): 聚类中心雷达图 

## PlotLearningCurveSPy3_BestModel

画出学习曲线，根据训练集和测试集分数判断是否过拟合或欠拟合。

#### Tag:
* 模型评估
* 可视化

#### Param:
* n_jobs (int) : Number of jobs to run in parallel
* n_splits (int) : 交叉验证时使用折数
* test_size (double) : 验证集百分比

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
* n_jobs (int) : Number of jobs to run in parallel
* n_splits (int) : 交叉验证时使用折数
* test_size (double) : 验证集百分比
* model (string) : 输入模型estimator, 例如GaussianNB()

#### Input:
* d_feature (csv): 特征变量
* d_label (csv): 目标变量

#### Output:
* learning_curve (jpg): 学习曲线图 

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

## WOE_IV_DataSPy3

IV的全称是Information Value，中文意思是信息价值，或者信息量。我们需要一些具体的量化指标来衡量每个自变量的预测能力，并根据这些量化指标的大小，来确定哪些变量进入模型。IV就是这样一种指标，他可以用来衡量自变量的预测能力。类似的指标还有信息增益、基尼系数等等。高IV表示该特征和目标变量的关联度高；目标变量只能是二分类；特征分箱越细，IV越高。

WOE的全称是“Weight of Evidence”，即证据权重。WOE是对原始自变量的一种编码形式。WOE表示的实际上是“当前分组中响应客户占所有响应客户的比例”和“当前分组中没有响应的客户占所有没有响应的客户的比例”的差异。

#### Tag:
* 可视化
* 数据预处理

#### Param:
* label (string) : 标签变量

#### Input:
* d_data1 (py3pkl): 输入数据
* o_all_var (py3pkl): 所有需要计算WOE的变量

#### Output:
* o_IV_bar_plot (jpg): IV分布柱形图
* o_WOE_corr_plot (jpg): 计算WOE后的相关性热力图
* o_vars_after_corr (txt): 根据阈值相关性筛选后剩余的变量
* o_vars_after_VIF (txt): 多重共线性筛选后剩余的变量
* d_data2 (py3pkl): 计算WOE后的数据输出
* o_vars_after_VIF_pkl (py3pkl): 多重共线性筛选后剩余的变量 (pkl格式) 

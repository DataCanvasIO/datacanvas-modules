
## AdaboostClasSPy3

一种对同一个训练集训练不同的分类器(弱分类器)，然后把这些弱分类器集合起来构成一个更强的最终分类器(强分类器)的迭代算法。其算法本身是通过改变数据分布来实现的，它根据每次训练集之中每个样本的分类是否正确，以及上次的总体分类的准确率，来确定每个样本的权值。将修改过权值的新数据集送给下层分类器进行训练，最后将每次训练得到的分类器最后融合起来，作为最后的决策分类器。使用adaboost分类器可以排除一些不必要的训练数据特征，并放在关键的训练数据上面。

#### Tag:
* 分类模型

#### Param:
* n_estimators (int) : 评估器数量
* learning_rate (double) : 收敛速度

#### Input:
* d_feature (csv) : 特征变量
* d_label (csv) : 目标变量

#### Output:
* d_pred (csv) : 预测值
* d_prob (csv) : 预测概率
* m_fitted_model (py3pkl) : 训练好的模型

## AssembleBaseLeanersSPy3

将多个模型组成一个list以便传入Stacking模型中

#### Tag:
* 分类模型

#### Param:
* None
#### Input:

* model1 (py3pkl): 模型1
* model2 (py3pkl): 模型2
* model3 (py3pkl): 模型3
* model4 (py3pkl): 模型4
* model5 (py3pkl): 模型5

#### Output:

* m_base_learners (py3pkl): 5个模型组成的Base Learner

## BaggingClasSPy3

bagging是一种用来提高学习算法准确度的方法，这种方法通过构造一个预测函数系列，然后以一定的方式将它们组合成一个预测函数。Bagging要求“不稳定”（不稳定是指数据集的小的变动能够使得分类结果的显著的变动）的分类方法。比如：决策树，神经网络算法。

#### Tag:
* 分类模型

#### Param:
* n_estimators (int) : 评估器数量
* max_samples (double) : 最大采样比率
* max_features (double) : 最大特征比率

#### Input:

* d_feature (csv): 特征变量
* d_label (csv): 目标变量

#### Output:

* d_pred (csv): 预测值
* d_prob (csv): 预测概率
* m_fitted_model (py3pkl): 训练好的模型 

## DecisionTreeClasSPy3

决策树(decision tree)是一种基本的分类与回归方法。决策树模型呈树形结构，在分类问题中，表示基于特征对实例进行分类的过程。它可以认为是if-then规则的集合，也可以认为是定义在特征空间与类空间上的条件概率分布。其主要优点是模型具有可读性，分类速度快。学习时，利用训练数据，根据损失函数最小化的原则建立决策树模型。预测时，对新的数据，利用决策树模型进行分类。
决策树学习通常包括3个步骤：特征选择、决策树的生成和决策树的修剪。

#### Tag:
* 分类模型

#### Param:
* min_impurity_split (double) : 预剪枝时节点的不纯度(gini或者entropy)低于此阈值就不再分裂; 注：9999.0表示默认值None
* criterion (string) : 节点最佳分裂的判断标准，可选值'gini'和'entropy'，默认值'gini'
* max_depth (int) : 树的最大深度。默认值不限制，当不设置的时候，树不能无限生长，它会由其他参数来控制它的生长；9999.0表示默认值None
* min_samples_split (int) : 节点继续往下分裂的最小样本数要求
* min_samples_leaf (int) : 叶子节点的最小样本数要求
* max_features (double) : 节点分裂时使用的最大特征数，数据集比较大的时候，对特征进行抽样，提高速度；注：注：9999.0表示默认值None

#### Input:

* d_feature_test (csv): 特征变量
* d_label_test (csv): 目标变量

#### Output:
* dtc_model (py3pkl): 训练好的模型

## ExtratreesClasSPy3

这个类实现了一个元估计器，该估计器适合于数据集的各个子样本上的多个随机决策树（又名extra-trees），并使用平均值来提高预测准确度和控制过度拟合。

#### Tag:
* 分类模型

#### Param:
* n_estimators (int) : 评估器数量
* learning_rate (double) : 收敛速度

#### Input:

* d_feature (csv): 特征变量
* d_label (csv): 目标变量

#### Output:

* d_pred (csv): 预测值
* d_prob (csv): 预测概率
* m_fitted_model (py3pkl): 训练好的模型 

## GradientboostingClasSPy3

和Adaboost不同，Gradient Boosting 在迭代的时候选择梯度下降的方向来保证最后的结果最好。 损失函数用来描述模型的“靠谱”程度，假设模型没有过拟合，损失函数越大，模型的错误率越高 如果我们的模型能够让损失函数持续的下降，则说明我们的模型在不停的改进，而最好的方式就是让损失函数在其梯度方向上下降。

#### Tag:
* 分类模型

#### Param:
* n_estimators (int) : 评估器数量
* loss (string) : 损失函数
* learning_rate (double) : 收敛速度

#### Input:

* d_feature (csv): 特征变量
* d_label (csv): 目标变量

#### Output:

* d_pred (csv): 预测值
* d_prob (csv): 预测概率
* m_fitted_model (py3pkl): 训练好的模型 

## LinearSVCSPy3

支持向量机的优势在于:
1. 在高维空间中非常高效
2. 即使在数据维度比样本数量大的情况下仍然有效
3. 在决策函数（称为支持向量）中使用训练集的子集,因此它也是高效利用内存的
4. 通用性: 不同的核函数与特定的决策函数一一对应

支持向量机的缺点包括:
如果特征数量比样本数量大得多,在选择核函数时要避免过拟合,而且正则化项是非常重要的

#### Tag:
* 分类模型

#### Param:
* kernel (string) : 核函数
* C (double) : 惩罚因子

#### Input:

* d_feature (csv): 特征变量
* d_label (csv): 标签变量

#### Output:

* d_pred (csv): 预测值
* d_prob (csv): 预测概率
* m_fitted_model (py3pkl): 训练好的模型

## LogisticRegr_WOE_ClasSPy3

对WOE后的数据放入逻辑回归模型进行训练和特征筛选

#### Tag:
* 分类模型

#### Param:
* method (string) : 选择筛选变量的方法
* features_to_keep (int) : 

#### Input:

* d_feature (csv): 特征变量
* d_label (csv): 标签变量

#### Output:

* m_fitted_model (py3pkl): 训练好的模型
* o_summary (txt): 各变量训练后指标
* o_cols (py3pkl): 筛选后的变量
* o_feature_importances (pdf): 随机森林筛选法特征重要性可视化

## LogisticRegrSPy3

logistic回归是一种广义线性回归（generalized linear model），因此与多重线性回归分析有很多相同之处。它们的模型形式基本上相同，都具有 w‘x+b，其中w和b是待求参数，其区别在于他们的因变量不同，多重线性回归直接将w‘x+b作为因变量，即y =w‘x+b，而logistic回归则通过函数L将w‘x+b对应一个隐状态p，p =L(w‘x+b),然后根据p 与1-p的大小决定因变量的值。如果L是logistic函数，就是logistic回归，如果L是多项式函数就是多项式回归。

#### Tag:
* 分类模型

#### Param:
* penalty (string) : 正则化（泛化）方法
* C (double) : 正则化强度
* solver (string) : 最优化方法

#### Input:

* d_feature (csv): 特征变量
* d_label (csv): 目标变量

#### Output:

* d_pred (csv): 预测值
* d_prob (csv): 预测概率
* m_fitted_model (py3pkl): 训练好的模型

## RandomforestClasSPy3

随机森林是利用多棵树对样本进行训练并预测的一种分类器，它是一个包含多个决策树的分类器， 并且其输出的类别是由个别树输出的类别的众数而定。

#### Tag:
* 分类模型

#### Param:
* n_estimators (int) : 评估器数量
* criterion (string) : 特征选择方法

#### Input:

* d_feature (csv): 特征变量
* d_label (csv): 目标变量

#### Output:

* d_pred (csv): 预测值
* d_prob (csv): 预测概率
* m_fitted_model (py3pkl): 训练好的模型 

## StackingClasSPy3

堆栈模型：分为两层，第一层是几个模型的集合，第二层是单独的一个模型，用第一层几个模型的输出作为第二层的输入来训练元模型。

#### Tag:
* 分类模型

#### Param:
* folds (int) : 在拟合时使用的折数
* shuffle (string) : 是否在分折之前洗牌数据
* random_state (int) : 随机种子数
* verbose (int) : 打印日志信息详细程度
* n_jobs (int) : 在模型训练和预测过程中使用的计算机核数

#### Input:

* d_feature (csv): 特征变量
* d_label (csv): 目标变量
* m_base_learners (py3pkl): 基础模型(第一层)
* m_meta_learner (py3pkl): 元模型(第二层)
 
#### Output:

* d_pred (csv): 预测值
* d_prob (csv): 预测概率
* m_fitted_model (py3pkl): 训练好的模型

## VotingClassifierSPy3

三种模型的投票模型，可以选择软投票或者硬投票

#### Tag:
* 分类模型

#### Param:

* voting (string): 投票方式，soft和hard

* n_jobs (int): 平行化运行工作的个数

#### Input:

* d_feature (csv): 特征

* d_label (csv): 标签

* model1 (model.pkl): 模型1

* model2 (model.pkl): 模型2

* model3 (model.pkl): 模型3

#### Output:

* pred (csv): 预测值

* prob (csv): 预测概率

* model (py3pkl): 模型

## XGboostClasSPy3

在过滤数据样例寻找分割值时，XGBoost 通过预分类算法和直方图算法来确定最优分割。XGBoost本身无法处理分类变量，而是像随机森林一样，只接受数值数据。因此在将分类数据传入 XGBoost 之前，必须通过各种编码方式：例如标记编码、均值编码或独热编码对数据进行处理。

#### Tag:
* 分类模型

#### Param:

* learning_rate (double): 学习速率
* n_estimators (int): 评估器数量
* max_depth (int): 最大树深度 
* min_child_weight (double): 最小叶子节点权重和
* gamma (double): 分叉时需要的最小损失减少
* subsample (double): 训练每棵树时用来训练的数据占全部的比例
* colsample_bytree (double): 训练每棵树时用来训练的特征的比例
* objective (string): 目标函数定义

#### Input:

* d_feature (csv): 特征变量
* d_label (csv): 目标变量

#### Output:

* d_pred (csv): 预测值
* d_prob (csv): 预测概率
* m_fitted_model (py3pkl): 训练好的模型
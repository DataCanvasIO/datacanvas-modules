
## AdaboostRegrSPy3

一种对同一个训练集训练不同的回归器(弱回归器)，然后把这些弱回归器集合起来构成一个更强的最终回归器(强回归器)的迭代算法。其算法本身是通过改变数据分布来实现的，它根据每次训练集之中每个样本的预测是否正确，以及上次的总体的准确率，来确定每个样本的权值。将修改过权值的新数据集送给下层回归器进行训练，最后将每次训练得到的回归器最后融合起来，作为最后的决策回归器。使用adaboost回归器可以排除一些不必要的训练数据特征，并放在关键的训练数据上面。

#### Tag:
* 回归模型

#### Param:
* n_estimators (int) : 评估器数量
* learning_rate (double) : 收敛速度

#### Input:

* d_feature (csv): 特征变量
* d_label (csv): 目标变量

#### Output:

* d_pred (csv): 预测值
* o_import_feat (csv): 预测概率
* m_fitted_model (py3pkl): 训练好的模型

## BaggingRegrSPy3

bagging是一种用来提高学习算法准确度的方法，这种方法通过构造一个预测函数系列，然后以一定的方式将它们组合成一个预测函数。Bagging要求“不稳定”（不稳定是指数据集的小的变动能够使得分类结果的显著的变动）的分类方法。比如：决策树，神经网络算法。

#### Tag:
* 回归模型

#### Param:
* n_estimators (int) : 评估器数量
* max_samples (double) : 抽取的样本数量

#### Input:

* d_feature (csv): 特征变量
* d_label (csv): 目标变量

#### Output:

* d_pred (csv): 预测值
* m_fitted_model (py3pkl): 训练好的模型 

## DecisionTreeRegSPy3

决策树(decision tree)是一种基本的分类与回归方法。决策树模型呈树形结构，在分类问题中，表示基于特征对实例进行分类的过程。它可以认为是if-then规则的集合，也可以认为是定义在特征空间与类空间上的条件概率分布。其主要优点是模型具有可读性，分类速度快。学习时，利用训练数据，根据损失函数最小化的原则建立决策树模型。预测时，对新的数据，利用决策树模型进行分类。
决策树学习通常包括3个步骤：特征选择、决策树的生成和决策树的修剪。

#### Tag:
* 回归模型

#### Param:

* min_impurity_split (double): 预剪枝时节点的不纯度(gini或者entropy)低于此阈值就不再分裂; 注：9999.0表示默认值None
* max_depth (int): 树的最大深度。默认值不限制，当不设置的时候，树不能无限生长，它会由其他参数来控制它的生长；9999.0表示默认值None
* min_samples_split (int): 节点继续往下分裂的最小样本数要求
* min_samples_leaf (int): 叶子节点的最小样本数要求
* max_features (double): 节点分裂时使用的最大特征数，数据集比较大的时候，对特征进行抽样，提高速度；注：9999.0表示默认值None
* criterion (string): 节点最佳分裂的判断标准，可选值'gini'和'entropy'，默认值'gini'

#### Input:

* d_feature_test (csv): 特征变量
* d_label_test (csv): 目标变量

#### Output:
* None

## ExtratreesRegrSPy3

这个类实现了一个元估计器，该估计器适合于数据集的各个子样本上的多个随机决策树（又名extra-trees），并使用平均值来提高预测准确度和控制过度拟合。

#### Tag:
* 回归模型

#### Param:
* n_estimators (int) : 评估器数量
* criterion (string) : 评估算法

#### Input:

* d_feature (csv): 特征变量
* d_label (csv): 目标变量

#### Output:

* d_pred (csv): 预测值
* o_importance_feat (csv): 特征重要性
* m_fitted_model (py3pkl): 训练好的模型 

## GradientboostingRegrSPy3

Gradient Boosting 在迭代的时候选择梯度下降的方向来保证最后的结果最好。 损失函数用来描述模型的“靠谱”程度，假设模型没有过拟合，损失函数越大，模型的错误率越高 如果我们的模型能够让损失函数持续的下降，则说明我们的模型在不停的改进，而最好的方式就是让损失函数在其梯度方向上下降。

#### Tag:
* 回归模型

#### Param:
* n_estimators (int) : 评估器数量
* loss (string) : 损失函数
* learning_rate (double) : 收敛速度

#### Input:

* d_feature (csv): 特征变量
* d_label (csv): 目标变量

#### Output:

* d_pred (csv): 预测值
* o_importance_feat (csv): 特征重要性
* m_fitted_model (py3pkl): 训练好的模型 

## RandomforestRegrSPy3

随机森林是利用多棵树对样本进行训练并预测的一种分类器，它是一个包含多个决策树的分类器， 并且其输出的类别是由个别树输出的类别的众数而定。

#### Tag:
* 回归模型

#### Param:
* n_estimators (int) : 评估器数量
* criterion (string) : 特征选择方法

#### Input:

* d_feature (csv): 特征变量
* d_label (csv): 目标变量

#### Output:

* d_pred (csv): 预测值
* o_importance_feat (csv): 特征重要性
* m_fitted_model (py3pkl): 训练好的模型 

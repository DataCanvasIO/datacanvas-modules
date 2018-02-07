## Hive_To_Dataframe��hive��תdataframe

### Param:

* delimiter:���ݷָ��

* table_name:hive����

### Input:

* jdbc_url:hive���ַ

### Output:

* dataframe:�����df

## FromShow:�鿴dataframe

### Param:

* head:��ʾ������

### Input:

* dataframe:Ҫ�鿴��dataframe

### Output:

* Table:���Ƶ����ݱ�

## DataPreprocess:����Ԥ����

### Param:

* frac:�����ٷֱ���0.1, 0.5 '#'��ʾȡȫ��
* drop_columns:��ɾ�����ֶ���"x1",x2"
* LabelEncode:Ҫ����ķ����ֶ�

### Input:

* dataframe:�����������

### Output:

* df:����������

## select:�ֶ�ѡ��

### Param:

* col_name:������ѡ��"x1","x2","x3"
* col_no:���к�ѡ

### Input:

* data_source:Դ����

### Output:

* columns:��ѡ�����ֶ�

## LogisticRegression:�߼��ع�

### Param:

* model_save_path:ģ�ͱ���·��
* model_name:ģ������
* CV:������֤����
* metrics:ģ������ָ��:"accuracy","f1_micro","f1_macro"

### Input:

* X:�Ա���
* Y:Ԥ�����

### Output:

* model:ѵ������ģ��

## DecisionTreeClassifiter:����������

### Param:

* CV:������֤����
* criterion:The function to measure the quality of a split. eg:gini
* import_feature:���ص���Ҫ��������ֵ(< 1)��0.01
* min_sample_leaf:The minimum number of samples required to be at a leaf node
* max_depth:������
* metrics:ģ������ָ��:"accuracy","f1_micro","f1_macro"
* model_save_path:ģ�ͱ���·��
* model_name:ģ������
* min_samples_split:The minimum number of samples required to split an internal node

### Input:

* X:�Ա���
* Y:Ԥ�����

### Output:

* model:ѵ������ģ��
* TreeShow:�������ṹͼ
* import_X:��Ҫ����������

### MetriceShow:ģ��ָ��鿴

### Input:

* model:ģ��

### Output:

* metrics:����ָ��
* metrics_desribe:����ָ��ͳ��

## ModelSelect:ģ��ѡ��

### Param:

* metric:����ָ��

### Input:

* model_A:ģ��
* model_B:ģ��

### Output:

* better_model:ѡ��������ģ��

## Predict:Ԥ��

### Param:

* result_col_name:Ԥ�������ֶ���

### Input:

* model:ģ��
* X:�Ա���

### Output:

* Y:Ԥ�����

## ResultEvaluation:Ԥ��������

### Param:
* FigureType:�������� �磺roc

### Input:

* Real:��ʵֵ
* Predict:Ԥ��ֵ

### Output:

* Show:�������

## df2hive:dataframe����hive

### Param:

* jdbc_url:hive���Ӵ�
* table_name:hive����

### Input:

* data:Ŀ������

## data_describe:�ֶ�ͳ��

### input:

* data:�����dataframe

### output:

* describes:����������Ϣ

## imputer:ȱʧֵ���

### input:

* data:�����dataframe

### output:

* data_new:���ȱʧֵ���dataframe

## HashingEncoder:���������ϣ����

### Param:

* columns:Ҫ����ı��� ��: x1,x2,x3 ����

### Input:

* data:�����dataframe

### Output:

* data_new:������dataframe


## OneHotEncoder:onehot����

### Param:

* columns:Ҫ����ı���

### Input:

* data:�����dataframe

### Output:

* data_new:������dataframe

## OrdinalEncoder:��֪�����Ľ�ɶ

### Param:

* columns:Ҫ����ı���

### Input:

* data:�����dataframe

### Output:

* data_new:������dataframe

## BinaryEncoder

### Param:

* columns:Ҫ����ı���

### Input:

* data:�����dataframe

### Output:

* data_new:������dataframe

## PolynomialEncoder

### Param:

* columns:Ҫ����ı���

### Input:

* data:�����dataframe

### Output:

* data_new:������dataframe

## BackwardDifferenceEncoder

### Param:

* columns:Ҫ����ı���

### Input:

* data:�����dataframe

### Output:

* data_new:������dataframe

## SumEncoder

### Param:

* columns:Ҫ����ı���

### Input:

* data:�����dataframe

### Output:

* data_new:������dataframe

## HelmertEncoder

### Param:

* columns:Ҫ����ı���

### Input:

* data:�����dataframe

### Output:

* data_new:������dataframe

## AdaBoost:�����㷨

### Param:

* learning_rate:ѧϰ����
* n_estimators:ѵ��ģ��ʱ�������������

### Input:

* x_train:������Ա���
* y_train:�����Ŀ�����

### Output:

* adaboost_classifier:ѵ�����adaboostģ��

## xgboost:�����㷨

### Param:

### Input:

* x_train:������Ա���
* y_train:�����Ŀ�����

### Output:

* xgboost_classifier:ѵ�����xgboostģ��

## StandardScaler:���ݱ�׼��

### Param:

### Input:

* df:�����dataframe

### Output:

* df_new:��׼�����dataframe

## MinMaxScaler:���ݹ�һ��

### Param:

### Input:

* df:�����dataframe

### Output:

* df_new:��һ�����dataframe

## SelectFromModel:����ѡ�񷽷�

### Param:

* method:������������ѡ���ǻ��ڷ���������ѡ��

### Input:

* x:������Ա���
* y:����������

### Output:

* x_new:����ѡ�����Ա���
* y_new:ͬy

## PearsonCorrelation:ͨ��Ƥ��ɭ���ϵ��ɸѡ����

### Param:
* corr_thel:��������ֵɸѡ����

### Input:

* x:������Ա���

### Output:
* x_new:�����ɸѡ����Ա���

## RFE:�ݹ�����ѡ�񷨣���������ɸѡ

### Param:

* step:ɸѡʱ����
* n_features:�����ı�������

### Input:

* x:������Ա���
* y:����������

### Output:

* x_new:����ѡ�����Ա���
* y_new:ͬy

## MINE:�����Ϣϵ��(MIE)���ں��������������Ի�����Ե�ǿ��

### Param:

* type:�����Ա���������Ա�����Ŀ�������������Ϣϵ��

### Input:

* x:������Ա���
* y:����������

### Output:

* mic:�����Ϣϵ��
* tic:����Ϣϵ��

## chi2:����ѡ�񷽷��������Ա�����Ŀ�������Ŀ���ͳ����

### Param:

* sample_rate:������������
* n_features:�������������ٷֱ�

### Input:

* x:������Ա���
* y:����������

### Output:

* x_new:����ѡ�����Ա���
* y_new:ͬy

## FunctionTransformer:��x���ݸ��û��Զ���ĺ����������ش˺����Ľ��

### Param:

### Input:

* x:�����dataframe

### Output:

* x_new:ת�����dataframe

## PolyNomialFeaturs:���ɶ���ʽ�ͽ�������

### Param:

* degree:����ʽ�����ĳ̶�
* interaction_only:�Ƿ�ֻ����������

### Input:

* x:�����dataframe

### Output:

* x_new:ת�����dataframe





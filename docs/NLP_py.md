
## Doc2VecPy3

自定义基于词袋模型与词聚类的doc2vec

#### Tag:
* 自然语言处理

#### Param:
* None

#### Input:

* in1 (any): 输入

* idf_path (any): 输入

* stop_words_path (any): 输入

* wc_path (any): 输入

#### Output:

* out1 (csv): 输出 

## FastTextSPy3

FastText是Facebook开发的一款快速文本分类器，提供简单而高效的文本分类和表征学习的方法

#### Tag:
* 自然语言处理

#### Param:

* model (string): skipgram 或者 cbow
* lr (double): 学习速率
* dim (int): 词向量维度

 
#### Input:

* word (txt): 分词后的数据

#### Output:

* model (bin): 包含模型参数的二进制文件以及字典和所有超参数。
* vec (bin): 词向量, 一词一行

## IDFSPy3

逆向文件频率

#### Tag:
* 自然语言处理

#### Param:
* None

#### Input:

* in1 (any): 输入

* top_words_path (any): 输入

#### Output:

* out1 (any): 输出

## JiebaSPy3

load进gensim生成的词向量模型，打印词向量

#### Tag:
* 自然语言处理

#### Param:
* None

#### Input:

* model (model): gensim训练的词向量模型

#### Output:

* None

## Word2CutSPy3

中文分词

#### Tag:
* 自然语言处理

#### Param:
* None

#### Input:

* text_feature (py3pkl): 输入的文本

#### Output:

* cut_feature (py3pkl): 分词后文本(pickle格式)
* cutted (txt): 分词后文本(txt格式可查看)

## Word2VecSPy3

把文本特征转成词向量

#### Tag:
* 自然语言处理

#### Param:
* None

#### Input:

* vectorizer (py3pkl): 训练后的词向量模型
* text_feature (py3pkl): 分词后文本

#### Output:

* vec_feature (py3pkl): 词向量

## WordFittingSPy3

训练词向量生成模型

#### Tag:
* 自然语言处理

#### Param:
* None

#### Input:

* word_set (py3pkl): 分词后文本

#### Output:

* vectorizer (py3pkl): 训练后的词向量模型

## WordSegdSPy3

中文分词

#### Tag:
* 自然语言处理

#### Param:

* cut_fields (string): 需要分词的字段，如果是多个字段用逗号隔开

* parallel_num (int): 分词并行进程数

#### Input:

* in1 (json): 输入

* dic_path (any): 输入

#### Output:

* out1 (any): 输出

## GensimWord2VecSPy3

用gensim对原始的文本进行分词、去除停用词等操作，得到特征列表，再训练词向量模型得到词向量

#### Tag:
* 自然语言处理

#### Param:

* folderPath (string): 源文件路径
* file_encoding (string): 文件编码格式
* mincount (int): 忽略所有频数小于mincount的词

#### Input:

* stopwords (txt): 停用词
* user_dict (txt): 原始文本

#### Output:

* fileSegWordPath (txt): 分词后文本
* model: 训练的词向量模型

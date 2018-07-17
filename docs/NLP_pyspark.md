
## CountVectorDPy3

将词汇生成文档的稀疏表示

#### Tag:
* 自然语言处理_分布式

#### Param:
* inputCol (string) : 
* outputCol (string) : 
* minDF (double) : 词汇表中的文档的最小数量
* minTF (double) : 最小tf值
* vocabSize (int) : 
* binary (string) : 是否二进制编码

#### Input:
* in1 (any) : 输入pipeline

#### Output:
* out1 (any) : 输出pipeline

## HashingTFDPy3

将原始特征通过应用哈希函数映射到索引中

#### Tag:
* 自然语言处理_分布式

#### Param:
* inputCol (string) : 
* outputCol (string) : 
* numFeatures (int) : 功能维度
* binary (string) : 是否二进制编码

#### Input:
* in1 (any) : 输入pipeline

#### Output:
* out1 (any) : 输出pipeline

## IDFDPy3

利用IDFModel获取特征向量（通常由HashingTF或CountVectorizer创建）并缩放每列

#### Tag:
* 自然语言处理_分布式

#### Param:
* inputCol (string) : 
* outputCol (string) : 
* minDocFreq (int) : 最低文档词频

#### Input:
* in1 (any) : 输入pipeline

#### Output:
* out1 (any) : 输出pipeline

## NGramDPy3

NGram

#### Tag:
* 自然语言处理_分布式

#### Param:
* inputCol (string) : 
* outputCol (string) : 
* n (int) : ngram的n值

#### Input:
* in1 (any) : 输入pipeline

#### Output:
* out1 (any) : 输出pipeline 

## RegexTokenizerDPy3

自定义分隔符分词，支持正则表达式

#### Tag:
* 自然语言处理_分布式

#### Param:
* inputCol (string) : 
* outputCol (string) : 
* toLowercase (string) : 是否将大写转成小写
* minTokenLength (int) : 最小分割长度
* gaps (string) : 
* pattern (string) : 分隔符，支持正则表达式

#### Input:
* in1 (any) : 输入pipeline

#### Output:
* out1 (any) : 输出pipeline

## StopWordsRemoverDPy3

去停用词

#### Tag:
* 自然语言处理_分布式

#### Param:
* inputCol (string) : 
* outputCol (string) : 
* stopWords (string) : 停用词逗号隔开
* caseSensitive (string) : 

#### Input:
* in1 (any) : 输入pipeline

#### Output:
* out1 (any) : 输出pipeline 

## TokenizerDPy3

空格分词

#### Tag:
* 自然语言处理_分布式

#### Param:
* inputCol (string) : 
* outputCol (string) : 

#### Input:
* in1 (any) : 输入pipeline

#### Output:
* out1 (any) : 输出pipeline 

## Word2VecDPy3

将每个单词映射到一个唯一的固定大小向量

#### Tag:
* 自然语言处理_分布式

#### Param:
* inputCol (string) : 
* outputCol (string) : 
* vectorSize (int) : 向量维度大小
* minCount (int) : 词最小总量
* numPartitions (int) : 设置分区数
* stepSize (double) : 
* maxIter (int) : 最大迭代次数
* seed (int) : 种子数
* windowSize (int) : 窗口大小
* maxSentenceLength (int) : 最大句子长度

#### Input:
* in1 (any) : 输入pipeline

#### Output:
* out1 (any) : 输出pipeline
 

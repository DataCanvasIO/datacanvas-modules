
## NormalVisuSR_all

报表展示可视化模块-静态图片

#### Tag:
* R

#### Param:

* x_data_factor_flag (string): 是否转化成维度因子,输入"y"/"Y"执行

* reorder_flag (string): 是否按y轴排序,"order"升序，"desc"降序,其他不排序

* lab_title (string): 图表标题内容

* x_lab_title (string): x轴标题内容

* y_lab_title (string): y轴标题内容

#### Input:

* df (csv): 输入

#### Output:

* pp1 (pdf): 输出

## NormalVisuSR_read_data

数据处理模块-1

#### Tag:
* R

#### Param:
* model_data_test_val (string) : 数据选择

#### Input:

* df (csv): 输入

#### Output:

* df_select (csv): 输出

## plotly_ggplot2_pie_2dim

动态-饼图

#### Tag:
* R

#### Param:
* lab_title (string) : 报表标题
* tooltip_text_val_up (string) : 提示标签前缀
* tooltip_text_val_down (string) : 提示标签后缀

#### Input:
* df (csv) : 输入

#### Output:
* ppg (html) : 输出

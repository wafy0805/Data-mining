注：1、因源数据集文件编码格式问题，我仅仅将要分析的数据单独复制粘贴到新的csv文件中做的处理~
       2、对于数据缺失的处理，采用了两种方法应对：（1）直接舍去空缺数据-与原数据结果一样（2）用最高频数据填充空缺数据，见xxx_update.py
数据集一：Melbourne Airbnb Open Data
1、calendar_dec18.csv
(1)观测数值属性：price——calendar_dec18.py
     填充空缺数据后的处理文件——calendar_dec18_update.py
2、cleansed_listings_dec18.csv
(1)观测数值属性：review_scores_rating——cleansed_listings.py
     填充空缺数据后的处理文件——cleansed_listings_update.py
(2)观测标称属性：property_type——Draw_cleansed_listings.py
3、listings_summary_dec18.csv
(1)观测数值属性：price——listings_summary_dec18.py
(2)观测标称属性：neighbourhood——Draw_listings_summary.py
数据集二：Wine Reviews
1、winemag-data_first150k.csv
(1)观测数值属性：price——winemag-data_first150k.py
     填充空缺数据后的处理文件——winemag-data_first150k_update.py
(2)观测标称属性：region_2——Draw_winemag-data_first150k.py
2、winemag-data-130k-v2.csv
(1)观测数值属性：price——winemag-data-130k-v2.py
     填充空缺数据后的处理文件——winemag-data-130k-v2_update.py
(2)观测标称属性：taster_name——Draw_winemag-data-130k-v2.py
1.通过整理的"热门蓝V分类.xls"文件提取所要分析的蓝V大号名单:
	运行文件"xls_output.py"，设定指定目录，生成各分类蓝V名单，以txt文件存储

2.通过新浪微博API获得指定用户的最新1000条微博：
	运行文件"weibo_API.py"中的函数"weibo_1000_content"
	
3.分析1000条微博，获得微博关键词：
	运行文件"get_keywords.py"中的函数"recode_keywords"，会生成每个蓝V账号的关键词文件

4.整合所有关键词，通过二分法两两合并，其中去掉字数少于2的词，词频少于4的词：
	运行文件"merge_two_files.py"中的函数"main"
	
5.对于总关键词表，用tfidf进行排序，提取前5000个高频关键词：
	运行文件"count_tfidf.py"
	
6.每个蓝V号对应5000个关键词生成一个向量：
	运行文件"vector.py"
	
7.获得每个大类的向量中心点：
	运行文件"center_point.py"
	
8.计算每个特定账号距离最近的大类：
	运行文件"check_distance.py"

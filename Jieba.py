import jieba
#Text obtaned from wiki of Zhu Shenghao
seg_list = jieba.cut("朱生豪（中文：朱生豪；拼音：ZhūShēngháo）（1912年2月2日至1944年12月26日）是一名中文翻译。他出生于中国浙江嘉兴，是中国最早将威廉·莎士比亚的作品翻译成中文的人之一。[1]他的翻译受到国内外学者的推崇。他共翻译了31部莎士比亚戏剧，其中27部在中华人民共和国成立之前出版。由于1966年开始的文化大革命以及1950年代前后的其他社会动荡，直到1978年，朱的完整著作才最终在北京出版。[2]为了使剧本适应中国人的阅读习惯，朱没有采用原始牛津版的时间顺序。相反，他将这些戏剧分为四类：喜剧，悲剧，历史戏剧和其他。莎士比亚全集的第一版中文印刷标志着中国莎士比亚戏剧研究的重大事件。", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  

seg_list = jieba.cut("朱生豪（中文：朱生豪；拼音：ZhūShēngháo）（1912年2月2日至1944年12月26日）是一名中文翻译。他出生于中国浙江嘉兴，是中国最早将威廉·莎士比亚的作品翻译成中文的人之一。[1]他的翻译受到国内外学者的推崇。他共翻译了31部莎士比亚戏剧，其中27部在中华人民共和国成立之前出版。由于1966年开始的文化大革命以及1950年代前后的其他社会动荡，直到1978年，朱的完整著作才最终在北京出版。[2]为了使剧本适应中国人的阅读习惯，朱没有采用原始牛津版的时间顺序。相反，他将这些戏剧分为四类：喜剧，悲剧，历史戏剧和其他。莎士比亚全集的第一版中文印刷标志着中国莎士比亚戏剧研究的重大事件。", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  

seg_list = jieba.cut("朱生豪（中文：朱生豪；拼音：ZhūShēngháo）（1912年2月2日至1944年12月26日）是一名中文翻译。他出生于中国浙江嘉兴，是中国最早将威廉·莎士比亚的作品翻译成中文的人之一。[1]他的翻译受到国内外学者的推崇。他共翻译了31部莎士比亚戏剧，其中27部在中华人民共和国成立之前出版。由于1966年开始的文化大革命以及1950年代前后的其他社会动荡，直到1978年，朱的完整著作才最终在北京出版。[2]为了使剧本适应中国人的阅读习惯，朱没有采用原始牛津版的时间顺序。相反，他将这些戏剧分为四类：喜剧，悲剧，历史戏剧和其他。莎士比亚全集的第一版中文印刷标志着中国莎士比亚戏剧研究的重大事件。")
print(", ".join(seg_list))

seg_list = jieba.cut_for_search("朱生豪（中文：朱生豪；拼音：ZhūShēngháo）（1912年2月2日至1944年12月26日）是一名中文翻译。他出生于中国浙江嘉兴，是中国最早将威廉·莎士比亚的作品翻译成中文的人之一。[1]他的翻译受到国内外学者的推崇。他共翻译了31部莎士比亚戏剧，其中27部在中华人民共和国成立之前出版。由于1966年开始的文化大革命以及1950年代前后的其他社会动荡，直到1978年，朱的完整著作才最终在北京出版。[2]为了使剧本适应中国人的阅读习惯，朱没有采用原始牛津版的时间顺序。相反，他将这些戏剧分为四类：喜剧，悲剧，历史戏剧和其他。莎士比亚全集的第一版中文印刷标志着中国莎士比亚戏剧研究的重大事件。")
print(", ".join(seg_list))

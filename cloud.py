import jieba
import wordcloud
import numpy as np
from PIL import Image
import pandas as pd

df = pd.read_excel('D:\\desktop\\livehouse\\live01.xls')
# 可以通过df.col 来指定某个列，value_count()在这里进行计数
df_li = df.values.tolist()

result = []
for s_li in df_li:
    result.append(s_li[0])
var = ' '.join(result)

words = jieba.lcut(var)
# f = open('text.txt','r',encoding = 'utf-8')
# txt = f.read()
# f.close
#mask = np.array(Image.open("cat.jpg"))
w = wordcloud.WordCloud(background_color="white",
                        width=800,
                        height=600,
                        max_words=150,
                        max_font_size=100,
                        font_path="./simyou.ttf",
                        # mask=mask,
                        contour_width=3,
                        contour_color='steelblue',
                        collocations=False
                        )
w.generate(var)
w.to_file("outfile.png")
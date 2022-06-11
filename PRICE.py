import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('D:\\desktop\\livehouse\\live01.xls')
# 可以通过df.col 来指定某个列，value_count()在这里进行计数
df_li = df.values.tolist()

hiphop = []
indep = []
rock = []

for s_li in df_li:
    '''if isinstance(s_li[3], str):
        s_li[3] = 0'''

    if s_li[2] == "HipHop":
        if isinstance(s_li[3], str):
            hiphop.append(0)
        else:
            hiphop.append(s_li[3])
    if s_li[2] == "独立":
        indep.append(s_li[3])
    if s_li[2] == "摇滚":
        rock.append(s_li[3])
# print(hiphop)
plt.boxplot((hiphop, indep, rock), labels=('hiphop', 'independence', 'rock'))
plt.show()

import pandas as pd
import numpy as np
from pyecharts import Bar
from pyecharts import Geo
from pyecharts import Pie

to_read = pd.read_excel('D:\\desktop\\livehouse\\live01.xls')
# 可以通过df.col 来指定某个列，value_count()在这里进行计数
to_read_counts = to_read['演出城市'].value_counts().sort_values(ascending=False)  # 降序
hot_ct_id = to_read_counts[:58].index
hot_ct_count = to_read_counts[:100].values
hot_ct = pd.DataFrame({
    '演出城市': hot_ct_id,
    '次数': hot_ct_count
})
print(hot_ct)

bar = Bar(title="城市分布", width=1200, height=600)
bar.add(name='city', x_axis=hot_ct_id, y_axis=hot_ct_count)

bar.render('citybar.html')

geo = Geo(
    "全国演出城市分布",
    title_color="#fff",
    title_pos="center",
    width=1100,
    height=700,
    background_color="#404a59",
)

data = []

for j in range(0, 58):
    data.append((hot_ct_id[j], hot_ct_count[j]))

attr, value = geo.cast(data)
geo.add(
    "",
    attr,
    value,
    visual_range=[0, 40],
    visual_text_color="#fff",
    symbol_size=15,
    is_visualmap=True,
    is_roam=True,
)
geo.render("citygeo.html")
print(data)
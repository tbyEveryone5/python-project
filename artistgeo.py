import pandas as pd
from pyecharts import Bar
from pyecharts import Geo

to_read = pd.read_excel('D:\\desktop\\livehouse\\artist01.xls')
# 可以通过df.col 来指定某个列，value_count()在这里进行计数
to_read_counts = to_read['地区'].value_counts().sort_values(ascending=False)  # 降序
hot_ct_id = to_read_counts[:92].index
hot_ct_count = to_read_counts[:92].values
hot_ct = pd.DataFrame({
    '地区': hot_ct_id,
    '次数': hot_ct_count
})
print(hot_ct)

geo = Geo(
    "全国音乐人工作室地区分布",
    title_color="#fff",
    title_pos="center",
    width=1100,
    height=700,
    background_color="#404a59",
)

data = []

for j in range(0, 92):
    data.append((hot_ct_id[j], hot_ct_count[j]))


attr, value = geo.cast(data)
geo.add(
    "",
    attr,
    value,
    visual_range=[0, 35],
    visual_text_color="#fff",
    symbol_size=15,
    is_visualmap=True,
    is_roam=True,
)
geo.render("artistgeo.html")
print(data)

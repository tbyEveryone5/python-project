import pandas as pd
from pyecharts import Pie

to_read = pd.read_excel('D:\\desktop\\livehouse\\live01.xls')
# 可以通过df.col 来指定某个列，value_count()在这里进行计数
to_read_counts = to_read['风格'].value_counts().sort_values(ascending=False)  # 降序
hot_ct_id = to_read_counts[:20].index
hot_ct_count = to_read_counts[:20].values
hot_ct = pd.DataFrame({
    '风格': hot_ct_id,
    '次数': hot_ct_count
})
print(hot_ct)

attr = hot_ct_id
value = hot_ct_count

pie = Pie("演出风格", title_pos='center', width=900)

pie.add(
    "style",
    attr,
    value,
    center=[55, 70],
    is_random=True,
    radius=[30, 70],
    rosetype="area",
    is_legend_show=False,
    is_label_show=True,
)
pie.render(path="pie.html")
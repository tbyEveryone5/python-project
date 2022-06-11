from bs4 import BeautifulSoup
import requests
import re
import xlwt
import xlrd  # 引入库

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/101.0.4951.67 Safari/537.36 "
}  # 用户代理

# 正则表达式

# 找live链接
findlink = re.compile(r'<a data-v-62202c70="" href="(.*?)">')

link_live = []
wb = xlrd.open_workbook("D:\\desktop\\livehouse\\artist.xls")
# 打开文件并返回一个工作蒲对象
sheet = wb.sheet_by_index(0)
# 通过索引的方式获取到某一个sheet，现在是获取的第一个sheet页，
# 也可以通过sheet的名称进行获取，sheet_by_name('sheet名称')
col_data = sheet.col_values(0)
index = 0
# print(col_data)
for i in range(1, 250):
    url = col_data[i]
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')

    for item in soup.find_all('div', class_='table-cell'):

        item = str(item)
        net = "https://www.showstart.com"

        link = re.findall(findlink, item)
        if link:
            net = net + str(link[0])
            link_live.append(net)

            print(index)
            index = index + 1

print(link_live)

# save
book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
sheet = book.add_sheet("live", cell_overwrite_ok=True)  # 创建工作表
col = ("演出链接")
for i in range(0, 1):
    sheet.write(0, i, col)  # 列名
for i in range(0, 1000):
    # print("第%d条" % i)
    data = link_live[i]
    for j in range(0, 1):
        sheet.write(i + 1, j, data)

book.save('D:\\desktop\\livehouse\\live.xls')

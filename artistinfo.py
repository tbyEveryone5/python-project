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

# 找artist链接
findlink = re.compile(r'<a class="name" data-v-037ad45b="" href="(.*?)">')
# 音乐人名字
findArtist = re.compile(r'<div class="name" data-v-b56caf7c="">(.*?)</div>')
# 音乐人地区
findArea = re.compile(r'<div class="p-text" data-v-b56caf7c="">地区：(.*?)</div>')
# 音乐风格
findSty = re.compile(r'<div class="p-text" data-v-b56caf7c="">风格：(.*?)</div>')
# 最低价格
findPrice = re.compile(r'<em data-v-62202c70="">¥(\d*)起</em>')

link_artist = []
artist_list = []

wb = xlrd.open_workbook("D:\\desktop\\livehouse\\artist.xls")
# 打开文件并返回一个工作蒲对象
sheet = wb.sheet_by_index(0)
# 通过索引的方式获取到某一个sheet，现在是获取的第一个sheet页，
# 也可以通过sheet的名称进行获取，sheet_by_name('sheet名称')
col_data = sheet.col_values(0)
# print(col_data)

for i in range(1, 1001):
    url = col_data[i]
    #print(url)
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')

    for item in soup.find_all('section', class_='profile-header'):
        artist = []
        item = str(item)

        name_artist = re.findall(findArtist, item)
        artist.append(name_artist)

        area = re.findall(findArea, item)
        artist.append(area)

        style = re.findall(findSty, item)
        artist.append(style)

        artist_list.append(artist)

#print(artist_list)

# save
book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
sheet = book.add_sheet("音乐人", cell_overwrite_ok=True)  # 创建工作表
col = ("音乐人", "地区", "风格")
for i in range(0, 3):
    sheet.write(0, i, col[i])  # 列名
for i in range(0, 1000):
    # print("第%d条" % i)
    data = artist_list[i]
    for j in range(0, 3):
        sheet.write(i + 1, j, data[j])

book.save('D:\\desktop\\livehouse\\artist01.xls')

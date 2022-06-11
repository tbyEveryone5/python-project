from bs4 import BeautifulSoup
import requests
import re
import xlwt

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/101.0.4951.67 Safari/537.36 "
}  # 用户代理
# print(soup.prettify())

# 正则表达式
# 找链接
findlink = re.compile(r'<a class="name" data-v-037ad45b="" href="(.*?)">')
# 音乐人名字
findArtist = re.compile(r'<a class="name" data-v-037ad45b="" href="/artist/\d*">(.*?)</a>')
# 音乐风格
findSty = re.compile(r'<div class="sty" data-v-037ad45b="">(.*?)</div>')
# 最近演出场数
findLive = re.compile(r'<em data-v-037ad45b="">(\d)</em>')

datalist = []

for i in range(0, 50):
    url = 'https://www.showstart.com/artist/list?pageNo=' + str(i)
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')

    for item in soup.find_all('div', class_='table-cell'):
        # print(item)
        data = []
        item = str(item)
        net = "https://www.showstart.com"

        link = re.findall(findlink, item)[0]
        net = net + link
        data.append(net)

        artist = re.findall(findArtist, item)
        data.append(artist)

        style = re.findall(findSty, item)
        data.append(style)

        live_num = re.findall(findLive, item)
        data.append(live_num)
        # print(data)
        datalist.append(data)


# save
book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
sheet = book.add_sheet("音乐人", cell_overwrite_ok=True)  # 创建工作表
col = ("音乐人详情链接", "音乐人", "风格", "最近有几场演出")
for i in range(0, 4):
    sheet.write(0, i, col[i])  # 列名
for i in range(0, 1000):
    # print("第%d条" % i)
    data = datalist[i]
    for j in range(0, 4):
        sheet.write(i + 1, j, data[j])

book.save('D:\\desktop\\livehouse\\artist.xls')

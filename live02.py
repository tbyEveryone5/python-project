import urllib.request
import urllib.error

import pandas as pd
import numpy as np
# from hyper.contrib import HTTP20Adapter
from bs4 import BeautifulSoup
import requests
import re
import xlwt
import sqlite3
import xlrd  # 引入库

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/101.0.4951.67 Safari/537.36 "
}  # 用户代理
# print(soup.prettify())

# 正则表达式
# live名字
findlive = re.compile(r'<div class="title" data-v-12271991=""><!-- --><!-- -->(.*?)</div>')
# artist
findartist = re.compile(r'<a data-v-12271991="" href=.*>(.*)<!-- --></a>')
# 演出地区
findArea = re.compile(r'<p data-v-12271991="">地址：(.*?).*<span class="link" data-v-12271991="">查看地图</span></p>')
# 音乐风格
findSty = re.compile(r'<label data-v-12271991=""><i class="el-icon-paperclip" data-v-12271991=""></i>(.*)</label>')
# 最低价格
findPrice = re.compile(r'<span>￥(\d*) .*</span></button>')


wb = xlrd.open_workbook("D:\\desktop\\livehouse\\live.xls")
# 打开文件并返回一个工作蒲对象
sheet = wb.sheet_by_index(0)
# 通过索引的方式获取到某一个sheet，现在是获取的第一个sheet页，
# 也可以通过sheet的名称进行获取，sheet_by_name('sheet名称')
# 获取第二列的数据
col_data = sheet.col_values(0)
#print(col_data)

live_list = []

for i in range(1, 2):
    url = "https://www.showstart.com/event/166693"
    #print(url)
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')

    for item in soup.find_all('div', class_='product'):
        live = []
        item = str(item)

        name_live = re.findall(findlive, item)
        live.append(name_live)

        area = re.findall(findArea, item)
        live.append(area)

        style = re.findall(findSty, item)
        live.append(style)

        price = re.findall(findPrice, item)
        live.append(price)

        print(live)
        live_list.append(live)

'''
# save
book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
sheet = book.add_sheet("音乐人", cell_overwrite_ok=True)  # 创建工作表
col = ("演出名称", "演出城市", "风格", "票价")
for i in range(0, 4):
    sheet.write(0, i, col[i])  # 列名
for i in range(0, 10):
    # print("第%d条" % i)
    data = live_list[i]
    for j in range(0, 4):
        sheet.write(i + 1, j, data[j])

book.save('D:\\desktop\\livehouse\\live01.xls')
'''
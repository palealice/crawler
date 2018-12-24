from bs4 import BeautifulSoup
import urllib.request
import requests
import os

x=0
def getDbImage(url_image):
    if not os.path.exists('d://images'):  # 检查文件夹是否存在
        os.mkdir('d://images')  # 创建文件夹（文件夹已存在则无法创建）

    response = requests.get(url_image)

    html = response.text  # 获得源代码

    soup = BeautifulSoup(html, 'html.parser')  # 创建对象  解析页面 html lxml

    my_girl = soup.find_all()  # 找到img标签 以列表形式存储 my_girl是返回的对象
    for i in my_girl:
        if i.get('href') and 'http' in i.get('href'):
            print(i.get('href'))

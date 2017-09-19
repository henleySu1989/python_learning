from lxml import etree
from bs4 import BeautifulSoup
import requests
import re

n = eval(input("请输入你要查询到第几页:\n"))
url = 'https://www.qiushibaike.com/hot/'
data_all = ""
for i in range(n):
    web_data = requests.get(url)
    Soup = BeautifulSoup(web_data.text,'lxml')
    # print(Soup)
    #爬取相关的信息
    authors = Soup.select('.author.clearfix h2')#后代所有的h2元素
    ages = Soup.select('.author.clearfix > div')
    laughs = Soup.select('.stats-vote > .number')
    comments = Soup.select('.stats-comments > a > .number')
    contents = Soup.select('.content')
    #抓取真实信息
    for age,author,laugh, comment,content in zip(ages,authors,laughs,comments,contents):
        # print(age)
        # 作者
        print(age)
        author = author.get_text().strip()
        data_all += (author+"  ")
        # 处理性别和年龄
        if author == '匿名用户':
            age = ""
            sex = ""
        else:
            print(author)
            pattern = re.compile('G.*n')
            sex_info = pattern.findall(str(age))
            age = age.get_text()
            print(age)
            print(sex_info)
            if 'manIcon' in sex_info[0]:
                sex = "男"
            else:
                sex = "女"

        data_all += (age+"  ")
        data_all += (sex+"\n")
        #内容
        content = content.get_text().strip()
        data_all += (content+"\n")
        #笑数和评论数
        laugh = laugh.get_text()
        comment = comment.get_text()
        # print('manIcon' in sex_info[0])
        # print(sex_info)
        # print(author.get_text()+": "+age.get_text()+': '+laugh.get_text()+':'+comment.get_text())
        # print(content.get_text().strip())
    current = Soup.select('.current')
    next_page = int(current[0].get_text().strip())+1
    url = 'https://www.qiushibaike.com/8hr/page/{}/'.format(next_page)

with open('qiushi.txt','w',encoding='utf8') as f:
    f.write(data_all)
    # print(current[0].get_text().strip())
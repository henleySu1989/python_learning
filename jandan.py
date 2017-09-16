from bs4 import BeautifulSoup
import requests
import urllib.request
import uuid
import os
import threading

imgPath = 'Image'
threadFlag = True;
def getimages(i):
    url = 'http://jandan.net/ooxx/page-{}#comments'.format(str(i))
    print(url)
    web_data = requests.get(url)
    Soup = BeautifulSoup(web_data.text, 'lxml')
    images = Soup.select('.text > p > a')
    if not os.path.isdir(imgPath):
        os.makedirs(imgPath)
    for image in images:
        imgAdr = 'http:'+ image.get('href')
        print(imgAdr)
        imgName = imgPath+'/'+str(uuid.uuid1())+'.jpg'
        urllib.request.urlretrieve(imgAdr,imgName)
        print(imgName+'  '+'下载完成')

start = eval(input("请输入起始页：\n"))
end = eval(input("请输入终止页：\n"))
print("开始下载")
try:
    for num in range(start,end+1):
         # _thread.start_new_thread(getimages,(num,))
        t = threading.Thread(target=getimages,args=(num,))
        t.start()
except:
    print("无法进入线程")
finally:
    threadFlag = False
import requests
import re
import pymongo
import time

MONGO_URL = 'localhost'
MONGO_DB = 'Maoyan'

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

def save_info(info):
    '''
    保存和去重
    :param info:
    :return:
    '''
    if db['MaoyanMovies'].update_one({'name':info['name']},{'$set':info},True):
        print('保存成功：',info)

def get_response(url):
    '''
    进行请求，获得响应
    :param url:
    :return:
    '''
    response=requests.get(url)#进行请求
    time.sleep(1)
    html = response.text#获得响应体
    return html

def get_info(html):
    '''
    提取并保存信息
    :param html:
    :return:
    '''
    pattern=re.compile(r'<dd>.*?data-src="(.*?)".*?class="name">.*?>(.*?)</a>.*?"star">(.*?)</p>'
                       r'.*?"releasetime">(.*?)</p>.*?"integer">(.*?)</i>.*?"fraction">'
                       r'(.*?)</i>',re.S)
    results=re.findall(pattern,html)
    for result in results:
        info={
            'url':result[0],#海报连接
            'name':result[1],#电影名
            'actor':result[2].strip()[3:],#主演
            'releasetime':result[3].strip()[5:],#上映时间
            'score':result[4]+result[5]#分数
        }
        save_info(info)#保存


#主体函数
def main():
    for i in range(0,10):#翻页
        url = 'https://maoyan.com/board/4?offset='+str(i*10)
        html=get_response(url)#请求，获得响应
        get_info(html)#提取信息

if __name__=='__main__':
    main()
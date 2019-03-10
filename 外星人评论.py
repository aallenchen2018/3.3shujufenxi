import time
import re
import requests
import json
import pymongo

MONGO_URL = 'localhost'
MONGO_DB = 'JdProduct'

client = pymongo.MongoClient(MONGO_URL)#连接数据库系统，创建客户端
db = client[MONGO_DB]#复用或者创建数据库


def 保存到_txt(info):

    with open(r'/home/aallen/爬虫库/外星人评论info.txt','a') as f:
        f.write('用户评论>>>'+str(info['content'])+'    产品>>>'+str(info['productColor'])+'   评论时间>>>'+str(info['referenceTime'])+'\n')
    print('ok')

def 保存到DB(html):
    html = html.replace('fetchJSON_comment98vv73(','').replace(');','')
    result=json.loads(html)
    comments = result['comments']
    for comment in comments:#对每条信息进行循环
        info={
            'content':comment['content'],#评论信息
            'productColor':comment['productColor'],#产品信息
            'referenceTime':comment['referenceTime'],#评论时间
    
        }

        if db['BeefRate'].insert_one(info):
            print('保存成功:',info)
        else:
            print('保存失败:', info)


        保存到_txt(info)


def 获取连接内容():
    page=int(input('想要获取多少页的评论'))
    for i in range(0,page):

        url='https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv73&productId=100003023800&score=0&sortType=5&page=4&pageSize=10&isShadowSku=0&rid=0&fold=1'
        headers={
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            'accept-language': 'zh-CN,zh;q=0.9'
        }
        req=requests.get(url=url,headers=headers)
        req.decoding='gbk'

        html=req.text
        保存到DB(html)


获取连接内容()




    
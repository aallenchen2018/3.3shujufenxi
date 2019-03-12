import time
import re
import requests
import json
import pymongo
from fake_useragent import UserAgent

MONGO_URL='localhost'
MONGO_DB='JdProduct'

client=pymongo.MongoClient(MONGO_URL)
db=client[MONGO_DB]

def save_txt(info):
    with open(r'/home/aallen/爬虫库/外星人评论info.txt','a') as f:
        f.write('用户评论>>>'+str(info['content']))
    print('ok')

def save_db(html):
    html=html.replace('fetchJSON_comment98vv74(','').replace(');','')
    print(html)
    result=json.loads(html)
    comments=result['comments']
    for comment in comments:
        info={
            'content':comment['content'],
            'productColor':comment['productColor'],
            'referenceTime':comment['referenceTime']

        }
        if db['BeefRate'].update_one({'content':info['content']},{'$set':info},True):
            print('保存成功',info)

from urllib import request
import json
import time
import pymongo

MONGO_URL = 'localhost'
MONGO_DB = 'JdProduct'

client = pymongo.MongoClient(MONGO_URL)#连接数据库系统，创建客户端
db = client[MONGO_DB]#复用或者创建数据库

def save_info(info):
    '''
    保存数据
    :param info:
    :return:
    '''
    if db['BeefRate'].insert_one(info):
        print('保存成功:',info)
    else:
        print('保存失败:', info)


def get_response(url):
    '''
    获得响应
    :param url:
    :return:
    '''
    headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'accept-language': 'zh-CN,zh;q=0.9'
    }
    req = request.Request(url=url,headers=headers,method='GET')
    response=request.urlopen(req)#获得响应
    time.sleep(1)
    result=response.read().decode('gbk')#提取响应体
    return result

def get_page(html):
    '''
    获取页码信息
    :param html:请求之后的响应体信息
    :return:返回页码
    '''
    html = html.replace('fetchJSON_comment98vv510(','').replace(');','')#将字符串替换成类似json字符串
    result=json.loads(html)#转化成字典
    page = result['maxPage']#提取页码信息
    return page

def get_info(html):
    '''
    获取信息
    :param html:获得请求的响应
    :return:
    '''
    html = html.replace('fetchJSON_comment98vv510(', '').replace(');', '')#将字符串替换成类似json字符串
    result = json.loads(html)#转化成字典
    comments = result['comments']#定位到包含评论的位置
    for comment in comments:#对每条信息进行循环
        info={
            'content':comment['content'],#评论信息
            'productColor':comment['productColor'],#产品信息
            'referenceTime':comment['referenceTime']#评论时间
        }
        save_info(info)#进行保存

#主体函数
def main():
    url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv510&productId=1515454684&score=0&sortType=5&page=1&pageSize=10&isShadowSku=0&rid=0&fold=1'
    result=get_response(url)#获取响应，主要是为了获取页码信息
    page=get_page(result)#提取页码信息
    for i in range(1,page+1):#翻页
        base_url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv510&productId=1515454684&score=0&sortType=5&page='+str(i)+'&pageSize=10&isShadowSku=0&rid=0&fold=1'
        html=get_response(base_url)#进行请求，获得响应
        get_info(html)#提取感兴趣的信息，并进行保存

if __name__=='__main__':
    main()
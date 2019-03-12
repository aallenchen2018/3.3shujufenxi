import requests
from bs4 import BeautifulSoup
import pymongo
import time

MONGO_URL = 'localhost'
MONGO_DB = 'Hose'

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

def save_info(info):
    '''
    保存信息
    :param info:
    :return:
    '''
    if db['Fangtianxia'].update_one({'url':info['url']},{'$set':info},True):
        print('保存成功',info)
    else:
        print('保存失败', info)

def get_response(url):
    '''
    进行请求
    :param url:
    :return:
    '''
    reponse=requests.get(url)
    time.sleep(1)
    reponse.encoding='gb18030'
    return reponse.text

def get_district(url):
    '''
    获取每个区域对应的url
    :param url:
    :return:
    '''
    html=get_response(url)#获得响应
    soup = BeautifulSoup(html,'html.parser')
    results = soup.select('div.qxName > a')
    print(results)
    name_url={}
    other_area=['不限','东莞','惠州','深圳周边']
    for result in results:
        if result.string.strip() not in other_area:
            yield (result.string,result['href'])

def get_page(district_url):
    '''
    获取每个区域的页码
    :param district_url:
    :return:
    '''
    html = get_response(district_url)
    soup = BeautifulSoup(html, 'html.parser')
    page=int(soup.select('.fanye .txt')[0].string[1:][:-1])
    return page

def get_info(base_url):
    '''
    提取信息
    :param base_url:
    :return:
    '''
    html = get_response(base_url)#获得响应
    soup = BeautifulSoup(html,'html.parser')
    results=soup.select('div.list')
    for result in results:
        half = len(result.select('.dj .half'))
        no2 = len(result.select('.dj .no2'))
        try:
            info={

                'name':result.select('dd > p > a')[0].string,
                'url':result.select('dd > p > a')[0].attrs['href'],
                'score':5-half*0.5 - no2*1,
                'address':result.select('dd p')[-1].get_text().strip(),
                'year':result.select('dd ul li')[-1].get_text().replace('年建成','').strip()
            }
            price = result.select('.priceAverage span')[0].get_text().strip()
            info['price']=price
        except IndexError:
            info['price']=''
        save_info(info)

#主体函数
def main():
    url='https://sz.esf.fang.com/housing/__1_0_0_0_1_0_0_0/'
    district_urls=get_district(url)#获取每个区域对应的url
    for district,district_url in district_urls:
        print(district)
        district_url='https://sz.esf.fang.com'+district_url
        page=get_page(district_url)#获取对应区域的页码
        for pn in range(1,page+1):#翻页
            base_url=district_url[:-8]+str(pn)+'_0_0_0/'
            get_info(base_url)#获取信息


if __name__ =='__main__':
    main()
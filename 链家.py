import requests
from bs4 import BeautifulSoup
import pymongo
import time
from fake_useragent import UserAgent


MONGO_URL = 'localhost'
MONGO_DB = 'Lhouse'

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

def get_response(url):
        
        headers={
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            'Referer':'http://www.mm131.com/xinggan/4819.html'
            
        }       
        reponse=requests.get(url=url,headers=headers)
        time.sleep(2)
        reponse.encoding='UTF-8'
        with open(r'/home/aallen/爬虫库/lianjia1info.txt','a') as f:
                f.write(reponse.text)
        print('保存到txt')
        return reponse.text


url='https://sz.lianjia.com/ershoufang/'
html=get_response(url)
soup=BeautifulSoup(html,'lxml')
results=soup.select('dl dd div a')
other=['限制条件']
for result in results:
        if result.string.strip() not in other:
                # print(result.string)
                district_url='https://sz.lianjia.com'+result['href']
                # print(district_url)
                print('正在进行 '+result['href'][11:]+' 区域')
                html=get_response(district_url)

                soup=BeautifulSoup(html,'lxml')
        # 没找到 # page=soup.select('#content > div.leftContent > div.contentBottom.clear > div.page-box.fr > div > a')
                page=5
                for pn in range(1,page+1):
                        base_url=district_url+'/pg'+str(pn)
                        html=get_response(base_url)

                        soup=BeautifulSoup(html,'html.parser')
                        print('abc')
                    
                        results=soup.select('.bigImgList')
                        # print(results)
                        
                        for result in results:
                                try:

                                        info={
                                                'name':result.select('.title')[0].string,
                                                'jiaotong':result.select('.subway')[0].text,
                                                'price':result.select('.price')[0].text,  

                                        }
                                     
                                        print('保存到字典',info)
                                except IndexError:
                                        info['price']=''
                                if db['lianjiainfo'].update_one({'name':info['name']},{'$set':info},True):
                                        print('保存成功!!!!',info)
                                else:
                                        print('保存失败',info)


                






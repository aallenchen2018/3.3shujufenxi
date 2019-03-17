# from urllib import request
import time
import re
import requests

#获取主页的标题和子页的图片

enter=input('enter')

def 爬虫第一页():
    try:
        for i in range(0,1):

            urlfirst_zi='http://img1.mm131.me/pic/'+enter+'/1.jpg'
            urlfirst='http://www.mm131.com/xinggan/'+enter+'.html'
            headers={
                'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
                'Referer':'http://www.mm131.com/xinggan/4819.html'
            }
            #爬主页
            req2=requests.get(url=urlfirst)
            req2.encoding='gbk'
            html1=req2.text
            

            pattern=re.compile(r'<title>(.*?)</title>'
                                r'.*?<meta.*?content="(.*?)".*?>',re.S)

            results=re.findall(pattern,html1)
            for result in results:
                info=result[0].strip()
                print(info)
                



                #爬子页
                req1=requests.get(url=urlfirst_zi,headers=headers)
                html1=req1.content

                time.sleep(1)


                with open(r'/home/aallen/爬虫库/妹子图/'+'1'+'>>>'+str(info)+'.jpg','wb') as f:
                    f.write(html1)
                print('ok,save '+str(i)+'page!!!')

    except Exception as result:
        print(result)

    finally:
        
        print('已经爬1页')   

def 爬虫():
    try:
        for i in range(0,100):
            url1='http://img1.mm131.me/pic/'+enter+'/'+str(i)+'.jpg'
            url2='http://www.mm131.com/xinggan/'+enter+'_'+str(i)+'.html'
            headers={
                'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
                'Referer':'http://www.mm131.com/xinggan/4819_'+str(i)+'.html'
            }
            #爬主页
            req2=requests.get(url=url2)
            req2.encoding='gbk'
            html1=req2.text
            

            pattern=re.compile(r'<title>(.*?)</title>'
                                r'.*?<meta.*?content="(.*?)".*?>',re.S)

            results=re.findall(pattern,html1)
            for result in results:
                info=result[0].strip()
                print(info)
                



                #爬子页
                req1=requests.get(url=url1,headers=headers)
                html1=req1.content

                time.sleep(1)


                with open(r'/home/aallen/爬虫库/妹子图/'+str(i)+'>>>'+str(info)+'.jpg','wb') as f:
                    f.write(html1)
                print('ok,save '+str(i)+'page!!!')

    except Exception as result:
        print(result)

    finally:
        
        print('已经爬完本专辑！！！！')

def 爬妹子final():
    爬虫第一页()
    爬虫()

爬妹子final()
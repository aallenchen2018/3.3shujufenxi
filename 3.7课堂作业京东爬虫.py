from urllib import request
import json
import time
import pymongo
MONGO_URL='localhost'


def get_re(url):
    req_headers={
        'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Referer':'https://alienware.jd.com/view_search-402179-0-5-1-24-1.html'
    }
    req=request.Request(url=url,headers=req_headers,method='GET')
    response=request.urlopen(req)
    time.sleep(1)
    result=response.read().decode('gbk')
    return result

def  get_pagenum(html):    #试试换html，占位词，代表main的result
    html_content= html.replace('fetchJSON_comment98vv375(','').replace(');','')
    dic=json.loads(html_content)
    max_page=dic['maxPage']
    return max_page
    
def get_info(html):
    html=html.replace('fetchJSON_comment98vv375(','').replace(');','')
    result=json.loads(html)
    comments=result['comments']
    for comment in comments:
        info={
            'pingjia':comment['comment'],
            'shijian':comment['creationTime']
        }
        save_info(info)






def main():
    url='https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv375&productId=7928131&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
    result=get_re(url)
    maxpage=get_pagenum(result)



if __name__=='__main__':
    main()


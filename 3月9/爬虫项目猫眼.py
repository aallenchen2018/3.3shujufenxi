import requests
import re
import pymongo
import time

MONGO_URL='localhost'
MONGO_DB='Maoyan'

client=pymongo.MongoClient(MONGO_URL)
db=client[MONGO_DB]

def save_info(info):
    if db['Maoyan'].update_one({'name':info['name']},{'$set':info},True):
        print('saved!!',info)



def get_response(url):
    response=requests.get(url)
    time.sleep(0.5)
    html=response.text  
    return html


def get_info(html):
    pattern=re.compile(r'</a>.*?<div.*?<p.*?><a.*?title="(.*?)".*?data-act' 
                        r'.*?<p.*?star">(.*?)</p>',re.S)

    # pattern=re.compile(r'<dd>.*?data-src="(.*?)".*?class="name">.*?>(.*?)</a>.*?"star">(.*?)</p>'
    #                     r'.*?"releasetime">(.*?)</p>.*?"integer">(.*?)</i>.*?"fraction">'
    #                     r'(.*?)</i>',re.S)
    results=re.findall(pattern,html)
    for result in results:
        info={
            'name':result[0],
            'actor':result[1].strip()[3:]
        }
        save_info(info)

def main():
    for i in range(0,10):
        url='https://maoyan.com/board/4?offset='+str(i*10)
        html=get_response(url)
        get_info(html)



if __name__=='__main__':
    main()



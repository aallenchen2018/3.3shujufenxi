import requests
import json

headers={
    # 'user_agent'='',
    # 'Referer'=''

}



# response=requests.get(url='http://httpbin.org/get?wd=python&a=b',headers=headers)
# print(response.text)
params={
    'wd':'python',
    'ab':'abc'
    }



response=requests.get(url='http://httpbin.org/get',params=params)
#post请求的话，后面加data=...
print(response.content)
print(response.url)
print(response.text)
print(response.headers)
print(response.cookies)
print(json.loads(response.text))
print(response.json()['origin'])


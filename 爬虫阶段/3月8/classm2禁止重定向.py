import requests
from urllib import request

headers={
    'Referer':'http://www.mm131.com/xinggan/2333_7.html'
}
r=requests.get(url='http://img1.mm131.me/pic/2333/7.jpg',allow_redirects=False,headers=headers)
print(r.status_code)
print(r.url)

with open ('abcd6.jpg','wb') as f:
    f.write(r.content)
    print('ok')

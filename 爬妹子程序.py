from urllib import request

url='http://img1.mm131.me/pic/2333/7.jpg'
headers={
    #'User-Agent':'...'
    'Referer':'http://www.mm131.com/xinggan/2333_7.html'
}

req=request.Request(url=url,headers=headers)
html=request.urlopen(req).read()
with open(r'./爬妹子/7.jpg','wb') as f:
    f.write(html)
print('ok')
from urllib import request
from urllib import parse

data2={
    'hello':'python',
    'wd':'python'
}

data2=bytes(parse.urlencode(data2),encoding='utf-8')
response=request.urlopen('http://httpbin.org/post',data=data2)
print(response.read().decode('utf-8'))



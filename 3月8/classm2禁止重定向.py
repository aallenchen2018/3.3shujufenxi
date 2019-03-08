import requests

r=requests.get('http://img1.mm131.me/pic/2333/3.jpg',allow_redirects=False)
print(r.status_code)
print(r.url)

from bs4 import BeautifulSoup


html = """
<html><head><title>百度一下，你就知道</title></head>
<body>
<p class="title" name="百度"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup=BeautifulSoup(html,'lxml')
a=soup.find_all(id='link2')
##选取列a列表中的第一个元素
print(a[0].get_text())


b=soup.select('.title')
print(soup.select('.title'))
print('*'*50)
print(b)
print(soup.select('#link1'))
print(b[0].get_text())
print('*'*100)
c=soup.select('#link2')
print(c)
print(c[0].get_text())

c=soup.select('body a:nth-of-type(2)')
print('*'*50)
print(c)

d=soup.select('body a')
print('*'*90)
print(d)
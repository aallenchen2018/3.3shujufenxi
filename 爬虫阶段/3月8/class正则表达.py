import re
import time
content='Hello 123 4567 world_this is a regex'
result=re.match(r'Hell(.*?)regex',content)
search=re.search(r'\d{3}\s\d{4}',content)

print(result.group())
print(search.group())

html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
        </li>
    </ul>
</div>'''

# # r1= re.search(r'<li.*?singer="(.*?)">(.*?)</a>',html,re.S)
# ra=re.search(r'<a.*?singer="(.*?)">(.*?)</a>',html,re.S)
# print(ra.group(1))
# # r2 = re.search(r'<li.*?active.*?singer="(.*?)">(.*?)</a>',html,re.S)
# rb=re.search(r'<a.*?/3.*?singer="(.*?)">(.*?)</a',html,re.S)
# print(rb.group(1),rb.group(2))
# rc=re.findall(r'singer="(.*?)">(.*?)</a>',html,re.S)
# print(rc)
# r3 = re.search(r'<li.*?/6.mp3.*?singer="(.*?)">.*?</i>(.*?)</a>',html,re.S)
# print(r1.group(1),r1.group(2))
# print(r2.group(1),r2.group(2))
# print(r3.group(1),r3.group(2))
####一次过

rd=re.findall(r'<li.*?>\s*(<a.*?singer="(.*?)">)?(.*?)<',html,re.S)
for r in rd:
    print(r[2],r[1])
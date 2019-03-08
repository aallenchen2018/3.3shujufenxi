#coding=utf-8
import pymysql
conn=pymysql.connect(host='localhost',user='root',passwd='1',db='zelin',port=3306,charset='utf8')

#连接主机名或者IP   host
#连接使用的用户名   user
#连接使用的密码     passwd
#连接哪个数据库     db
#连接端口           port
#字符集             charset

cur=conn.cursor()     #获取一个游标
cur.execute('select * from stu')  #所需要执行的语句
data=cur.fetchall()		#获取语句的执行结果
for i in data:
	print(i)
cur.close()			#关闭游标
conn.close()   			#关闭数据库连接，释放数据库资源
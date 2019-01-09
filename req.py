#coding=utf-8
import requests
import threading
import re
import random
from time import sleep
from bs4 import BeautifulSoup

__another__
'''

'''

#url = ''

def wr_log(log):
	"""
	打印log，传入log地址
	"""
	f = open('D:/TEST.txt','a')
	try:
		for i,v in log.items():
			st = i + ':' + v + '\n'
			f.write(st)
	except:
		print('err+1')
	f.close


def 返回体转字符串(请求体):
	请求体.encoding = 'gbk'
	文本 = 请求体.text
	return 文本

def counter(last=[0]):
	#+1方法
	next = last[0] + 1
	last[0] = next
	return next

def rqs(index):
	#请求程序
#	we = counter() #调试/输出次数用，每调用一次counter()返回+1整数
	# url = '' + ran(zilei) + '_' + ran(zizilei) + '_' + ran(pinpai) + '_s0_p' + ran(trucklong) + '-' + ran(boxlong) + '-' + \
	# 		ran(totalmass) + '-' + ran(mali) + '-' + ran(xuhang) + '-' + ran(oil)  + '-' + ran(paifang) + '-' + ran(pailiang) + '.html'
	url = ''%index
	r = requests.get(url) #发起请求
	# print(r.elapsed.total_seconds())
	# if '50' or '40' in str(r.status_code):
	# 	weq = str(we) + ':' + url + ',' + str(r.status_code) + ',' + time + '\n'
	# 	wr_log(weq)
	return 返回体转字符串(r)
	

def ran(par):
	#随机参数用
	a = random.choice(par)
	return a

for index in range(1,824):
	a = BeautifulSoup(rqs(index),features="lxml")
	美丽体_body = a.body
	美丽体_div29 = 美丽体_body.find_all('div')[29]
	美丽体_ten = 美丽体_div29.find_all('li')[:40]
	结果 = {}
	for i in 美丽体_ten:
		c = i.find_all('a')
		结果[c[1].text] = c[0].text
	wr_log(结果)


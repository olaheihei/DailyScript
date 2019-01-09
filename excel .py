#coding=utf-8

import json
import xlrd
import re

__author__ = 'olaheihei'
'''
excel取值专用
'''

data = xlrd.open_workbook(r'','rb') 				
table = data.sheets()[0]										
nrows = table.nrows 											
sheetname = data.sheet_names	
beginn = 5
table = table						
apinames = table.row_values(beginn - 1)[2]
apiurl = table.row_values(2)[3]

for i in range(8,9):    #可改参数，取第几行
	parameter = {}
	str2 = ''
	str1 = ''
	for o in table.row_values(i - 1)[3]:				
		str2 = str2 + o 												

	for x in table.row_values(i - 1)[2]:
		str1 = str1 + x

	plist = re.split(r'[\s\，\（\）\,\【\】]+' , str2)	
	#print(plist)	
	for w in plist:
		if w == 'abc':
			plist[plist.index('abc')] =  ' '
			

	for u , o in zip(plist[1::2] , plist[::2]):
		parameter[o] = u

	print ('++++++++++++++++++++++++++++\n','第%d个接口:'%(i - 4) , str1 )
	print ('参数：%s'%parameter)

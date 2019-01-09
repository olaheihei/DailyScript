#encoding:utf-8

' test module '

__author__ = 'zhoujian'

import requests
import json
import xlrd
import re
import datetime
import time









class Myfunction(object):


	def __init__(self,file_path,begins = 0,beginn = 5):
		'''
		file_path 为用例表格路径
		begins 为开始的sheet; beginn 为开始的行
		'''
		try:
			if beginn <= 4:
				print ('行数给错了！看不见表格是从哪行开始的？')
				quit()
			data = xlrd.open_workbook(file_path,'rb') 				
			table = data.sheets()[begins]										
			nrows = table.nrows 											
			sheetname = data.sheet_names	
			self.begins = begins		 
			self.beginn = beginn
			self.table = table						
			self.sheetname = sheetname()[begins]
			self.apinames = table.row_values(self.beginn - 1)[2]
			self.apiurl = table.row_values(2)[3]
			self.nrows = nrows
			self.mode = table.row_values(2)[5]
			self.begintime = datetime.datetime.now()


		except xlrd.biffh.XLRDError:
			print ('你就不能细心点？赶紧写个对的路径去！！')
			quit()

		except FileNotFoundError:
			print ('我去！你连文件名都能写错？你是猪么？？！')
			quit()



	def get_parameter(self):

		global parameter 
		global str1 
		global str2 
		global plist 
		global table
		

#		for i in range(self.beginn,self.nrows + 1):
		for i in range(self.beginn,7):

			parameter = {}
			str2 = ''
			str1 = ''
			for o in self.table.row_values(i - 1)[3]:				
				str2 = str2 + o 												

			for x in self.table.row_values(i - 1)[2]:
				str1 = str1 + x
				self.str1 = str1
							
			#plist = re.split(r'[\s+\u4e00-\u9fa5+\，\（\）\,\【\】]+' , str2)		
			plist = re.split(r'[\s\，\（\）\,\【\】]+' , str2)
			for w in plist:
				if w == 'abc':
					plist[plist.index('abc')] =  ' '

			for u , o in zip(plist[1::2] , plist[::2]):
				parameter[o] = u

			print ('++++++++++++++++++++++++++++\n','第%d个接口:'%(i - 4) , self.str1 )
#			print ('参数：%s'%parameter)
			yield parameter 



	def re_check(self,url,parameter = None):
		if self.mode == 'post':
#			print (self.apiurl,parameter)
			return self.re_post(self.apiurl,parameter)

		else :

			return self.errc(2)						#有问题			return self.re_get(self.apiurl,parameter)



	def re_get(self,url,parameter):

		global r
		self.parameter = parameter

		try:
			r = requests.get(url , params = self.parameter,timeout = 20)
			self.r = r
			print(r)
			if  '200' not in str(self.r) :
				return self.errc(9)

			if self.parameter is None:
				return self.errc(3)

			if r.json().get('status') == 1:
				return self.errc(1)						#接口正常返回，但该次请求失败

			elif r.json().get('status') == 0 :
				return None

			else :
				pass


		except requests.exceptions.ConnectTimeout: 
			return self.errc(7)

		except requests.exceptions.ConnectionError:
			return self.errc(4)

		except json.decoder.JSONDecodeError:
			return self.errc(5) 

		except requests.exceptions.InvalidSchema:
			return self.errc(6) 

		except requests.exceptions.ReadTimeout:
			return self.errc(8)

		

	def re_post(self,url,parameter):
		"""
		请求接口，并返回接口返回值；
		parameter为dict；
		返回json串；
		对异常处理没做，待优化

		"""
		
		self.parameter = parameter

		try:
			r = requests.post(url , data = self.parameter , timeout = 20)
			self.r = r
			if '200' not in str(self.r):
				return self.errc(9)

			if self.parameter is None:
				return self.errc(3)

			if r.json().get('status') == 1:
				return self.errc(1)

			elif r.json().get('status') == 0 :
				return None

			else :
				return self.errc(2)					

		except requests.exceptions.ConnectTimeout: 
			return self.errc(7)

		except requests.exceptions.ConnectionError:
			return self.errc(4)

		except json.decoder.JSONDecodeError:
			return self.errc(5) 

		except requests.exceptions.InvalidSchema:
			return self.errc(6) 

		except requests.exceptions.ReadTimeout:
			return self.errc(8)



	def wr_log(self,log,log_path):
		"""
		打印log，传入log地址
		"""
		self.log = log 

		if isinstance(self.log ,str):
			f = open(log_path,'a')
			f.write(self.log)
			f.close

		elif self.log is None:
			return

		else :
			print ('请传入字符串')



	def errc(self,errcode):

		if errcode == 1:
#			print('缺少参数')
			self.log1 = self.rlog() + '\n异常类型：缺少参数\n'
			return self.log1

		if errcode == 2:
#			print('异常')
			self.log1 = self.rlog() + '\n异常\n' 
			return self.log1 , self.r

		if errcode == 3:
#			print('麻烦您捎带手把参数传进来！')
			self.log1 = self.rlog() + '\n麻烦您捎带手把参数传进来！\n' 
			return self.log1

		if errcode == 4:
#			print('电脑网络问题？')
			self.log1 = self.rlog() + '\n错误类型：电脑网络问题？\n' 
			return self.log1

		if errcode == 5:
#			print('应该是参数错了')
			self.log1 = self.rlog() + '\n错误类型：参数问题\n' 
			return self.log1 

		if errcode == 6: 
#			print('看看url前边是不是有空格')
			self.log1 = self.rlog() + '\n错误类型：看看url前边是不是有空格\n' 
			return self.log1

		if errcode == 7:
			self.log1 = self.rlog() + '\n错误类型：20s超时\n'
			return self.log1

		if errcode == 8:
			self.log1 = self.rlog() + '\n错误类型：20s超时\n'
			return self.log1

		if errcode == 9:
			if '40' in str(self.r):
				self.log1 = self.rlog() + '\n错误类型：400+\n接口返回:' + str(self.r) + '\n'
				return self.log1 
	
			if '50' in str(self.r):
				self.log1 = self.rlog() + '\n错误类型：500+\n接口返回:' + str(self.r) + '\n'
				return self.log1
 	

	def rlog(self):
		self.relog = '\n---------------------------------\n' + self.begintime.strftime('%Y-%m-%d %H:%M:%S') + '\n' + 'exceptions :\n' + '功能：' + self.str1 + '\n' + self.apiurl + ' ,参数：' + str(self.parameter) + '\n' + str(self.r) + '\n' + str(self.r.text)
		return self.relog 

	def a(self):
		"""
		检查是否调用成功，可调用这个
		"""
		print ('pass')

	def start(self):
		self.sstr = '************开始执行检测************\n' + '监测接口平台：' + self.sheetname + '\n' + '执行时间: ' + self.begintime.strftime('%Y-%m-%d %H:%M:%S') + '\n' + '************************************\n'
		return self.sstr


	def end(self):
		self.endtime = datetime.datetime.now()
		self.expendtime = (self.endtime - self.begintime)
		self.estr = '\n************************************\n' + '本次检测耗时:' + str(self.expendtime) + '\n************本次检测结束************\n\n\n\n\n\n\n'
		return self.estr



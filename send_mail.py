#encoding:utf-8
import smtplib 
import email.mime.text
import email.mime.multipart
__author__ = 'olaheihei'
'''
邮件发送
'''

sender = 'mantis@.com'  
receiver = ['jian.zhou@.com' , 'meng.xing@.com']  
smtpserver = 'smtp.mxhichina.com'  


msg = email.mime.multipart.MIMEMultipart()  
msg['from'] = '发送人'  
msg['to'] = '相关人员'
msg['subject'] = '这边是标题'  

content = '''
	这里填文本
'''

txt = email.mime.text.MIMEText(content)
msg.attach(txt)


smtp = smtplib
smtp = smtplib.SMTP()  
smtp.connect('smtp.mxhichina.com','25' )  
smtp.login('mantis@.com', '')  
smtp.sendmail(sender, receiver, str(msg))  
smtp.quit()  

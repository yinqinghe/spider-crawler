from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
import smtplib

def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))
#发件人地址
from_addr='c987746808@163.com'
#发件人密码
password='ZCXLUDCDLYXUJVPS'
#收件人地址
to_addr='987746808@qq.com'

#ZCXLUDCDLYXUJVPS
#邮箱服务器地址
stmp_server='smtp.163.com'

#设置邮件信息
msg=MIMEText('傻逼','plain','utf-8')
msg['From']=_format_addr('一号牛马<%s>'% from_addr)
msg['To']=_format_addr('987746808@qq.com<%s>' %to_addr)
msg['Subject']=Header('一号牛马我已出仓，状态良好','utf-8').encode()
#发送邮件
for i in range(0,10):
    server=smtplib.SMTP(stmp_server,25)
    server.login(from_addr,password)
    server.sendmail(from_addr,[to_addr],msg.as_string())
    server.quit()
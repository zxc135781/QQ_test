# -*- coding: utf-8 -*-

import requests
import yaml
import os
import smtplib
import time
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

r = requests.get('http://task.qq.com/index.php/taskListContent?&pageSize=50&pageNumber=1')
print(r)
while r.status_code == 500:
    time.sleep(5)
    r = requests.get('http://task.qq.com/index.php/taskListContent?&pageSize=50&pageNumber=1')
a = r.json()
b = a['data']['taskList']
for index in range(len(b)):
    # print(b[index]['name'])
    if (b[index]['product'] == 'com.tencent.mobileqq' and b[index]['expireStatus'] == True):
        print(b[index]['versionBuild'])
        with open('father.yml') as f:
            content = yaml.load(f, Loader=yaml.FullLoader)
            if (content['versionBuild'] != b[index]['versionBuild']):
                # 报名部分
                headers = {
                    'Host': 'task.qq.com',
                    'Connection': 'Keep-Alive'
                }
                cookies = dict(uin='827169070', useopenid='1', appid='1105152396',
                               openid='1AB9A94FD82CEFAB18D66A99FCC8BE6B',
                               access_token='2EA30E286D552EADD6FF350AC25F9176')
                a = requests.get('https://task.qq.com/index.php/api/appSignup/' + b[index]['id'], headers=headers,
                                 cookies=cookies)
                print(a.text)
            print(content)
            content.update(
                {
                    'product': b[index]['product'],
                    'versionBuild': b[index]['versionBuild'],
                    'endTime': b[index]['endTime'],
                    'pkgDownloadUrl': b[index]['pkgDownloadUrl'],
                    'pkgMd5': b[index]['pkgMd5'],
                    'id': b[index]['id'],
                    'id_url': 'https://task.qq.com/index.php/api/appSignup/'+b[index]['id'],
                })
            print(content)
            version = content['version']

            print(version)
            # if (version!=b[index]['versionBuild']):
            #     url = b[index]['pkgDownloadUrl']
            #     name = url.split('/')[-1]
            #     get = requests.get(url)
            #     # with open('file' + '/' + name, 'wb') as fp:
            #     #     fp.write(get.content)
            #     version = b[index]['versionBuild']
            #     print(version)
            #     content.update(
            #         {
            #             'version': version,
            #         })
            #     with open('father.yml', 'w') as nf:
            #         yaml.dump(content, nf)
            #
            #     #邮件发送
            #     env_dist = os.environ # environ是在os.py中定义的一个dict environ = {}
            #     sender = env_dist.get('sender') #发件人
            #     receiver = env_dist.get('receiver') #收件人
            #     smtpserver = 'smtp.163.com'
            #     username = env_dist.get('sender')  #发件人
            #     password = env_dist.get('password') #密码
            #     mail_title = version
            #
            #     # 创建一个带附件的实例
            #     message = MIMEMultipart()
            #     message['From'] = sender
            #     message['To'] = receiver
            #     message['Subject'] = Header(mail_title, 'utf-8')
            #
            #     # 邮件正文内容
            #     message.attach(MIMEText(b[index]['product']+'\n'+version+'\n'+b[index]['pkgDownloadUrl'], 'plain', 'utf-8'))
            #
            #     # 构造附件1（附件为TXT格式的文本）
            #     # att1 = MIMEText(open('file/'+name, 'rb').read(), 'base64', 'utf-8')
            #     # att1["Content-Type"] = 'application/octet-stream'
            #     # att1["Content-Disposition"] = 'attachment; filename="test.html"'
            #     # message.attach(att1)
            #
            #     smtpObj = smtplib.SMTP_SSL(host='smtp.163.com')  # 注意：如果遇到发送失败的情况（提示远程主机拒接连接），这里要使用SMTP_SSL方法
            #     smtpObj.connect(smtpserver)
            #     smtpObj.login(username, password)
            #     smtpObj.sendmail(sender, receiver, message.as_string())
            #     print("邮件发送成功！！！")
            #     smtpObj.quit()
            with open('father.yml', 'w') as nf:
                yaml.dump(content, nf)

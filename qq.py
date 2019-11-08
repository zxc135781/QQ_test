# -*- coding: utf-8 -*-

import requests
import yaml

r=requests.get('http://task.qq.com/index.php/taskListContent?&pageSize=10&pageNumber=1')
a = r.json()
b= a['data']['taskList']
for index in range(len(b)):
    # print(b[index]['name'])
    if (b[index]['product']== 'com.tencent.mobileqq' and b[index]['expireStatus']==True):
        print(b[index]['versionBuild'])
        with open('father.yml') as f:
            content = yaml.load(f, Loader=yaml.FullLoader)
            print(content)
            content.update(
                {
                    'product': b[index]['product'],
                    'versionBuild': b[index]['versionBuild'],
                    'endTime': b[index]['endTime'],
                    'pkgDownloadUrl': b[index]['pkgDownloadUrl'],
                    'pkgMd5': b[index]['pkgMd5'],
                })
            print(content)
            with open('father.yml', 'w') as nf:
                yaml.dump(content, nf)

print($qqq)
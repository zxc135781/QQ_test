import requests
import yaml

cookies = {'skey':'@nbohiPe0P','uin':'o0358018109'}
r=requests.get('https://task.qq.com/index.php/api/searchAct',cookies=cookies)
print(r.json())

with open('father.yml') as f:
    content = yaml.load(f,Loader=yaml.FullLoader)
    print(type(content))
    print(content)
    content.update({'age': 38})
    print(content)
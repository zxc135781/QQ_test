import requests
import yaml

r=requests.get('http://task.qq.com/index.php/taskListContent?&pageSize=10&pageNumber=1')
a = r.json()
print(a['data']['taskList'])

with open('father.yml') as f:
    content = yaml.load(f,Loader=yaml.FullLoader)
    print(type(content))
    print(content)
    content.update({'age': 30})
    print(content)
    with open('father.yml', 'w') as nf:
        yaml.dump(content, nf)
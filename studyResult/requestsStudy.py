import requests
import json

def a():
    r = requests.get('https://www.bilibili.com/')
    print(r.status_code)
    print(r.text)

def b():
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
    r = requests.post('https://accounts.douban.com/passport/login',data={'form_email': '463628990@qq.com', 'form_password': '34utchen'},headers=headers)
    return r.status_code

def requestsStudy(url,params):
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
    r = requests.get(url, params, headers=headers)
    print(r.status_code)
    print(r.url)
    print(r.text)

# requestsStudy('https://search.bilibili.com/all',{'keyword':'LoL'})

def c():
    headers={'Content-Type': 'application/json;'}
    data = {'username':'deepexi_cjq','password':'OXBRxDYkAwkI3Ir09EgP8Q==','appId': '1','tenantId':'Gree'}
    data=json.dumps(data)
    r = requests.post('http://dev-dm-console.gree.com/application-center/api/v1/login',data= data, headers=headers)
    print(r.status_code)
    print(r.url)
    print(r.text)
    # 将 JSON 对象转换为 Python 字典
    # r.text中的loayload的key中的mobile的key
    print(json.loads(r.text)['payload']['mobile'])
c()
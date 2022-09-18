# coding=utf-8

login_url = 'https://login3.scrape.center/api/login'
login_data = {
    'username': 'admin',
    'password': 'admin',
}
data_url = 'https://login3.scrape.center/api/book/?limit=18&offset=0'

import requests

response = requests.post(login_url, data=login_data)
print(response.json())

# 获取到登录的token
token = response.json()['token']
print(token)

# 通过token获取数据
headers = {
    'Authorization': 'jwt ' + token,
}
data_response = requests.get(data_url, headers=headers)
print(data_response.json())
# 结果成功获取到数据


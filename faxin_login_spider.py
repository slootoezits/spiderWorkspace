# coding=utf-8

# 测试数据链接与登录链接
data_url = 'http://faxin.cn/lib/zyfl/zyflcontent.aspx?gid=A320847&libid=010101'
login_url = 'http://faxin.cn/login.aspx'

# 登录信息
login_hit = {
    'user_name': '3192990641@qq.com',
    'user_password': 'jies0525'
}
# login_hit = {
#     'user_name': '18214721407',
#     'user_password': '123456aL'
# }

# 1. 使用selenium实现登录获取cookie
# 2. 使用requests实现数据抓取

# 登录实现
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import json

# 指定webdirver的路径,需要注意webdirver的版本需要与浏览器版本一致或者比浏览器版本新
driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.get(login_url)
time.sleep(3)  # 等待渲染时间

# 定位用户名输入框
# 定位密码输入框
# 定位登录按钮
user_name = driver.find_element(By.XPATH, '//*[@id="user_name"]')
user_password = driver.find_element(By.XPATH, '//*[@id="user_password"]')
login_button = driver.find_element(By.XPATH, '//*[@id="submitButton"]')
# 输入用户名和密码，并点击登录，等待渲染
user_name.send_keys(login_hit['user_name'])
user_password.send_keys(login_hit['user_password'])
login_button.click()
time.sleep(3)

# 获取cookie
cookies = driver.get_cookies()
print(cookies)
# [{'domain': '.faxin.cn', 'expiry': 1698032605, 'httpOnly': False, 'name': '__bid_n', 'path': '/', 'secure': False, 'value': '1834eb197f158002e14207'}, {'domain': '.faxin.cn', 'expiry': 1663516799, 'httpOnly': False, 'name': 'sajssdk_2015_cross_new_user', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.faxin.cn', 'httpOnly': False, 'name': 'Hm_lpvt_a317640b4aeca83b20c90d410335b70f', 'path': '/', 'secure': False, 'value': '1663472600'}, {'domain': 'faxin.cn', 'httpOnly': False, 'name': 'insert_cookie', 'path': '/', 'secure': False, 'value': '71170129'}, {'domain': '.faxin.cn', 'httpOnly': False, 'name': 'Hm_lpvt_a4967c0c3b39fcfba3a7e03f2e807c06', 'path': '/', 'secure': False, 'value': '1663472605'}, {'domain': '.faxin.cn', 'expiry': 1663501404, 'httpOnly': False, 'name': 'up_cookie_name', 'path': '/', 'secure': False, 'value': '1901413-1663472593'}, {'domain': 'faxin.cn', 'expiry': 1698032604, 'httpOnly': False, 'name': 'sid', 'path': '/', 'secure': False, 'value': 'hywktdilfsoiyujsdvhknb0j'}, {'domain': '.faxin.cn', 'httpOnly': True, 'name': 'lawapp_web', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1FA459B46423E58B48181E0E2A6EF6E0D8D1B06BF5213DF524161C1638DD53B4583E82DAB9C19E08911D3D5C3F4E6921BE7A667D916EA1129D1F16C5BD38BB5BC6BBBC8F8CB332C62E5F835AA29FB72998E4E71A1FCD65654E2AA6CD0017F68BADF43F34ACADA14590ED3B1947187923277B639C23EE4A98DC31D4376B585C6335FD0FB28E48D74A0B4EEC2167589A8FF66EC512'}, {'domain': '.faxin.cn', 'expiry': 1695008604, 'httpOnly': False, 'name': 'Hm_lvt_a4967c0c3b39fcfba3a7e03f2e807c06', 'path': '/', 'secure': False, 'value': '1663472605'}, {'domain': '.faxin.cn', 'expiry': 1695008600, 'httpOnly': False, 'name': 'Hm_lvt_a317640b4aeca83b20c90d410335b70f', 'path': '/', 'secure': False, 'value': '1663472600'}, {'domain': '.faxin.cn', 'expiry': 1698032605, 'httpOnly': False, 'name': 'sensorsdata2015jssdkcross', 'path': '/', 'secure': False, 'value': '%7B%22distinct_id%22%3A%221834eb19767117f-09be09584697f6-26021c51-1327104-1834eb1976812cd%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%7D%2C%22%24device_id%22%3A%221834eb19767117f-09be09584697f6-26021c51-1327104-1834eb1976812cd%22%7D'}, {'domain': 'faxin.cn', 'httpOnly': True, 'name': 'ASP.NET_SessionId', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'hywktdilfsoiyujsdvhknb0j'}]
input('按任意键继续，访问数据页面')

# 将cookie保存，并设置到requests中，用于请求数据
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    'Referer': 'http://faxin.cn/login.aspx'
}
cookie_str = ''
for cookie in cookies:
    cookie_str += cookie['name'] + '=' + cookie['value'] + ';'
headers['Cookie'] = cookie_str  # 将cookie设置到headers中,以字符串的形式
resp = requests.get(data_url, headers=headers)
print(resp.status_code)
with open('faxin.html', 'w', encoding='utf-8') as f:
    f.write(resp.text)

# 请求成功，返回200
# 需要手动注销登录，否则会导致账号被锁定


# 因为session创建会话时就已经设置了cookie，但在使用中需要手动更新headers中的cookie
# 只能将cookie以字符串的方式设置到headers中，并用于session的连续访问


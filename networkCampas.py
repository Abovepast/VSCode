import requests

url = 'http://10.10.10.10/'
data = {
    'DDDDD': '17379265904@telecom',
    'upass': '123456',
    '0MKKey': '123456'
}

response = requests.post(url=url, data=data).status_code
# print(f'回应代码{response}')
if response==200:
    print('连接成功！')
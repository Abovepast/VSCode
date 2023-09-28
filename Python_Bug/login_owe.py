import requests

url = 'http://10.10.10.10/'

data = {
    # 'callback': 'dr1695098113437',
    'DDDDD': '17379265904@telecom',
    'upass': '123456',
    '0MKKey': '123456',
    # 'R1':' 0',
    # 'R3':' 0',
    # 'R6':' 0',
    # 'para':' 00',
    # 'v6ip':' ',
    # '_': '1695098072392'
}

headers = {
    # 'Accept':'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    # 'Accept-Encoding':'gzip, deflate',
    # 'Accept-Language':'zh-CN,zh;q=0.9,ru;q=0.8,en;q=0.7',
    # 'Connection':'keep-alive',
    # 'Cookie':'PHPSESSID=494kip8givovad4gdrvkak2le4',
    # 'Host':'10.10.10.10',
    # 'Referer':'http://10.10.10.10/',
    # 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    # 'X-Requested-With':'XMLHttpRequest'
}

response = requests.post(url=url, data=data, headers=headers).status_code
print(f'回应代码{response}')
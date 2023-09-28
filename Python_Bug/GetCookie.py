import requests
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    ' (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}
url='https://www.csdn.net/?'
r=requests.get(url=url,headers=headers)
cookiejar = r.cookies
cookiedict = requests.utils.dict_from_cookiejar(cookiejar)
print(cookiejar)
print(cookiedict)
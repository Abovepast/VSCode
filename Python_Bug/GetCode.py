import requests
r = requests.get('https://cn.bing.com')
print(r.status_code)
print(r.text)
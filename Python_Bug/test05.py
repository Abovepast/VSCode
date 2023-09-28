import requests
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    ' (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}

url = 'https://pic3.zhimg.com/100/v2-63d890808649aa21693ba4553ef20caa_hd.png'

r = requests.get(url=url, headers=headers)
with open('photo.jpg', 'wb') as f:
    f.write(r.content)
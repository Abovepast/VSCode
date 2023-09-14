import urllib.request
try:
    request = urllib.request.Request('https://bilibili.com/')
    response = urllib.request.urlopen(request)
    
    save = open('./Python_Bug/bing.html','w');
    save.write(str(response.read()))
    save.close()
except Exception as e:
    print(str(e))

import urllib
import urllib.request

url = 'http://qq.com'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'Cookie':'pgv_pvid=4697711143; pac_uid=0_14fb71f9752b0; iip=0; o_minduid=c1APj7jkDgV-O0SAS8VxzlGU98YnYqqM; appuser=3A5F71558F338618; _qpsvr_localtk=0.35540297714720603; Lturn=969; LKBturn=89; LPVLturn=41; LPLFturn=283; RK=bd8BQU1Jl0; ptcz=4da06f455357429f55aaa35c379b3c07dbbaecc2c7b0d6b8358a7244a5fcf73a; open_access_token=9A6929AAED14BDAD11542CDEC65AAB2A; open_openid=1C06494F3A34A00EC600285FC93D9B37; open_appid=100383922; logintype=11; wap_refresh_token=3F8ACC1FD517FA1568A0EA7197AAA32A; ams_openid=E4005524FD530EE92C1C238EC6D755A7; wap_encrypt_logininfo=AVcHREH7WMu8P54YvabrRXFTcijj5CpEuD9lzIydVnry2MVlpciXHW9l1XQH1Uj6dmRN9tHq11tlcwTrz4WxNkcdXjVWt3cgVQ',
    'Connection':'keep-alive'
    }

request = urllib.request.Request(url=url,headers=headers)   
response = urllib.request.urlopen(request)  #发起请求
html = response.read()   #用read()方法读取文件里的全部内容，返回字符串
print(response.getcode())   #返回HTTP响应码，返回200表示成功
print(response.geturl())    #返回数据的事迹url，防止重定向问题
print(response.info())  #返回服务器响应的HTTP标头
# print(html) #打印响应，返回内容
# save = open('qq_com.html','w')
# save.write(str(html))
# save.close()


from win10toast import ToastNotifier
import requests
import os
import socket

def get_ip():
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.connect(('8.8.8.8',80))
    ip = s.getsockname()[0]
    s.close()
    return ip

if __name__ == '__main__':

    #以下5个变量，需要根据自己的情况进行修改，
    #与MacroDroid中的几乎保持一致,
    #仅对中文作修改，其他的字符（特别是前后的单引号）均不要修改！
    login_IP = 'http://10.10.10.10/'
    not_sign_in_title = '上网登录页'
    result_return = 'result":1,"aolno":6179,"m46":0,"v46ip":"172.16.39.1","myv6ip":"","sms":0,"NID":"","olmac":"b025aa4155f6","ollm":0,"olm1":"00000000","olm2":"0002","olm3":0,"olmm":2,"olm5":0,"gid":1,"oltime":169200,"olflow":4294967295,"lip":"","stime":"","etime":"","uid":"17379265904@telecom'
    sign_parameter = f'http://10.10.10.10/drcom/login?callback=dr1678592471264&DDDDD=17379265904@telecom&upass=123456&0MKKey=123456&R1=0&R3=0&R6=0&para=00&v6ip=&_=1678592463318'
    signed_in_title = '注销页'

    #以下4个变量，可根据自己的需要，决定是否修改
    already_icon = None
    success_icon = None
    false_icon = None
    unknown_icon = None

    try:
        r = requests.get(login_IP,
                        timeout = 1)
        req = r.text
    except:
        req = 'False'

    if signed_in_title in req:
        ToastNotifier().show_toast(title = "该设备已经登录",
                   msg = "校园网状态",
                   icon_path = already_icon,
                   duration = 5,
                   threaded = False)
        os._exit(0)

    elif not_sign_in_title in req:
        r = requests.get(sign_parameter, timeout=1)
        req = r.text
        if result_return in req:
            ToastNotifier().show_toast(title = "登录成功",
                   msg = "校园网状态",
                   icon_path = success_icon,
                   duration = 5,
                   threaded = False)
        else:
            ToastNotifier().show_toast(title = "登录失败",
                   msg = "校园网状态",
                   icon_path = false_icon,
                   duration = 5,
                   threaded = False)

        os._exit(0)

    else:
        ToastNotifier().show_toast(title = "未连接到校园网",
                   msg = "校园网状态",
                   icon_path = unknown_icon,
                   duration = 5,
                   threaded = False)
        os._exit(0)



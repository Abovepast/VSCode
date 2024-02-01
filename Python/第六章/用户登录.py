import os


def menu():
    print("1. 用户注册")
    print("2. 普通帐户登录")
    print("3. 管理员帐户登录")
    print("4. 退出")


def user_register():
    init()
    print('注册帐户')
    f = open('flag.txt', 'w', encoding='utf-8')
    f.write("1")
    f.close()
    user_id = input("请输入你的用户名：")
    user_pwd = input("请输入你的密码：")
    user_path = "./user/" + user_id + ".txt"
    if not os.path.exists(user_path):
        f = open(user_path, 'w', encoding='utf-8')
        user = {'uname': user_id, 'upwd': user_pwd}
        f.write(str(user))
        f.close()
        print("注册成功")
    else:
        print("用户名已存在")


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def entry():
    # 选择普通用户还是管理员用户
    while True:
        # 清屏
        clear()
        menu()
        choice = input("请输入你的选择：")
        if choice == "1":
            user_register()
            input("按任意键继续...")
        elif choice == "2":
            user_login()
            input("按任意键继续...")
        elif choice == "3":
            root_login()
            input("按任意键继续...")
        elif choice == "4":
            exit()
        else:
            print("输入有误，请重新输入")


def init():
    # 初始化管理员用户
    if not os.path.exists("u_root.txt"):
        f = open('u_root.txt', 'w', encoding='utf-8')
        root = {'uroot': 'root', 'upwd': "123456"}
        f.write(str(root))
        f.close()

    # 创建普通用户文件夹
    print(os.getcwd())
    if not os.path.exists("user"):
        os.mkdir('user')


def root_login():
    # 当用户输入正确时，进入用户登录界面
    while True:
        root = input("请输入管理员用户名：")
        pwd = input("请输入管理员密码：")
        f = open('u_root.txt', 'r', encoding='utf-8')
        r_dit = eval(f.read())  # 返回字典
        f.close()
        if root == r_dit["uroot"] and pwd == r_dit["upwd"]:
            print("登录成功")
            break
        else:
            print("账号或密码错误，请重新输入")


def user_login():
    if not os.path.exists("flag.txt"):
        user_register()
        login()
    else:
        f = open('flag.txt', 'r', encoding='utf-8')
        word = f.read()
        f.close()
        print('哎哟，你干嘛~~')
        if word == "1":
            init()
            login()


def login():
    # 普通用户登录
    print("普通用户登录")
    while True:
        user_id = input("请输入你的用户名：")
        user_pwd = input("请输入你的密码：")
        user_path = "./user/" + user_id + ".txt"
        if os.path.exists(user_path):
            f = open(user_path, 'r', encoding='utf-8')
            user = eval(f.read())
            if user["upwd"] == user_pwd:
                print("登录成功")
                break
            else:
                print("账号或密码错误，请重新输入")
        else:
            print("用户名不存在，请重新输入")


if __name__ == '__main__':
    entry()

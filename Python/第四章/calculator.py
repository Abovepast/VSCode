
# content = "5-7";
# def prase (content):
#     index = content.find("+")
#     if(index!=-1):
#         return prase(content[0:index]) + prase(content[index+1])
#     index = content.find("-")
#     if(index!=-1):
#         if(content[0:index]==''):
#             return -prase(content[index+1])
#         elif(content[index-1:index]=="*" or content[index-1:index]=="/"):
#             index = content.find("*")
#             if(index!=-1):
#                 return prase(content[0:index]) * prase(content[index+1])
#             index = content.find("/")
#             if(index!=-1):
#                 return prase(content[0:index]) / prase(content[index+1])
#         else:
#             return prase(content[0:index]) - prase(content[index+1])
#     index = content.find("*")
#     if(index!=-1):
#             return prase(content[0:index]) * prase(content[index+1])
#     index = content.find("/")
#     if(index!=-1):
#             return prase(content[0:index]) / prase(content[index+1])
#     return float(content)
# num = prase(content)
# print(num)


#---------------学生管理系统-------------

# ---------------学生管理系统-------------
stu_info = [
    {
        'ID':'001',
        'name':'张三',
        'sex':'男'
    },
    {
        'ID':'002',
        'name':'李四',
        'sex':'女'
    }
]

def print_menu():
    print('==============================')
    print('\t学生管理系统')
    print('\t1.添加学生信息')
    print('\t2.删除学生信息')
    print('\t3.修改学生信息')
    print('\t4.显示所有学生信息')
    print('\t0.退出系统')
    print('==============================')
    pass


def add_stu_info():
    '''添加学生信息,学号，姓名，性别'''
    ID, name, gender = input("请依次输入学生学号、姓名、性别：").split(" ")
    stu_info.append(
        {
            'ID': ID,
            'name': name,
            'sex': gender
        }
    )


def del_stu_info():
    '''删除学生信息'''
    i = int(input('请输入要删除学生的序号'))
    del stu_info[i]

def modify_stu_info():
    '''修改学生信息'''
    if(len(stu_info)==0):
        print('列表为空！')
    else:
        i = int(input("请输入要修改的学生序号"))
        ID, name, gender = input("请依次输入学生学号、姓名、性别：").split(" ")
        stu_info[i]['ID'] = ID
        stu_info[i]['name'] = name
        stu_info[i]['sex'] = gender


def show_stu_info():
    '''显示学生信息'''
    print('学生信息如下')
    print('='*30)
    print('序号    学号   姓名    性别')
    i = 1
    for temp_info in stu_info:
        print('%d    %s    %s    %s' % (i, temp_info['ID'], temp_info['name'], temp_info['sex']))
def main():
    while True:
        print_menu()
        choice = input("请输入功能对应的数字(0-5):")
        if choice == '1':
            add_stu_info()
        elif choice == '2':
            del_stu_info()
        elif choice == '3':
            modify_stu_info()
        elif choice == '4':
            show_stu_info()
            break
        elif choice == '0':
            confrm = input("确认退出吗？(是Y/否N):")
            if(confrm == 'Y'):
                break
            else:
                print("输入有误或重新输入")
if __name__ == "__main__":
    main()

    
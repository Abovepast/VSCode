#-------------lambda-----------------#
# remainder = lambda num:num%2
# print(remainder(13))

# multiply = lambda x,y: x*y
# print(multiply(2,3))

#-----常态用途：短时间需要一个简单函数并传给高阶函数

# item = [
#     ('product1',10),
#     ('product2',9),
#     ('product3',12),
# ]

# #   list.sort(reverse=True|False, key=muFunc)
# item.sort(key = lambda item:item[1])
# print(item)

#----------------practise01
# sentence = 'This is a common interview question'

# char_frequency = {}
# for char in sentence:
#     if char in char_frequency:
#         char_frequency[char] += 1;
#     else:
#         char_frequency[char] = 1;

# char_frequency_sorted = sorted(char_frequency.items(), key= lambda kv:kv[1], reverse=True)

# print(char_frequency_sorted)

# print(char_frequency)


#-----------全局变量和局部变量--------#
#局部变量 函数内部定义的变量

# def fun1():
#     a = 100;
#     print("text------", a, '\n', id(a))


# def fun2():
#     a = 200;
#     print("text------", a, '\n', id(a))

# fun1()
# fun2()

#全局变量
# a = 100
# def fun1():
#     #global a   声明a为全局变量
#     a = 300
#     print("text------", a, '\n', id(a))

# def fun2():
#     print("text------", a, '\n', id(a))


# fun1()
# fun2()


# a = 100
# def text01():
#     a = 200
#     print(locals())     #局部名字空间
#     print(globals())    #全局名字空间


# text01()

#---------------形式参数和局部变量-----
# def test(a, b):
#     print(f'text函数中的变量值， 初始， a={a}, b={b}')
#     a = 10
#     b.append('bbb')
#     print(f'text函数中的变量值， 修改后， a={a}, b={b}')


# x = 20
# y = ['aaa']

# print(f'调用函数前text函数中的变量值 x={x}, y={y}')
# test(x, y)
# print(f'调用函数后text函数中的变量值 x={x}, y={y}')

#函数闭包
#全局变量有被修改风险
#nonlocal initial_amount非局部声明
#缺点：持续引用外部变量，占用内存
#优点：安全
# def outer(num1):
#     def inner(num2):
#         nonlocal num1
#         num1 +=num2
#         print(num1)
#     return inner


# fn = outer(10)
# fn(20)

#---------------装饰器--------------
# def foo():
#     print('i')


# def foo():
#     print('i')
#     logging.info('foo is running')


# def use_logging(func):
#     logging.warn('%s is running' % func.__name__)
#     func()


# def bar():
#     print("sdajwild")

# use_logging(bar)

#简单装饰器
# import logging
# def use_logging(func):
#     def wrapper():
#         logging.warn('%s is running' % func.__name__)
#         func()
#     return wrapper

# @use_logging    #使用了@后就可以省略调用use_logging()
# def bar():
#     print('I am bar')


# # bar = use_logging(bar)
# bar()

# def entrance(func):
#     def inner(*args, **kwargs):
#         print(f'inside function:{func.__name__}')
#         func(*args, **kwargs)
#     return inner

# @entrance    #使用了@后就可以省略调用use_logging()
# def fun(x):
#     print('I am fun')

# fun(10)


import logging
flag = False
def login():
    pass

def toLogin(func):
    def inner(*args, **kwargs):
        global flag
        if flag:
            func(*args, **kwargs)
            return func
        else:
            username = input('请输入用户名')
            pwd = input('请输入密码')
            if(username=='admin' and pwd=='123'):
                flag = True
                result = func(*args, **kwargs)
                return result
            else:
                print('登录失败')
    return inner

@toLogin
def shopping_list_add():
    print("购物车添加物品")

@toLogin
def shopping_list_del():
    print("购物车移除物品")


shopping_list_add()

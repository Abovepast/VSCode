#####-------列表生成表达式-------
# value = []
# for x in range(5):
#     value.append(2*x)
# print(value)

# value1 = [2*x for x in range(5)]    #通过for依次取值
# print(value1)

# ls1 = [x*x for x in range(10) if x%2!=0] #找其中的奇数
# print(ls1)

# values = {x: x*2 for x in range(5)}
# print(values)

# values = (x*2 for x in range(5))
# print(values)

#---------------practise--------------------------------#
# ls2 = [x*x for x in range(1, 11)]
# print(ls2)

# ls3 = ['52pojie', 'OVVO', 'asd', 'sdf', 'freg', 'res']
# ls4 = [x for x in ls3 if 'a' in x]
# print(ls4)
#---------------生成器---------------------#
# from sys import getsizeof
# ls = [x*2 for x in range(10000)]   #解决内存占用问题
# # print(ls)

# ls1 = (x*2 for x in range(10000))   #改成小括号
# # for i in ls:
# #     print(i)

# print("生成器大小：", getsizeof(ls1))
# print('列表大小：', getsizeof(ls))

#------------函数-----------
def fun():
    return 0;


def fun1():
    print('1')


def fun2():
    return '2'
#默认参数只能不带默认参数的前面

# myFuns = [fun, fun1, fun2]
# print(myFuns)

# i = fun() + 3 + 4
# ls = [i]
# print(ls)


# def Student(name, chineselevel='良好', country='中国'):
#     print('姓名：%s, 中文水平：%s, 国家：%s' % (name, chineselevel, country))


# def pInfo(name, *args):
#     print(f'姓名：{name}, 作品：{args}')

# pInfo('张三', 8.9, 7.8, 9)

# def PInfo(name, **kwargs):
#     print(f'姓名:{name}')
#     for k, v in kwargs.items():
#         print(f'{k}:{v}')

# info = {'身高':180, '国籍':'中国'}
# PInfo('张三', **info)

# ls = [1, 2, 3]
# print(*ls)
# print(*range(5))

# val = [*ls, *'hello']
# print(val)

# first = {'x':1}
# second = {'x':10, 'y':2}
# combined = {**first, **second}
# print(combined)


# def fun(N):
#     tsum=0
#     for i in range(1, N+1):
#         tsum+=i
#     return tsum


# print(fun(100))


# def funMax(*args):
#     max = args[0]
#     for x in args:
#         if(max<x):
#             max = x
#     return max


# print(funMax(1, 2, 4, 67))


# def funN(N=10):
#     s = 1
#     for i in range(1, N+1):
#         s*=i
#     return s


# print(funN(5))


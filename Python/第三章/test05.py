#----------流程控制
#------回文数
# str = input("请输入四位数：")
# if str==str[::-1]:
#     print('是')
# else:
#     print('否')
#-----循环
# d = {'name':'Tom'}
# for k in d.keys():
#     print(k, ":", d[k])

#-----sorted(),不改动原序列作排序
# ls = ['a', 'e', '79']
# ls1 = sorted(ls)
# print(ls1)

# dict1 = {
#     'name':'aa'
# }
# for k, v in dict1.items():
#     print(k, ">>", v)

# # print(type(dict1.items()))  #返回数据类型


# for item in range(3, 7, 2): #3开始，打印到7之前的数，步长2
#     print(item)

# print(list(range(5)))

# n = eval(input("input a number:"))   #取值
# sum = 0
# for i in range(1, n+1, 2):
#     sum+=i
# print('sum = ', sum)

for x in range(3):
    for y in range(3):
        print(f'({x},{y})')
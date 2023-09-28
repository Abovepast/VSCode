#-------------------------字典
# point = {"x":1, "y":2}
# print(point)
# point2 = dict(x=1, y=2)
# point2['x'] = 20    #修改
# print(point2["x"])
# point['z'] = 3  #可以插入，若打印不存在的z则报错
# print(point)
# print(point2.get("z"))  #不存在返回none

#---------------------------字典插删改
stu = {'sno':'10086', 'name':'Ikun'}
#--------------修改
# stu.update({'sno':'10090','age':'20'})  #增加了一条
# stu.update(name='Tom')
# print(stu)

#-----------删除
# del stu['name'] #删除name元素
# name = stu.pop('name')
# print('name = ',name)

#------------------------字典浅拷贝与深拷贝
# #深拷贝-----copy.deepcopy()
# import copy
# stu2 = copy.deepcopy(stu)
# #浅拷贝--------
# stu_ = stu.copy()

# print(stu_)
# print(stu2)
#-----------------拼接
# d1 = dict(sno='1009', name='Tony')
# d2 = dict(age=19)
# dMergel = dict(d1,**d2)

# dM = d1.copy()
# dM.update(d2)
#--------------清除
# d = {'sno':'109'}
# d.clear()   #元素没有
# del d   #彻底没有
# print(d)

# #----------
# dict_keys = stu.keys()  #返回所有key，迭代器
# print(dict_keys)
# print('长度：',len(stu))
#可变是不可哈希的;元组不可变，可哈希。

#--------------身份运算符
# is 对应相同的存储单元，返回true
# 不可变对象（字符串，数字，元组）指向同一个，true；可变对象反之
# x, y, z = 1, 2, 2
# print(x is y)
# print(id(x) == id(y))
# print(y is z)

# ls1 = [1, 2, 3]
# ls2 = [1, 2, 3]
# print(ls1 is ls2)   #false
# ls3 = ls1
# print(ls1 is ls3)


# cer = (1,'2')
# cer1 = (1,'2')
# print(cer is cer1)
#--------------成员运算符
# x, y = 15, ['abc', 15, True]
# print(x in y)
x, y = 'one',{'one':1}
print(x in y)
item_ = stu.items()
print(item_)
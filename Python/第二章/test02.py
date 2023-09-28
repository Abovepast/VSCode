import copy
# str = '  python是一种解释型语言  '
# print(str.strip().capitalize()) #首字母大写

# ls = 'abc'
# print(ls[::-1])

# ls01 = list('hello')
# print(ls01)

# ls01[2] = 'bv'
# print(id(ls01))
# ls2 = ls01[:]
# print(id(ls2))
# ls3 = copy.deepcopy(ls01)
# print(id(ls3))

#----------------------------------------------#
# ls = [1,3,5,7,8]
# print(ls.index(3))

# ls.insert(0,'as')
# ls.append([1,2])

# del ls[1:3]
# print(ls)

# ls[1:3] = []
# print(ls)

# ls.remove([1,2])
# print(ls)

# print(ls.pop()) #默认删最后一个
# print(ls)
#-------------------------------------------------#列表
# ls = [3,2,5,81,45,1,5]
# print(ls.count(5))
# print(len(ls))
# print(max(ls))
# print(min(ls))

# ls.sort()
# print(ls)

# ls.sort(reverse=True)
# print(ls)
#------------------------------------------------#元组
# tuple = (1,2,3,1,[3,5])
# print(tuple)
# print(tuple[1:3])
# print(tuple[1:2])
# tuple = tuple*2+('a','b')
# print(tuple)
# del tuple
# tuple = ('a','b')
# print(tuple)
# set = {1, 'a', 2, (6,), 2, 3}
# print(set)
# # set1 = set()
# # print(set1)

# set.add('bt')   #要可哈希
# print(set)

# set.update('bt')    #要可迭代
# print(set)
#-------------------------------------#集合
# s1 = {1,4,2,'a','vt',('c',3)}
# s2 = set([1,2,4])

# print(s1)
# print(s1.difference(s2))  #前者减交集
# print(s1.intersection(s2))
# print(s1.union(s2))
# print(s1.symmetric_difference(s2))

# #子集父集
# print(s1.issubset(s2))
# print(s2.issubset(s1)) #s2是否为s1的子集
#-----------------------------------------#字典
dt = {'name':1,'age':'two','name':'1',('abc',):3}  #键要唯一且可哈希
print(dt)
dt2 = dict(name='niganma', age=1)
print(dt2)

z = zip(['name', 'age'],['jack', 20])
# print(list(z))
print(dict(z))

ls1 = [("name", 'tom'), ('age', 20)]
print(dict(ls1))

#访问字典元素
print(dt['name'])

str1 = dt.get('name')
print(str1)
print(f"age:{dt.get('age')}")
print(f"gender:{dt.get('gender', '男')}")   #获取不到就使用右边的默认值
print(f"age:{dt['age']}")











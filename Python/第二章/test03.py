# seq = ['a', '9', '[1,3]']
# str = 'content'
# s1 = str.join(seq)
# print(s1)
# s2 = ''.join(seq)
# print(s2)

#02------------------------#
# print(str.find('e', 2)) #从参数2开始，查找参数1，返回下标
# print(str.find(str, 0))

#practice-----------------------------#
# ls = 'cdea'
# list(ls).sort(reverse=True)
# print(''.join(ls))

# str = input('输入一串字符：')
# print(''.join(str.sorted(reverse=True)))

#practice----------------------------#
# url = 'http://www.163.com?userName=admin&pwd=123456'
# domin = url[:url.find('?')]
# userName = url[(url.find('userName=')+9):url.find('&')]
# pwd = url[(url.find('pwd=')+4):]

# print('domin='+domin)
# print('userName='+userName)
# print('pwd='+pwd)

# ls = 'http?name'
# ls.split('?')
# print(ls.split('?'))
# print(ls[:ls.find('?')])

#practice02--------------------------------#
# ls = [2, 5, 6, 7, 8, 9, 2, 9, 9]
# print(ls)
# ls.append(15)
# print(ls)
# ls.insert(len(ls)//2, 20)
# print(ls)
# ls+=[2,5,6] #ls.extend([2, 5, 6])
# print(ls)
# del ls[3]   #ls.remove(ls[3])
# print(ls)
# ls = ls[::-1]
# print(ls)
# ls.sort()
# print(ls)
# ls.sort(reverse=True)
# print(ls)
#practice03---------------------------------#
# ls1 = [1, 2, 3, 5, 6, 3, 2]
# ls2 = [2, 5 ,7 ,9]

# set1 = set(ls1)
# set2 = set(ls2)
# set_inter = set1.intersection(set2)

# print(set_inter)  #交集
# print(set1 & set2)

# print(set2-set_inter)   #差集与下行相同
# print(set2.difference(set1))    #set2中的跟set1不同的元素
# print(set2 - set1)

# print(set1.union(set2)) #并集
# print(set1 | set2)
#practice04------------------------------------------------#
IEEE = {'Python', 'C++', 'C', 'Java', 'C#'}
TIOBE = {'Python', 'C', 'Java', 'C++', 'VB.NET'}

print(IEEE | TIOBE)
print(IEEE & TIOBE)
print(IEEE - TIOBE)

print((IEEE - TIOBE) | (TIOBE - IEEE))
print((IEEE | TIOBE) - (IEEE & TIOBE))
print(IEEE.symmetric_difference(TIOBE))
print(IEEE ^ TIOBE) #对称差集
IEEE.symmetric_difference_update(TIOBE)
print(IEEE)
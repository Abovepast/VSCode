#-------------------point--------------------------#

#-------------------practise---------------------#
#Q1从一个列表或元组中找出奇数位对应的元素并返回一个新列表
# def fun01(args):
#     temp = []
#     for x in range(1, len(args), 2):
#         temp.append(args[x])
#     return temp


# ls = []
# ls1 = [1,2,3,4,5,6,7,8]
# ls = fun01(ls1)
# print(ls)

#--------------------------Q2------------------------------------------#
# def fun02(dit):
#     for key,val in dit.items():
#         if len(val)>2:
#             # val = val[:2] 不能直接赋值，要索引赋值
#             dit[key] = val[:2]
#     return dit


# dit = {'a':'asd','add':'d', '2dg':[2,4,5]}
# dit1 = {}

# dit1 = fun02(dit)
# print(dit1)

#--------------------Q3----------------------#
# def fun02(str):
#     num, char, space, other = 0, 0, 0, 0
#     for i in str:
#         if i.isdigit(): #是否为数字
#             num+=1
#         elif i.isalpha():   #是否为字母
#             char+=1
#         # elif i == ' ':
#         elif i.isspace():   #是否为空格
#             space+=1
#         else:
#             other+=1
#     # ls = [num, char, space, other]
#     # return ls
#     return num, char, space, other


# str1 = 'ac 123 Aacd &()汉字镍龘'
# print(fun02(str1))
# ls = fun02(str1)
# print(ls)

#----------------Q4----------------------------#
# def fun04(num, country='US'):
#     country = input('选择兑换的币种:(美元:USD, 欧元:EUR, 英镑:GBP)')
#     if(country=='USD'):
#         num = round(num/7.2009, 2)
#         print('美元兑换成功')
#     elif country=='EUR':
#         num = round(num/7.02285, 2)
#         print('欧元兑换成功')
#     elif country=='GBP':
#         num = round(num/8.126922, 2)
#         print('英镑兑换成功')
#     elif country=='CNY':
#         num=num
#     return num


# def fun05(amt, target='USD'):
#     rate = {'USD':7.2009, 'EUR':7.02285, 'GBP':8.126922}
#     for k,v in rate.items():
#         if target==k:
#             result = round(amt/v, 2)
#             print(f'{k}汇率计算成功')
#             break
#     return result


# num = float(input('请输入人民币金额：'));
# # print(fun04(num))


# target = input('何币种:(USD, EUR, GBP):')
# # target = upper(target)
# if (target != 'EUR') | (target !='GBP'):
#     target = 'USD'
# print(fun05(num, target))

#---------------Q5---------------------------------#
goods = [399, 4369, 539, 288, 109, 749, 235, 190, 99, 1000]
maxPrice = int(input("maxPrice:"))
minPrice = int(input('minPrice'))

ls=[]

for x in goods:
    # if(x>=minPrice & x<=maxPrice):
    if(minPrice<= x <=maxPrice):
        ls.append(x)

flag = input('升序or降序?(Y/y|N/n):')
if(flag=="Y") or (flag=='y'):
    ls.sort()
elif flag=='N' or flag=='n':
    ls.sort(reverse=True)

print(ls)
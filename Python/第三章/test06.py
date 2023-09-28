#------------------Q1密码加密--------------------------#
#%%
pwd = input('输入六位数字：')
ls = ""
sum = 0
for i in pwd:
    sum += int(ord(i))
    ls += str(ord(i))

scurePassword = int(ls[::-1]) + sum
print(scurePassword)
#------------------Q2逢七拍手--------------------#

#%%
for i in range(1,101):
    if(str(i).find('7')!=-1):
        print('*',end=',')
    elif(i%7==0):
        print('*',end=',')
    elif(i==100):
        print(i)
    else:
        print(i, end=',')

#------------------Q3登录系统账号检测--------------------------#
# %%
df_user = 'admin'
df_pwd = '123'
times = 0
while(times<3):
    username = input("账号:")
    password = input("密码:")
    times += 1
    if(username==df_user and password==df_pwd):
        print('登录成功！')
        break
    else:
        if(times==3):
            print('你的三次机会已用完，账户已锁定！')
            break
        print(f'账号或密码错误!你还剩{3-times}次机会')
#
#------------------------Q4九九乘法表---------------------------#
# %%
for i in range(1,10):
    for j in range(1,10):
        if(i>=j):
            print(f'{j}x{i}={i*j}', end='\t')
    print()
# %%

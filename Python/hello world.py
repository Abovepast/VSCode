#question 1
num_ = num = int(input("输入一个3位数："))
sum = 0
while num:
    sum+=(num%10)**3
    num//=10
if sum==num_:
    print("是")
else:
    print("不是")


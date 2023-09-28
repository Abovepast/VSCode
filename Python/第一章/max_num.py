#question 2
a,b,c=map(int,input("请输入三个数：").split())
if a>b:
    if(a>c):
        print(a)
    else:
        print(c)
else:
    if(b>c):
        print(b)
    else:
        print(c)
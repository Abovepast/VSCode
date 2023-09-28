#question 3
x,y,z = map(int,input("请输入三个数x,y,z:").split())
if x+y>z and x+z>y and y+z>x:
    q = (x+y+z)/2
    S = (q*(q-x)*(q-y)*(q-z))**0.5
    print(f"三角形的面积S为:{S}")
else:
    print("无法构成三角形")
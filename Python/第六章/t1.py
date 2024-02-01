#f = open('t.txt', 'w', encoding='UTF-8')
#f.write('你好，hello world!')
#f.close()
f = open('t.txt', 'r', encoding='UTF-8')
#data = f.readlines()
#print(data)
data = f.readlines()
for i,item in enumerate(data):
    print(f'{i}:{item}', end='')

f.close()

#a,a+附加写
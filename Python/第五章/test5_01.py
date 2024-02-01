# class Person:
#     def __init__(self, name='null', weight='null') -> None:
#         self.name = name
#         self.weight = weight
    

#     def __str__(self):
#         return f'name:{self.name}, weight:{self.weight}'
    

#     def run(self):
#         self.weight -= 0.5
#         print(f'{self.name}爱跑步，体重减轻')
#         pass


#     def eat(self):
#         self.weight += 1
#         print(f'{self.name}爱吃，体重增加')
#         pass


# xiaoming = Person('小明', 40)
# print(xiaoming)

# xiaoming.run()
# xiaoming.eat()
# print(xiaoming)
#------------士兵突袭-----------------
class Gun(object):
    def __init__(self, modle='null', bullet_number=0):
        self.modle = modle
        self.bullet_number = bullet_number


    def addbullet(self, count):
        self.bullet_number += count


    def shoot(self):
        if self.bullet_number<=0:
            print('没有子弹')
            return
        else:
            self.bullet_number -=1
            print(f'磅！,剩余子弹{self.bullet_number}')
            
            
class Soldier:
    def __init__(self, name, gun):
        self.name = name
        self.gun = gun


    def fire(self):
        print('射击')
        self.gun.shoot()

    
    def power(self):
        print(f'{self.name}调用power方法')


ak47 = Gun('ak47', 60)
dengzijie = Soldier('dengzijie', ak47)

ak47.addbullet(10)
dengzijie.fire()
dengzijie.fire()
dengzijie.fire()
dengzijie.fire()


class Ak47(Gun):
    def __init__(self, modle='null', bullet_number=0, powerM=0):
        super().__init__(modle, bullet_number)
        self.powerM = powerM
    def power(self):
        print(f'{self.modle}power:{self.powerM}:')

ak1 = Ak47('ak47-plus', 120, 12)
ak1.power()
dengzijie.power()

class SeinerSoldier(Soldier):
    def __init__(self, name, gun):
        super().__init__(name, gun)

    #可以不写，但写了便于维护
    def fire(self):
        print('调用父类fire()方法')
        return super().fire()
    
#super不是函数是类，是个type
        

s_Solider = SeinerSoldier('Any', ak1)
#调用父类方法
s_Solider.fire()

#dfs往上找父类，遇到同级（共父类）就bfs,(MRO)
class Obj(Gun, Soldier):
    def selfPrint(self):
        pass

#返回搜索顺序
print(Obj.mro())

# # GDBA
# GDAB
# # FCBDAA
# FCBDA

print(isinstance(Gun, object))
print(isinstance(Obj, Gun))
print(isinstance(SeinerSoldier, Soldier))



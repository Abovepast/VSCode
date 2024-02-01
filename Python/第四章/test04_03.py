# class Student:
#     #构造方法
#     def __init__(self) -> None:
#         self.name = 'Unknown_init'


#     #静态方法
#     @staticmethod
#     def s_info(name, add):
#         print('调用静态方法')


#     name = 'Unknown'


#     def setName(self, newname):
#         self.name = newname


#     def printName(self):
#         print("姓名："+self.name)


#     @classmethod
#     def info(cls):
#         print("调用了类方法")


# Student.name = '未知'
# stu = Student()
# print(stu.name)

# # stu.name = '小明'
# stu.setName('小明')
# stu.printName()

# Student.printName(stu)
# class Person:
#     def __init__(self, name='未知') -> None:
#         self.name = name;

#     def printPerson(self):
#         print("名字:"+self.name);

#     def __del__(self):
#         print('对象已经删除')
    
#     def __str__(self):
#         text = f"这厮是{self.name}"
#         return text


# s1 = Person('小白')
# s1.printPerson()


# class Box:
#     def __init__(self, long = 0, width = 0, height = 0) -> None:
#         self.long = long
#         self.width = width
#         self.height = height

    
#     def volumn(self):
#         print(self.long*self.width*self.height)


# b1 = Box()
# b1.volumn()

# class Restaurant:
#     def __init__(self, restaurant_name = 'null', cuisine_type = 'null', number_served = 0):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = number_served

    
#     def describe_restaurant(self):
#         print(f'1.{self.restaurant_name}\n2.{self.cuisine_type.title()}')   #title()首字母大写

    
#     def open_restaurant(self):
#         print('The restaurent is open')

    
#     def set_number_served(self, number):
#         self.number_served = number
#         print(f'当前有{self.number_served}人就餐')


#     def increment_number_served(self, number):
#         self.number_served += number
#         print(f'当前有{self.number_served}人就餐')


# r0 = Restaurant('A', 'tom')
# print(r0.restaurant_name, r0.cuisine_type)
# r0.describe_restaurant()
# r0.open_restaurant()

# print(f'当前有{r0.number_served}人就餐')
# r0.set_number_served(3)
# r0.increment_number_served(2)


class User:
    def __init__(self, first_name = 'null', last_name='null', age = '', sex = '', login_attempts=0) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attempts = login_attempts


    def describe_user(self):
        print('first_name:',self.first_name)
        print('last_name:',self.last_name)
        print('age:',self.age)
        print('sex:',self.age)


    def greet_user(self):
        print(f'你好，{self.first_name} {self.last_name}！')


    def increment_login_attempts(self):
        self.login_attempts += 1;
        print(f'login_attempts={self.login_attempts}')

    
    def reset_login_attempts(self):
        self.login_attempts = 0;
        print(f'login_attempts={self.login_attempts}')


u_one = User('Tom', 'Jery', 18, 'meal')
u_two = User('Bob', 'Goo', 19, 'femeal')

u_one.describe_user()
u_one.greet_user()
u_two.describe_user()
u_two.greet_user()

u_one.increment_login_attempts();
u_one.reset_login_attempts()
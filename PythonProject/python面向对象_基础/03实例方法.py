#在类中定义实例方法时，定义语法与之前学习的函数定义的方式是一样的
'''
#定义类
class 类名:
    def __init__(self):
        self.属性名=属性值
    def 方法名1(self,形参名):
        .....
    def 方法名2(self,形参名):
        .....
#创建对象
对象名=类名(参数列表)
对象名.方法名(实参)
'''

class Car:
    def __init__(self,brand,name,price):
        self.brand=brand
        self.name=name
        self.price=price

    def running(self):#汽车的运行功能
        print(f"{self.brand} {self.name}正在高速行驶")
    def total_price(self,discount,rate = 0.2):#汽车的价格计算方法
        return self.price*discount+self.price*rate

c1 = Car("BMW","X5",500000)
total_cost = c1.total_price(discount=0.9)
print(total_cost)

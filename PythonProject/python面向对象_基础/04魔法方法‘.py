'''
1.魔法方法指的就是python中提供的以双下划线开头和结尾的特殊方法，用于定义类的特殊行为，比如__init__
2.魔法方法是不需要我们手动去调用的，Python会在合适的时候自动调用。
'''

'''
魔法方法-------------------描述
__init__   --------->  初始化方法
__str__    --------->  字符串表示的方法
__eq__     --------->  比较两个对象是否相等（equal）
__lt__ , __le__ , __gt__ , __ge__      支持比较两个对象的大小
'''

class Car:
    def __init__(self,brand,name,price):
        self.brand = brand
        self.name = name
        self.price = price
    def running(self):
        print(f"{self.brand} {self.name}正在高速行驶")
    def __str__(self):
        return f"{self.brand},{self.name},{self.price}"
    def __eq__(self,other):
        return self.price == other.price and self.brand == other.brand and self.name == other.name
    def __lt__(self,other):
        return self.price < other.price

c1 = Car("bmw","X5",500000)
print(c1)
c2 = Car("bmw","X5",500000)
print(c2)

print(c1 == c2)
print(c1<c2)
print(c1>c2)






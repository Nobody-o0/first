#属性分为实例属性和类属性
'''
实例属性：是属于每个对象的具体属性，每个对象都是独立的。（每个对象特有的数据）
类属性：类属性是类本身的属性，所有实例共享的（所有对象共享的数据或配置）
通过实例查找属性时，会先查找实例属性，当实例属性不存在时，再查找类属性
'''

class Car:
    weels = 4#这就是类属性
    tax_rate =0.5#这就是类属性
    def __init__(self,brand,name,price,weels):
        self.brand=brand
        self.name=name
        self.price=price
        self.weels=weels

    def running(self):
        print(f"{self.brand} {self.name}正在高速行驶。。。")

c1 = Car("BYD","汉","180000",5)

c2 = Car("Tesla","model Y",260000,4)

print(c1.brand,c1.name,c1.price,c1.weels)#同时存在相同的类属性和实例属性时，优先检索实例属性的值，如这里的weels
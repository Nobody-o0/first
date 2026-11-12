#封装
#封装就是把数据（属性）和操作数据的函数（方法）捆绑在一起，形成一个独立的单元（类），并隐藏内部的实现细节（也就是私有属性，私有方法），
# 只对外暴露必要的功能（公共属性，公共方法）

#之前写的公共的类：
'''
class Car:
    wheel = 4
    tax_rate = 0.1

    def __init__(self,c_color,c_brand,c_name):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name

    def start(self):
        print(f"{self.brand} {self.name}正在启动")


    def stop(self):
        print(f"{self.brand} {self.name}停止行驶")

'''

#如果想将其中的一些属性和方法设置为私有属性和私有方法，可以在对应的属性和方法前面加上双下划线

class Car:
    #类属性（对所有实例对象共享）
    wheel = 4
    tax_rate = 0.1

    def __init__(self,color,brand,name,owner):
        #实例属性
        self.color = color
        self.brand = brand
        self.name = name
        self.__owner = owner    #私有属性

    def start(self):#启动
        print(f"{self.brand} {self.name}正在启动")


    def stop(self):#停止
        print(f"{self.brand} {self.name}停止行驶")

    def __control_fuel(self):#燃油分配          #私有方法
        print(f'{self.brand} {self.name}控制燃油分配')

#私有：私有的属性和方法只能在类的内部使用，Python当中并没有真正的私有机制，约定在私有属性名和方法名前加__(两个下划线)。


if __name__ == '__main__':
    car = Car("dark","AUDI","A6L","owner")
    print(car.color)
    print(car.brand)
    print(car.name)
 #   print(car.__owner)#输出不了，他是私有的

    car.start()
    car.stop()
  #  car.__control_fuel()#这个方法也无法直接使用，因为是私有的

#但正如一开始说的，没有真实的私有，我们可以通过下面的方法不经对象内部同意来获取调用私有属性和方法

    print(car._Car__owner)
    car._Car__control_fuel()
















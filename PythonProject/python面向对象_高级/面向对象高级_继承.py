#继承
#车(Car)分为油车(FuelCar)和电车(ElectricCar),他们都具备车(Car)的基本属性和方法，但又有各自独特的属性和方法，这种情况就要用到继承
class Car(object):
    wheel = 4
    def __init__(self,color,brand,model):
        self.color = color
        self.brand = brand
        self.model = model

    def start(self):#启动
        print(f"{self.color},{self.brand},{self.model}正在启动")

    def run(self):
        print(f"{self.color},{self.brand},{self.model}正在行驶")

    def stop(self):
        print(f"{self.color},{self.brand},{self.model}停止行驶")


#油车继承
class FuelCar(Car):#通过在括号内写出要继承的类来实现继承，从而提高代码的复用率
    pass

#电车继承
class ElectricCar(Car):
    pass

if __name__ == '__main__':
    c1=FuelCar("黑色","bengchi","e300")
    c2=ElectricCar("红色","xiaomi","su7")
    c1.start()
    c2.start()
    c1.run()
    c2.run()
    c1.stop()
    c2.stop()

#值得注意的是，子类继承父类，并非将父类所有的属性和方法全部继承了下来，父类私有的属性和方法是不会被继承的



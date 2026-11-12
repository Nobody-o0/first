#多态：多态是指同一个方法具有不同的形态，行为，表现。
#例如：

#定义一个父类Car
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

    def charge(self):#这个补能的方法并不通用
        print(f"{self.color},{self.brand},{self.model}正在补能")

#再分别定义两个子类FuelCar和ElectricCar
class FuelCar(Car):
    def charge(self):
        super().charge()
        print(f"{self.color}{self.brand}{self.model}正在加油")


class ElectricCar(Car):
    def charge(self):
        super().charge()
        print(f"{self.color}{self.brand}{self.model}正在充电")

#此时已经有三个不同形态的charge()方法

#此时我定义一个方法handle_Car(car:Car),并在当中调用charge方法

def handle_Car(car: Car):
    car.charge()
#可以看到此时handle_Car()中调用了car.charge()方法，但charge有三个版本的方法，这究竟会是哪个方法会生效呢

#我们传入不同的不同的对象来调用这个函数
handle_Car(FuelCar("白色","bwm","x5"))
handle_Car(ElectricCar("黑色","xiaomi","su7"))

#分别传入了不同的子类，在运行结果可以看到，handle_Car这个函数里的car.charge()方法它是根据传入子类的不同来执行对应的子类重写的方法的
#这种同一调用语句，传入对象不同，触发行为不同的特性，就被称为多态
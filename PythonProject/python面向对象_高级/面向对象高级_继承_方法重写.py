#当父类中现有的某个方法不满足需求，可以在子类中重新定义父类中已有的方法（方法名相同），从而用子类的实现替换父类的实现

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



class FuelCar(Car):
    def charge(self):
        super().charge()
        #注意，如果在重写父类方法的时候需要调用到父类的方法时，可以通过父类名.方法名(self)/super().方法名  的方式来调用
        print(f"{self.color}{self.brand}{self.model}正在加油")


class ElectricCar(Car):#电车需要重写补能的方法
    def charge(self):
        super().charge()
        print(f"{self.color}{self.brand}{self.model}正在充电")


if __name__ == '__main__':
    c1 = FuelCar("红色","宝马","X5")
    c2 = ElectricCar("黑色","岚图","追光S")
    c1.start()
    c2.start()
    c1.stop()
    c2.stop()
    c1.charge()
    c2.charge()


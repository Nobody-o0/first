#多继承：一个子类继承多个父类

class Car(object):
    wheel = 4
    def __init__(self,color,brand,model,owner):
        self.color = color
        self.brand = brand
        self.model = model
        self.__owner = owner

    def start(self):#启动
        print(f"{self.color},{self.brand},{self.model}正在启动")

    def run(self):
        print(f"{self.color},{self.brand},{self.model}正在行驶")

    def stop(self):
        print(f"{self.color},{self.brand},{self.model}停止行驶")

    def get_owner(self):
        return self.__owner[0:1]+"**"

    def charge(self):#这个补能的方法并不通用
        print(f"{self.color},{self.brand},{self.model}正在补能")


class HuaweiAiDriving:
    def __init__(self,version = "V1.0"):
        self.version = version

    def run(self):
        print(f"使用华为ai智能驾驶系统{self.version}正在行驶。。。")


#现在要定义一个“问界”类的汽车，他同时要继承Car类和HuaweiAiDriving类

class WenjieCar(Car,HuaweiAiDriving):#这种写法就可以同时继承两个父类的属性和方法
    def __init__(self,color,brand,model,owner,version = "V1.0"):
        super().__init__(color,brand,model,owner)
        HuaweiAiDriving.__init__(self,version)
 

#注意：MRO(方法解析顺序)
#当一个类继承了多个父类的时候，默认优先使用第一个父类中的同名属性和方法，可以使用 类名.__mro__属性 或 类名.mro()方法来查看调用顺序


if __name__ == "__main__":
    car = WenjieCar("heise","Wenjie","M9","MR.Yi")
    print(WenjieCar.__mro__)
    print(WenjieCar.mro())
    print(car.__dict__)
    car.run()
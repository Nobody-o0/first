class Duck():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def swimming(self):#游泳技能
        print(f"{self.age}岁的{self.name}正在游泳")

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def swimming(self):
        print(f'{self.age}岁的{self.name}正在游泳')


class Pig:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self):
        print(f'{self.age}岁的{self.name}正在游泳')

#上面定义了三个类，他们之间没有继承关系，但是都有一个相同的方法swimming

def go_swimming(duck:Duck):#这里也能看出括号内的类型标注并不是强制约束，只是为了提高代码可读性而写上的东西
    duck.swimming()

#测试代码
if __name__ == '__main__':
    go_swimming(Dog("旺财",4))
    go_swimming(Duck("唐老鸭","5"))
    go_swimming(Pig("佩奇","1"))

#可以看到在函数go_swimming()中，已经标注了类型是Duck，但输入其它类的对象依然能成功调用各自类型对应的方法名，这也是多态的一种体现
#这种多态被称之为鸭子多态



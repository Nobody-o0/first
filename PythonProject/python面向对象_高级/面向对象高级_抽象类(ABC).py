#抽象类：是一中只能被被继承，不能直接实例化的类，作用是规定子类必须要实现某些方法，强制子类必须遵守统一的代码规范
#Python中的抽象类，需要继承abc模块中的ABC类---->ABC:Abstract Base Class(抽象基类)

from abc import ABC, abstractmethod

class Member(ABC):#把这个类定义为继承ABC的类
    def __init__(self,member_id,name,password):
        self.member_id = member_id
        self.name = name
        self.password = password

    @abstractmethod#在需要强制让子类实现的方法名上方加上这个装饰器，表示这个方法是个抽象的方法，要求其必须在子类中实现
    def get_max_books(self):
        pass

class NormalMember(Member):
    def get_max_books(self):#如果没实现这个方法在实例化此对象时会报错
        return 3

class VipMember(Member):
    def __init__(self,member_id,name,password,vip_level):
        super().__init__(member_id,name,password)
        self.vip_level = vip_level
    def get_max_books(self):
        return 6 + self.vip_level


if __name__ == '__main__':
    m = NormalMember("N001","qiangseng","123456")
    print(m)
    print(m.get_max_books())


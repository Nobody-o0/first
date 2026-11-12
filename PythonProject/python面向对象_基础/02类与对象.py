#类的定义,定义一个类要遵循以下格式


#定义类---->这种方法不推荐，动态的为对象添加属性（降低代码的可读性，加大联合开发的难度）
'''
class Car:
    pass


#创建对象
'''
'''
对象名=类名（）
对象名.属性名1=属性值1
对象名.属性名2=属性名2
'''
'''
xiaomi = Car()
#动态的为对象添加属性
xiaomi.color = 'red'
xiaomi.speed = 'medium'
xiaomi.price =249999
print(xiaomi)
print(xiaomi.__dict__)

#__dict__是Python中用户自定义类实例的一个特殊属性，用于以字典形式存储对象的属性。

#类名的命名规范：遵循大驼峰法，每个单词的首字母全大写，单词之间不加分隔符，比如：UserInfo,UserAccount


#规范的定义类的方法
'''
'''
calss 类名
    def __init__(self,参数列表):
        self.属性名=参数值
        self.属性名=参数值
#说明：定义在类外面的称之为函数，定义在类中的函数称之为方法
#__init__:初始化方法，对象创建后自动调用，主要用于设置对象的初始状态，（设置对象属性）
'''

#定义类
class NewCar:
    #self:第一个参数，表示当前所创建出来的实例对象
    def __init__(self,c_color,c_brand,c_name,c_price):
        self.color=c_color
        self.brand=c_brand
        self.name=c_name
        self.price=c_price

#创建对象
Xiaomi = NewCar("red","xiaomi","su7",249999)
print(Xiaomi.__dict__)



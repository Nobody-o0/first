#普通参数：数字，布尔，字符串，列表，元组，集合，字典等


#特殊参数：函数
def add(x,y):
    return x+y

def substract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

def calc(x,y,oper):
    '''
    输入的数字和要进行的运算方法，从而实现计算器的功能
    :param x:参数1
    :param y:参数2
    :param oper:想要进行的运算方式
    :return:返回运算的结果
    '''
    return oper(x,y)

resullt = calc(1,2,add)#这里就是直接用add传递函数add中封装的逻辑
print(resullt)

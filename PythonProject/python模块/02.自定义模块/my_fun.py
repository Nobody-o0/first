#自定义一个功能

#常量（不会发生变化的数据；常量名字全大写）
PI=3.14
NAME = "Nobody"

#函数
def log_separator1():
    '''
    输出一行由-号组成的分隔线
    :return:无
    '''
    print("-"*30)


def log_separator2():
    '''
    输出一行由+号组成的分隔线
    :return: 无
    '''
    print("+"*30)


#测试函数
#__name__ : python中的内置变量，表示当前模块的名字（直接运行当前模块，__name__的值为"__main__";当该模块被导入时，__name__的值就是模块名）
if __name__=="__main__":#这样写测试代码就不会在模块被引用时自动运行测试代码了
    log_separator1()


#__all__是一个特殊的模块级的特殊变量，用于指定from 模块名 import* 时会导入哪些功能（*通配了哪些功能）
__all__=["log_separator1","log_separator2"]
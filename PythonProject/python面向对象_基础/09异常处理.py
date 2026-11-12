#异常的传递
'''
异常传递就是异常在函数调用中层层上报的过程，知道有人处理它，或者程序崩溃
'''
#例如
def fun1():
    print("fun1 is running")
    fun2()
def fun2():
    print("fun2 is running")
    fun3()
def fun3():
    print("fun3 is running")
    print(my_color)

if __name__ == '__main__':
    try:
        fun1()
    except:
        print("程序出错了，待会再试试吧~")



'''
在上面的函数中，有以下动作
if __name__ == '__main__'
   |        ↑    
   |(调用)   |(bug传递)
   ↓        |
-----fun1()-----
   |        ↑
   |(调用)   |(bug传递)
   ↓        |
-----fun2()-----
   |        ↑
   |(调用)   |(bug传递)
   ↓        |
-----fun3()-----

bug从方法内部传递到主程序之后依然没有被处理的话就会处罚程序的的中断
在bug上报传递的过程中，任何位置处理掉这个bug都可以让程序继续运行，不过最佳的处理位置是在最外层的主程序里统一进行捕获处理
'''




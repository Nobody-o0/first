#分为  全局变量  和  局部变量
#全局变量：函数之外定义的变量，在全局都可以使用和访问
#局部变量：函数内部定义的变量，只能在函数内部访问，外部无法访问

#global 关键字，可以在函数中修改全局变量
num = 1
def change():
    global num
    num = num + 1
    return num
change()
print(num)
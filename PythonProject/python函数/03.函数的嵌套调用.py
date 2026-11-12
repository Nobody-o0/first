#嵌套调用指的是在一个函数中，又调用了另外一个函数
#函数调用遵循栈结构，最后被调用的函数最先返回LIFO（Last In First Out，先进后出）
def function_a():
    print("function_a before")
    function_b()
    print("function_a after")
def function_b():
    print("function_b before")
    function_c()
    print("function_b after")
def function_c():
    print("function_c before")

function_a()
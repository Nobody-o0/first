#传参方式
#1，位置传参：调用函数时根据函数定义时的位置来传递参数
def reg_stu1(name,age,height,weight):
    print(f"注册成功姓名{name},年龄{age},身高{height},体重{weight}")
#调用函数
reg_stu1("liru",23,37,46)

#2.关键字传参：调用函数时以函数定义时的形参名作为关键字，以“键=值”的形式来传递参数（不要求顺序）

#调用函数：
reg_stu1(name="lihua",age=20,height=30,weight=50)

#注意，如果位置参数和关键字参数混用，关键字参数必须在位置参数之后（关键字参数之间，没有顺序要求）

#调用函数：
reg_stu1("lihuang",26,height=50,weight=56)
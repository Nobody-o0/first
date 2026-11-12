#在定义函数的时候，直接用关键字传参的方式给形参赋予一个默认值
def reg_stu(name,age,height,weight=100):
    print(f"注册成功姓名{name},年龄{age},身高{height},体重{weight}")
    return {"name":name,"age":age,"height":height,"weight":weight}
reg_stu(name="lihua",age=20,height=100)
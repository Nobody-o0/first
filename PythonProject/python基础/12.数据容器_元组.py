#元组：tuple,不可修改，只能查询
#可重复，有序，不可修改
#格式：元组名称= （元素一，元素二，）
#方法：count():统计某元素在元组中出现的次数
#index（）：查找某个元素在元组中的索引位置

#定义
t1 = (10,20,30,40)
print(t1)
print(type(t1))

#索引访问
print(t1[0])

#元组解包：
#1.基础解包
a,b,c,d,= t1
print(a)
print(b)
print(c)
print(d)

#2.（*）扩展解包,*表示收集剩余的所有元素，这样我们就可以先去收集其他的元素，剩余的归纳到*标注的容器里就好了
t2=(1,2,3,4,5)
x,*y,z = t2
print(x,end=" ")
print(y,end=" ")
print(z,)
o,*s = t2
print(o,end=" ")
print(s,end=" ")
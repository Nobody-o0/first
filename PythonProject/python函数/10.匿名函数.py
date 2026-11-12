#匿名函数指的即是没有名称的函数，需要通过lambda表达式来声明函数，可以简化简单函数的编写（单行表达式）

#在命名函数中，我们都采取def方法来定义函数

#定义匿名函数：lambda语法格式
'''
lambda 参数列表 :函数体   #只能是单行的简单逻辑
如：
'''
lambda : print("好好学习呀")#和命名函数一样，参数列表可以为空

lambda a,b:a+b#计算a+b的值

#匿名函数的用法

for_you = lambda : print("好好学习呀")
add = lambda a,b:a+b


for_you()
print(add(100,200))

#在函数逻辑比较简单（单行表达式）且只在一个地方使用的时候，可以考虑使用匿名函数，简化书写（通常作为高阶函数的参数使用）


#列表里sort方法如何使用自定义的排序方式


#1.sort()方法的默认排序：按照字符的字母在字母表的顺序排序
data_list = ["c++","c","python","jack","php","java","go","javascript","rust"]
data_list.sort()#这里产生的排序是通过字母的顺序来排，如首字母重复，则比第二位字母，以此类推
print(data_list)


#2，但我们想要按照字符的字符长度进行排序;sort()函数的默认设置是sort(...,key=none,reverse=False),
#其中key就是一个函数，他会作用于列表中的每一个数据，控制列表中的数据如何排序

data_list.sort(key = lambda item :len(item))#这里使用匿名函数来充当方法中的参数是常用用法，这个匿名函数的返回值为所有
#参数的长度，以他作为key
print(data_list)

#sort()方法的reverse参数的作用是反转，上面我们使用的是字符串长度从小到大的顺序进行排序，将reverse设置成True就可以反转顺序

data_list.sort(key = lambda item :len(item),reverse = True)
print(data_list)



#在函数逻辑简单，且只在一个地方调用，那就使用匿名函数（通常作为高阶函数的参数）
#在函数逻辑复杂，且需要多步操作，需要多个地方重复使用或需要加文档说明的情况下，使用命名函数

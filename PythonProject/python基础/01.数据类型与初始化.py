# #需求,python是动态类型语言，变量存储的变量类型是可以改变的
# a,b = 2,1
# print(a)
# a = "hello"
# print(a)
# # 基础播放量，每月新增播放量，求未来一月总播放量
# base_num,attend_num = 20.5,10 #一条语句可以定义多个变量，也可以连续赋值
# print("未来一个月的播放总量：",base_num + attend_num )#输出多项，逗号分隔
a,b =1,2
a,b=b,a#可以通过这个办法让a，b的值互相交换
print(a,b)
print(type(a))#type()方法可以查看变量和数据的类型
print(isinstance(a,int))#isinstance()方法可以判断数据类型是否为指定类型，输出的值是bool值
print(isinstance(a,bool))

#定义字符串→it's very good
s1 = 'it\'s very good'#用单引号定义字符串时，如果字符串本身含有单引号，容易被认定为语法错误，此时需要用转义字符\
#转义字符有\n:换行,  \t:缩进,  \':单引号,  \":双引号 等等
print(s1)

#字符串拼接
#1，定义的时候直接拼接,两种拼接方法
my_name="易"+"明磊"
print(my_name)
your_name="李""华"
print(your_name)
#2，两个字符串变量进行拼接,用+号直接拼接
print("我们的名字是"+my_name+your_name)
#3拼接字符串变量和非字符串变量时,要先将非字符串变量转换成字符串变量才能用+号拼接
age=21
print(my_name+"和"+your_name+"都是"+str(age)+"岁")#要用str()方法来转换age的数据类型
#其他类型转换为int类型：int（）
#其他类型转换为float类型：float()......以此类推

# 字符串格式化：
# 1.通过%占位符的形式完成字符串和变量的快速拼接
str1 = "人生苦短"
str2 = "我用python"
print("我说过：%s,%s"%(str1,str2))#%表示我要占位，s表示将变量转为字符串放入占位的位置
# 2.通过f"内容{变量/表达式}”
print(f"我说过：{str1},{str2}")

#input()方法可以获取到用户在键盘输出的数据,获得的数据都是字符串类型
User_names = input（"请输入你的用户名"）
print(User_names)
print(type(User_names))


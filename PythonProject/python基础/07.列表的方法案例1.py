#列表方法案例
#合并两个列表，并对合并的结果进行去重处理

#1.合并
list1=[1,2,3,4,5,6]
list2=[5,6,7,8,9,10]
list1.extend(list2)
print(list1)

#2.去重
new_list=[]
for num  in list1:
    if num not in new_list:#in方法可以判断列表中是否有该元素
        new_list.append(num)
print(new_list)


#当然，想要实现合并的操作还有更简单的办法：解包,"+"号
#解包：将列表这一类容器解开成一个个独立的元素
some_list1=[1,2,3,4,5,6]
some_list2=[5,6,7,8,9,10]
all_list=[*some_list1,*some_list2]
print("all_list",all_list)

the_list=some_list1+some_list2#用加号更是简单
print("the_list",the_list)
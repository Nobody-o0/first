#案例1：生成1-20之间的平方列表
#方法一，传统方式
num_list1=[]
for i in range(1,21):
    num_list1.append(i**2)
print("num_list1",num_list1)

#方法二，列表推导式---->按照一定的规则快速生成一个列表的方法-->语法格式1：[要插入的值 for i in 序列/列表]
num_list2=[i**2 for i in range(1,21)]
print("num_list2",num_list2)


#案例2：从一个数字序列中提取出所有偶数，并计算其平方，组成一个新的列表
#列表推导式--->语法格式2：[要插入的值 for i in 序列/列表 if 条件]
new_list3 = [12,32,45,77,80,92,33,57,97,110,122]
new_list4 = [i**2 for i in new_list3 if i%2==0]
print("new_list4",new_list4)





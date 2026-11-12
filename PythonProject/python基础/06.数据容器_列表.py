#数据容器类型:列表,字符串,元组,集合,字典
#1.列表（list）
'''
s = [1,"字符串",3,False,5,6,7,8]#创建一个列表（可以存储不同类型的数据类型）


#访问列表元素
#索引
print(s[0])
print(s[-1])


#修改列表元素
s[0]="修改"
print(s[0])

#删除列表元素
del s[0]
print(s[0])



#列表的切片
some=s[0:3:1]#从第0位截取到第3位，包含起始索引，不包括结束索引
print(some)

num=[0,1,2,3,4,5,6,7]
#列表的常用方法
#添加列表元素,
#有append()：在列表的尾部添加元素,extend()：在列表的尾部添加元素,insert()：在列表的指定索引前插入该元素
num.append(8)
print(num)
num.extend([9,10,11])
print(num)
num.insert(0,0)
print(num)

#删除元素:
# remove()：移除列表中第一个匹配到的值。 pop():删除列表指定索引位置的元素（未指定默认删除最后一个）
num.remove(0)
print(num)
num.pop(0)
print(num)


#sort():对列表元素进行排序，reverse():反转列表元素
num.reverse()
print(num)
num.sort()
print(num)

'''




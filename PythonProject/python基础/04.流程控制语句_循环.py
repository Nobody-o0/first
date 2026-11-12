#while循环是通过条件表达式来控制是否要进行下一次循环的。
#用while循环打印10次"生活，易如反掌"
'''
i = 0
while i<10:
    print("生活，易如反掌")
    i += 1
else:
    print(i)
'''

'''
#用while循环计算1——100之间所有偶数累加之和
total = 0 #记录累加之和
i=1
while i<100:
    if i%2==0:
        total = total + i
    i += 1
print(f"1——100之间的偶数累加值和为{total}")
'''


#for循环，本质是一种轮询遍历机制，对一批内容进行逐个处理。
#定义要遍历的字符串
'''
msg = input("输入要遍历的字符串")
for c in msg:
    print(c)
else:
    print("遍历结束")
'''

#用for来完成计算1——100的奇数之和
#获得1——100的数据列表需要用到range语句一共有3种用法
'''
用法一：range（end）:获取一个从零开始，到end结束的数字序列（不包含end本身）
用法二:range(start,end):获取一个从start开始，到end结束的数字序列（不包含end本身）
用法三：range（start,end,step）:获取一个从start开始，到end结束，以step为间隔的数字序列（不包含end本身）
'''
num_list = range(1,101)
total = 0          #累加和
for num in num_list:
    if num % 2 == 1:
        total += num
print(total)

#用range的第三种方法来简化
num_list2 = range(1,101,2)
total2 = 0
for num in num_list2:
        total2 += num
print(total2)


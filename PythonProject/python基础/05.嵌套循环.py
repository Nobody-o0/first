#使用嵌套循环：根据输入的长方形的长度为m，宽度为n，打印一个长方形
'''
m = int(input("输入长"))
m_list = range(1,m+1)
n = int(input("输入宽"))
n_list = range(1,n+1)
for i in n_list:
    for j in m_list:
        print("*",end="")#print自带换行效果。需要在后面加end=none来防止换行
    print()#print()不输出任何东西时，就是一次换行
'''

'''
#用嵌套循环打印九九乘法表
m_list= range(1,10)
n_list = range(1,10)
for i in range(1,10) :
    for j in range(1,i+1):
            print(f"{j}x{i}={j*i}",end="\t")
    print()
'''
'''
#一共三个账户，188/666,199/777.100/888
while True:
    user_name = int(input("请输入你的账户名"))
    password = int(input("请输入你的密码"))
    match(user_name):
        case 188:
            if password==666:
                print("登录成功")
                break
            else:
                print("登陆失败，账号和密码错误，请重新输入")
        case 199:
            if password==777:
                print("登录成功")
                break
            else:
                print("登陆失败，账号和密码错误，请重新输入")
        case 100 :
            if password==888:
                print("登录成功")
                break
            else:
                print("登陆失败，账号和密码错误，请重新输入")
        case _ :
            print("登陆失败，账号和密码错误，请重新输入")
            
'''
#continue语句与break不同，continue是中断此次循环进入下一次循环，break是跳出循环，不再执行循环而是进入之后的流程

#猜数字游戏
import random   #引入random模块
random_num = random.randint(1,100)#生成一个1到100的随机数
while True :
    user_num = int(input("输入你猜的数字"))
    if user_num == random_num :
        print("恭喜你猜对了")
        break
    elif user_num > random_num :
        print("你猜的数字太大了")
        continue
    elif user_num < random_num :
        print("你猜的数字太小了")
        continue
print("游戏结束了")




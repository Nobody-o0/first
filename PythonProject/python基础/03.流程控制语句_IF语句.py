#1.条件判断if
# score = input("输入你的分数")
# if int(score) >= 680:
#     print("欢迎你来清华读书")
#
# User_name = input("请输入你的用户名")
# Pass_word = input("请输入你的密码")
# if int(User_name) == 1888 and int(Pass_word) == 10086:
#     print("登录成功")
# else:
#     print("登陆失败，账号或密码不正确")

# sign_year = int(input("请输入需要判断的年份"))
# if (sign_year)%100==0:
#     if (sign_year)%400==0:
#         print("%s是闰年"%sign_year)
#     else:
#         print("%s是平年"%sign_year)
# else:
#     if sign_year%4==0:
#         print("%s是闰年"%sign_year)
#     else:
#         print("%s是平年"%sign_year)

# Num = int(input("输入你想要判断的数字"))
# if Num == 0 :
#     print("%d是0"%Num)
# elif Num > 0:
#     print("%d是正数"%Num)
# else:
#     print("%d是负数"%Num)

#判断三条边能否构成三角形，并且判定是等边，等腰还是普通三角形
# a = int(input("输入第一条边长"))
# b = int(input("输入第二条边长"))
# c = int(input("输入第三条边长"))
#
# if a+b>c and b+c>a and b+c>a:
#     if a==b==c:
#         print("这是一个等边三角形")
#     elif a==b or b==c or a==c:
#         print("这是一个等腰三角形")
#     else:
#         print("这是一个普通的三角形")
# else:
#     print("这三条边无法构成三角形")

#结构模式匹配match.....case
day = int(input("请输入星期几"))
match day:
    case 1:
        print("今天是周一")
    case 2:
        print("今天是周二")
    case 3:
        print("今天是周三")
    case 4:
        print("今天是周四")
    case 5:
        print("今天是周五")
    case 6:
        print("今天是周六")
    case 7:
        print("今天是周天")
    case _:
        print("错误")

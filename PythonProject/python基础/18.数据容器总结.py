# 开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：
# 1. 添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
# 2. 修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
# 3. 删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
# 4. 查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
# 5. 列出所有学生：遍历所有学生信息并输出。
# 6. 统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
# 7. 退出系统。


#1.确定好框架，用字典嵌套字典的方式来存储学生信息
Stu_dict = {}
#2.生成主菜单
print("请选择你要执行的操作：\n1.添加学生信息\n2.修改学生信息\n3.删除学生信息\n4.查询学生信息\n5.列出所有学生\n6.统计班级成绩\n7.退出系统")
#3.构建选择功能
while True:
    choice = input("请输入你想执行操作的序号")
    if not choice.isdigit():          # 不是纯数字就直接提示，不转 int
        print("请输入1-7之间的有效序号")
        continue
    choice = int(choice)              # 确认是数字再转
    match choice:
        case 1:
            name = input("请输入你要添加的学生姓名")
            chinese_scores = int(input("请输入该学生的语文成绩"))
            math_scores = int(input("请输入该学生的数学成绩"))
            english_scores = int(input("请输入该学生的英语成绩"))
            list_scores = [name,chinese_scores, math_scores, english_scores]
            Stu_dict[name] = list_scores
            print("已成功录入")
        case 2:
            name = input("请输入你要修改的学生姓名")
            if name in Stu_dict:
                chinese_scores = int(input("请输入该学生的语文成绩"))
                math_scores = int(input("请输入该学生的数学成绩"))
                english_scores = int(input("请输入该学生的英语成绩"))
                list_scores = [name, chinese_scores, math_scores, english_scores]
                Stu_dict[name] = list_scores
                print("已成功修改")
            else:
                print("该学生不存在，无法修改")
        case 3:
            name = input("输入你想删除的学生姓名")
            if name in Stu_dict:
                del Stu_dict[name]
                print("已成功删除该学生信息")
            else:
                print("该学生不存在，删除失败")
        case 4:
            name = input("输入你想查询的学生姓名")
            if name in Stu_dict:
                message = Stu_dict[name]
                print(f"{message}")
            else:
                print("该学生不存在")
        case 5:
            for name in Stu_dict:
                print(f"{Stu_dict[name]}")
        case 6:
            students = list(Stu_dict.values())          # 转成真列表，支持下标
            chinese_list = [s[1] for s in students]     # 所有语文成绩
            math_list    = [s[2] for s in students]
            english_list = [s[3] for s in students]

            Max_chinese, Min_chinese = max(chinese_list), min(chinese_list)
            Max_math,    Min_math    = max(math_list),    min(math_list)
            Max_english, Min_english = max(english_list), min(english_list)

            Avg_chinese = sum(chinese_list) / len(chinese_list)
            Avg_math    = sum(math_list)    / len(math_list)
            Avg_english = sum(english_list) / len(english_list)

            # 可能有多个同分，用列表收集学员姓名
            Max_chinese_stu = [s[0] for s in students if s[1] == Max_chinese]
            Min_chinese_stu = [s[0] for s in students if s[1] == Min_chinese]
            Max_math_stu    = [s[0] for s in students if s[2] == Max_math]
            Min_math_stu    = [s[0] for s in students if s[2] == Min_math]
            Max_english_stu = [s[0] for s in students if s[3] == Max_english]
            Min_english_stu = [s[0] for s in students if s[3] == Min_english]

            print(f"语文最高分得主{Max_chinese_stu}，考了{Max_chinese}分；最低分得主{Min_chinese_stu}，考了{Min_chinese}分；平均分{Avg_chinese}")
            print(f"数学最高分得主{Max_math_stu}，考了{Max_math}分；最低分得主{Min_math_stu}，考了{Min_math}分；平均分{Avg_math}")
            print(f"英语最高分得主{Max_english_stu}，考了{Max_english}分；最低分得主{Min_english_stu}，考了{Min_english}分；平均分{Avg_english}")

        case 7:
            break
        case _:
            print("请输入1-7之间的有效序号")












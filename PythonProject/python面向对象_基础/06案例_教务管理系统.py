# 案例：采用面向对象编程思想完成教务管理系统
'''
需求：采用面向对象的编程思想，完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息，通过控制台菜单与用户交互，具体的功能如下：
1. 添加学生成绩：根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
2. 修改学生成绩：根据输入的学生姓名，修改对应的学生成绩
3. 删除学生成绩：根据输入的学生姓名，删除对应的学生成绩
4. 查询指定学生成绩：根据输入的学生姓名，查找对应的学生成绩，并输出
5. 展示全部学生成绩：展示出系统中所有学生的成绩
'''
from os import name

#1.准备
'''
由需求可以看出一共需要定义两个类，分别是“学生”，“教务系统”，分别命名为“Student”，“EduManagement”
'''
class Student():
    def __init__(self, name, chinese=0, english=0, math=0):
        self.name = name
        self.chinese = chinese
        self.english = english
        self.math = math

    def add_score(self, c_scores, e_scores, m_scores):
        self.chinese = c_scores
        self.english = e_scores
        self.math = m_scores

    def change_score(self, c_scores, e_scores, m_scores):
        self.chinese = c_scores
        self.english = e_scores
        self.math = m_scores

    def found_score(self):
        total = self.chinese + self.english + self.math
        print(f"{self.name}的语文成绩为{self.chinese},英语成绩为{self.english},数学成绩为{self.math},总分为{total}")

    # 重写__str__，打印对象时显示学生信息
    def __str__(self):
        total = self.chinese + self.english + self.math
        return f"{self.name} | 语文:{self.chinese} 英语:{self.english} 数学:{self.math} | 总分:{total}"


class EduManagement():
    def __init__(self):
        self.stu_list = []  # 存放Student对象

    # 添加学生成绩
    def add_student(self):
        name = input("请输入学生姓名：")
        # 查找是否同名学生
        for stu in self.stu_list:
            if stu.name == name:
                print("该生成绩信息已经存在")
                return

        chinese = int(input("请输入学生语文成绩："))
        english = int(input("请输入学生英语成绩："))
        math = int(input("请输入学生数学成绩："))

        if 0 <= chinese <= 100 and 0 <= english <= 100 and 0 <= math <= 100:
            stu = Student(name, chinese, english, math)
            self.stu_list.append(stu)
            print("学生信息添加成功")
        else:
            print("学生成绩必须在0~100之间")

    # 修改学生成绩
    def change_student(self):
        name = input("请输入要修改的学生姓名：")
        # 遍历找到学生对象
        target_stu = None
        for stu in self.stu_list:
            if stu.name == name:
                target_stu = stu
                break
        if target_stu is None:
            print("不好意思，此学生还没有任何信息")
            return

        target_stu.found_score()
        chinese = int(input("请输入修改后的语文成绩："))
        english = int(input("请输入修改后的英语成绩："))
        math = int(input("请输入修改后的数学成绩："))

        if 0 <= chinese <= 100 and 0 <= english <= 100 and 0 <= math <= 100:
            target_stu.change_score(chinese, english, math)
            print("学生信息修改成功")
        else:
            print("学生成绩必须在0~100之间")

    # 删除学生成绩
    def del_student(self):
        name = input("请输入要删除的学生姓名：")
        target_stu = None
        for stu in self.stu_list:
            if stu.name == name:
                target_stu = stu
                break
        if target_stu is None:
            print("该生信息不存在")
            return
        self.stu_list.remove(target_stu)
        print("学生信息删除成功")

    # 查询指定学生成绩
    def query_student(self):
        name = input("请输入要查询的学生姓名：")
        target_stu = None
        for stu in self.stu_list:
            if stu.name == name:
                target_stu = stu
                break
        if target_stu is None:
            print("抱歉，未找到该学生信息")
            return
        target_stu.found_score()

    # 展示全部学生成绩
    def list_student(self):
        if not self.stu_list:
            print("暂无学生信息！")
            return
        for stu in self.stu_list:
            print(stu)


# 主菜单
if __name__ == "__main__":
    manager = EduManagement()
    while True:
        print("\n===== 学生成绩管理系统 =====")
        print("1. 添加学生")
        print("2. 修改学生成绩")
        print("3. 删除学生")
        print("4. 查询单个学生")
        print("5. 显示全部学生")
        print("0. 退出系统")
        choice = input("请输入功能序号：")
        try:
            if choice == "1":
                manager.add_student()
            elif choice == "2":
                manager.change_student()
            elif choice == "3":
                manager.del_student()
            elif choice == "4":
                manager.query_student()
            elif choice == "5":
                manager.list_student()
            elif choice == "0":
                print("程序退出")
                break
            else:
                print("输入选项错误，请重新选择！")

        except ValueError as e:
            print("输入的数据有问题，请重新输入")
        except Exception as e:
            print("程序运行出错了，请重新选择")







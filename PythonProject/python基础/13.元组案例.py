#根据提供的学生成绩单，完成以下需求：
'''
1.计算每个学生的总分，各科平均分，然后一并输出
2。统计各科成绩的最低分，最高分，平均分，并输出
3.查找成绩优秀的学生（平均分大于90）的学生，并输出
'''
students = (
    ("S001","王林",85,92,78),
    ("S002","李沐婉",92,88,95),
    ("S003","十三",78,85,82),
    ("S004","曾牛",88,79,91),
    ("S005","周铁",95,96,89),
    ("S006","王卓",76,82,77),
    ("S007","红蝶",89,91,94),
    ("S008","徐立国",75,69,82),
    ("S009","许木",86,89,98),
    ("S010","遁天",66,59,72)
)
#1.计算每个学生的总分，各科平均分，然后一并输出
for stu in students:
    all = stu[2]+stu[3]+stu[4]
    avg = all/3
    print(f"{stu[1]}的总分为{all},\t\t平均分为:{avg:.1f}")

#2.统计各科成绩的最低分，最高分，平均分，并输出
#2.1获取各科成绩
chinese_scores = [stu[2] for stu in students]
math_scores = [stu[3] for stu in students]
english_scores = [stu[4] for stu in students]
#2.2获取最高，最低，平均成绩
lower_chinese_scores = {min(chinese_scores)}
lower_math_scores = {min(math_scores)}
lower_english_scores = {min(english_scores)}

high_chinese_scores = max(chinese_scores)
high_math_scores = max(math_scores)
high_english_scores = max(english_scores)

avg_chinese_scores = sum(chinese_scores)/len(chinese_scores)
avg_math_scores = sum(math_scores)/len(math_scores)
avg_english_scores = sum(english_scores)/len(english_scores)

print(f"语文的最低分是{lower_chinese_scores},最高分是{high_chinese_scores},平均分是{avg_chinese_scores:1f}")
print(f"数学的最低分是{lower_math_scores},最高分是{avg_math_scores},平均分是{avg_math_scores:1f}")
print(f"英语的最低分是{lower_english_scores},最高分是{high_english_scores},平均分是{avg_english_scores:1f}")


#3.判断优秀学生
print("优秀学生名单如下：")
for stu in students:
    total = stu[2]+stu[3]+stu[4]
    avg = total/3
    if avg > 90:
        print(f"{stu[0]},{stu[1]},平均分{avg:.1f}")


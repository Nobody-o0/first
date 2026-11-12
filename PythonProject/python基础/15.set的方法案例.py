#根据以下数据，完成如下需求：
'''
1.找出同时选修了法语和艺术的学生
2.找出同时选修了所有四门课程的学生
3.找出选修了足球，但没有选修篮球的学生
4.统计每一个学生选修的课程数量
'''
# 选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}

# 选修篮球学生名单
basketball_set = {"张铁", "墨居仁","王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}

# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}

# 选修艺术学生名单
art_set = { "遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}



#1.找出同时选修了法语和艺术的学生
print(f"同时选修了法语和艺术的学生有：{french_set.intersection(art_set)}")

#2.找出同时选修了所有课程的学生
print(f"选修了所有课程的学生有：{football_set.intersection(basketball_set.intersection(french_set.intersection(art_set)))}")

#3.找出选修了足球，但没有选修篮球的学生
print(f"选修了足球却没有选修篮球的学生有：{football_set.difference(basketball_set)}")

#4.统计所有学生选修的课程数量
all_set= (football_set | art_set | basketball_set | french_set)
all_student_list= [*football_set,*basketball_set, *french_set, *art_set]
for student in all_set :
    print(f"{student}选修了{all_student_list.count(student)}门课程")#.count可以统计元素出现在列表中的次数

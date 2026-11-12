'''
完成以下需求
1.定义一个函数：根据传入的底和高计算三角形面积的函数（三角形面积=底*高/2）
2.定义一个函数：计算传入的字符串中的元音字母的个数（元音字母为aeiouAEIOU）.
3.定义一个函数：计算传入的班级学员高考成绩列表中的最高分，最低分，平均分（保留一位小数），并返回
'''
def triangle_area(high,low):
    '''
    通过底和高来计算三角形的面积
    :param high:三角形的高
    :param low:三角形的底边
    :return:返回面积
    '''
    area = high*low/2
    return area

def vowel_letters(s):
    '''
    统计输入的字符串中的元音字母的个数
    :param s: 用户输入的字符串
    :return: 返回字符出中元音字母个数
    '''
    num = 0
    for c in s:
        if c in 'aeiouAEIOU':
            num += 1
    return num

def scores_processing(s_list):
    '''
    统计学生成绩列表的最高分最低分和平均分
    :param s_list: 学生高考成绩列表
    :return: 返回最高分最低分和平均分
    '''
    return max(s_list),min(s_list),round(sum(s_list)/len(s_list),1)



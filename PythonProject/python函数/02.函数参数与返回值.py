#计算圆的面积，周长,多个返回值会封装到元组之中
def circle_area(r):
    '''
    根据圆的面积计算圆的面积和圆的周长
    :param r: 圆的半径
    :return: 圆的面积，圆的周长
    '''
    area = 3.14*r*r
    lenth = 2*r*3.14
    return area, lenth


print(f"{circle_area(4)}")



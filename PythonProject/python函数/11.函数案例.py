'''
#案例一：N的阶乘，定义一个函数，根据传入的数字，输出他的阶乘
'''
def jiecheng(n):
    if n==1 :
        return 1  #这是调用的终结点，运用递归的时候尤其要注意，没有他，当调用到n=1后，又会调用n=0,n=-1直至n=负无穷，栈会直接溢出
    else:
        return n * jiecheng(n-1)
#上面这个函数采用了递归的办法，在函数内部调用自己，调用一次就入一次栈，高位先进栈，函数又在内部被调用，低位跟着进栈，层层进栈直到n = 1
#此时返回的值为1，终于不再调用，此时用n=1的返回值再去回流给n =2出栈...依此类推直到n=10出栈，问题便解决了

result = (jiecheng(10))
print(result)


'''
案例二：定义一个用于根据传入的一批商品信息（商品名，价格，数量），优惠（优惠券，积分抵扣），运费信息计算订单的总金额的函数
具体规则如下：
1.优惠券需要商品满5000才可以使用，且优惠券金额不能超过商品总价
2.积分抵扣需要商品总金额满5000才可以使用，100积分抵扣1元（且积分总额不能超过商品总价格，积分只能整百抵扣）
'''

def calc_order_cost(*shop_tuple,youhuiquan,jifen,yunfei):
    '''
    根据传入的一批商品信息运费信息计算订单的总金额的函数
    :param shop_list: 商品信息（名称，价格，数量）如：("鼠标"，100，2),("键盘"，200，2)
    :param youhui: 优惠信息（优惠券抵扣金额，积分数量），如：(1000,2000)
    :param yunfei: 运输费用
    :return: 需要支付的金额
    '''
    #订单的总金额 = 价格*数量-优惠+运输费用
    #1.计算总金额
    his_cost = 0
    for item in shop_tuple:
        shop_prices = item[1]*item[2]
        his_cost += shop_prices

    #2.计算优惠
    if his_cost>=5000:
        youhuijine=youhuiquan+jifen%100
    else:
        youhuijine=0

    #3.连带运费一起计算支付额
    return (his_cost-youhuijine+yunfei)


pay_list=calc_order_cost(("鼠标",100,2),("键盘",200,2),youhuiquan=900,jifen=100,yunfei=20)
print(pay_list)



#类型注解：是Python中的一种语法特性，用于明确标识变量，函数参数和返回值的变量类型，从而使代码更清晰更安全，更易维护。
a: int =695
score:float=98.5
hobby:str="Python"
flag:bool=True
pic:None=None

names:list[str]=["a","b","c"]
phones:set[str]={"13309091111","15233045567"}
options:dict[str,int]={"count":0,"total":0}
goods:tuple[str,int,int]=("手机",5999,1)

#函数类型注解
def circle_area_len(r:float)->float:
    area=3.14*r**2
    len =3.14*2*r
    return area,len

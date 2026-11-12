#有时候参数的的数量不是固定的，所以需要不定长参数，不定长参数有两种形式
#1.位置传递（*args）
def calc_data(*arges):#args不是一个关键字，它只是一个约定俗成的变量名，你也可以把它改成你喜欢的变量名
    min_data=min(arges)
    max_data=max(arges)
    avg_data=sum(arges)/len(arges)
    return min_data,max_data,round(avg_data,1)

#本质是将我们输入的变量封装成了一个元组，再通过*号来解包

data = calc_data(1,2,3,4,5,5,6,7,78,8,8,100)
print(data)


#2.关键字传递的不定长参数（**kwargs）
def calc_data1(*arges,**karges):#kwargs不是一个关键字，它只是一个约定俗成的变量名，你也可以把它改成你喜欢的变量名
    min_data=min(arges)
    max_data=max(arges)
    avg_data=sum(arges)/len(arges)

    if karges.get("round"):
        avg_data=round(avg_data,karges.get("round"))

    return min_data,max_data,round(avg_data,1)

data = calc_data1(20,40,80,200,round=3 ,count=0)
#这里后面输入的参数是以键值对的形式传递的，这些键和值参数被kwarges接收，通过**符号组包封装成字典类型
print(data)

data = calc_data1(20,40,80,200)
print(data)



#一个小例子，比如点奶茶要加小料

def get_milk_tea(naichaminzi,tiandu,bindu,*jiaoliao):
    print(f"点单成功，你点的{naichaminzi},{tiandu},{bindu},{jiaoliao}马上就好了")

get_milk_tea("lulu","zhondeng","qubin","布丁","珍珠")

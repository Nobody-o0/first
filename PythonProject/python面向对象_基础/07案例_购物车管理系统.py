# 采用面向对象的编程思想，开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。
# 系统使用自定义对象存储商品数据，通过控制台菜单与用户交互。具体功能如下：
# 1. 添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
# 2. 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
# 3. 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
# 4. 查询购物车：将购物车中的商品信息展示出来，格式为: "商品名称：xxx，商品价格：xxx，商品数量：xxx"。
# 5. 退出购物车

#定义商品类
class Good():
    def __init__(self,name,num,price):
        self.name = name
        self.num = num
        self.price = price

    def __str__(self):
        return f"{self.name} | {self.num} | {self.price}"


#定义购物车类
class ShoppingCart(Good):
    def __init__(self):
        self.goods_list = []

    def add_good(self):
        name = input("请输入你要添加的商品名称：")
        for g in self.goods_list:
            if g.name == name:
                num = int(input("请输入你想要添加的商品数量："))
                g.num += num
                return
        num = int(input("请输入你要添加的商品数量："))
        price = int(input("请输入你要添加的商品的价格："))
        self.goods_list.append(Good(name,num,price))

    def change_good(self):
        name = input("请输入你想查询的商品名称：")
        for g in self.goods_list:
            if g.name == name:
                num = int(input("请输入你想修改的商品数量："))
                g.num = num
                return
        print(f"该商品不存在，请添加后再试")

    def del_good(self):
        name = input("请输入你想删除的商品名称：")
        for g in self.goods_list:
            if g.name == name:
                self.goods_list.remove(g)
                return
        print(f"该商品不存在，请检查商品名称是否正确")

    def show(self):
        for g in self.goods_list:
            print(g)


#定义购物车主菜单
if __name__ == "__main__":
    shopping_cart = ShoppingCart()
    while True:
        way = int(input("请输入你想执行的功能"))
        match way:
            case 1:
                shopping_cart.add_good()
            case 2:
                shopping_cart.change_good()
            case 3:
                shopping_cart.del_good()
            case 4:
                shopping_cart.show()
            case 5:
                break




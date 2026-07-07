# 需求：采用面向对象的编程思想，开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用自定义对象存储 商品数据，
# 通过控制台菜单与用户交互。具体功能如下：

# 添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。

# 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。

# 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。

# 查询购物车：将购物车中的商品信息展示出来，格式为："商品名称: xxx, 商品价格: xxx, 商品数量: xxx"。

# 退出购物车
# ————————————————
# 版权声明：本文为CSDN博主「Maiko Star」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/weixin_55772633/article/details/162603980

class Goods:
    def __init__(self, g_name, g_price, g_num):
        self.name = g_name
        self.price = g_price
        self.num = g_num

    def __str__(self):
        return f"商品名称：{self.name} | 商品价格：{self.price} | 商品数量：{self.num}"

    def update(self, g_name=None, g_price=None, g_num=None):
        if g_name is not None:
            self.name = g_name
        if g_price is not None:
            self.price = g_price
        if g_num is not None:
            self.num = g_num


class ShoppingCart:
    def __init__(self):
        self.goods_list = []  # 商品信息记录在这个列表中

    def add_goods(self):  # 添加商品
        name = input("请输入商品名称：")

        for g in self.goods_list:
            if g.name == name:
                print("该商品已存在！")
                return

        price = input("请输入商品价格：")
        num = input("请输入商品数量：")
        goods = Goods(name, int(price), int(num))
        self.goods_list.append(goods)
        print("商品信息添加成功！")

    def update_goods(self):  # 修改商品
        name = input("请输入要修改的商品名称：")
        for g in self.goods_list:
            if g.name == name:
                print(f"当前商品信息：{g}")
                price = input("请输入商品价格：")
                num = input("请输入商品数量：")
                g.update(g_price=int(price), g_num=int(num))
                print("商品信息修改成功！")
                return
        print("未找到该商品！")

    def delete_goods(self):  # 删除商品
        name = input("请输入要删除的商品名称：")
        for g in self.goods_list:
            if g.name == name:
                self.goods_list.remove(g)
                print("商品信息删除成功！")
                return
        print("未找到该商品！")

    def query_goods(self):  # 查询商品
        name = input("请输入要查询的商品名称：")
        for g in self.goods_list:
            if g.name == name:
                print(f"商品信息：{g}")
                return
        print("未找到该商品！")

    def show_all_goods(self):  # 显示所有商品
        for g in self.goods_list:
            print(g)

    def run(self):  # 运行购物车管理系统
        while True:
            print("="*30)
            print("欢迎使用购物车管理系统！")
            print("1. 添加商品")
            print("2. 修改商品")
            print("3. 删除商品")
            print("4. 查询商品")
            print("5. 显示所有商品")
            print("6. 退出系统")
            print("="*30)
            choice = input("请输入操作编号：")
            if choice == "1":
                self.add_goods()
            elif choice == "2":
                self.update_goods()
            elif choice == "3":
                self.delete_goods()
            elif choice == "4":
                self.query_goods()
            elif choice == "5":
                self.show_all_goods()
            elif choice == "6":
                print("退出系统！")
                break
            else:
                print("输入有误，请重新输入！")


if __name__ == "__main__":
    cart = ShoppingCart()
    cart.run()

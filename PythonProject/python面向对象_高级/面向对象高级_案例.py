# 某社区图书馆需要开发一个简单的图书管理系统。系统需要支持会员登录、图书借阅、图书归还等功能。
'''
系统中有两种类型的会员：普通会员和VIP会员，他们的借书权限不同。
需要使用面向对象编程的思想，设计并实现这个图书管理系统。

核心功能：
1. 会员登录：会员通过卡号和密码登录系统
2. 借书：会员可以借阅库存中有余量的图书
3. 还书：会员可以归还借阅的图书
4. 查看我的借阅：展示当前会员已经借阅的图书列表
5. 退出系统

借阅规则：
1. 普通会员最多可借3本
2. VIP会员最多可借 6+VIP等级 本（VIP等级，默认为1）

注意：
1. 登录成功（卡号和密码均正确）后，才可以访问该系统
2. 图书库存不足，或当前会员借书数量达到最大借书数量，不能再借新书
'''
import json
import os


class Member:
    """会员基类：普通会员和VIP会员的公共部分"""
    def __init__(self, card_no, password):
        self.card_no = card_no
        self.password = password
        self.borrowed = []              # 已借阅的图书列表（同书借多本会重复出现）

    def get_max_books(self):
        return 0

    def remaining_slots(self):
        return self.get_max_books() - len(self.borrowed)

    def borrow(self, book, count):
        if book.stock < count:
            print(f"《{book.name}》库存不足（当前 {book.stock} 本，需 {count} 本）")
            return False
        if self.remaining_slots() < count:
            print(f"剩余可借额度 {self.remaining_slots()} 本，不够借 {count} 本")
            return False
        book.stock -= count
        self.borrowed.extend([book] * count)
        print(f"成功借阅《{book.name}》x{count}，剩余库存 {book.stock}，已借 {len(self.borrowed)} 本")
        return True

    def return_book(self, book, count):
        have = self.borrowed.count(book)
        if have == 0:
            print(f"《{book.name}》不是您借阅的图书")
            return False
        if count > have:
            print(f"您只借了 {have} 本，不能还 {count} 本")
            return False
        for _ in range(count):
            self.borrowed.remove(book)
        book.stock += count
        print(f"成功归还《{book.name}》x{count}，当前库存 {book.stock}")
        return True

    def show_borrowed(self):
        if not self.borrowed:
            print("您当前没有借阅任何图书")
            return
        print(f"{self.card_no} 已借阅：")
        for b in self.borrowed:
            print(f"  - 《{b.name}》")


class NormalMember(Member):
    def get_max_books(self):
        return 3


class VipMember(Member):
    def __init__(self, card_no, password, vip_level=1):
        super().__init__(card_no, password)
        self.vip_level = vip_level

    def get_max_books(self):
        return 6 + self.vip_level


class Book:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock


class LibrarySystem:
    def __init__(self, members_file="members.json", books_file="books.json"):
        self.members = {}                       # 卡号 -> 会员对象
        self.books = []                         # 图书列表
        self.members_file = members_file        # 会员数据文件
        self.books_file = books_file            # 书库数据文件
        self.load()                             # 启动时从两个文件读数据

    # ---------- 持久化：保存 ----------
    def save(self):
        """把内存对象转成字典，分别写入 members.json 和 books.json"""
        # 会员 -> members.json
        members_data = [
            {
                "card_no": m.card_no,
                "password": m.password,
                "type": m.__class__.__name__,            # 存类名："NormalMember"/"VipMember"
                "vip_level": getattr(m, "vip_level", None),  # 普通会员没有该属性 -> None
                "borrowed": [b.name for b in m.borrowed],    # 借阅记录只存书名
            }
            for m in self.members.values()
        ]
        with open(self.members_file, "w", encoding="utf-8") as f:
            json.dump(members_data, f, ensure_ascii=False, indent=2)

        # 图书 -> books.json
        books_data = [
            {"name": b.name, "stock": b.stock}
            for b in self.books
        ]
        with open(self.books_file, "w", encoding="utf-8") as f:
            json.dump(books_data, f, ensure_ascii=False, indent=2)

    # ---------- 持久化：加载 ----------
    def load(self):
        """启动时分别读取两个 JSON 文件重建对象；文件缺失则用默认数据"""
        # 1) 加载图书
        if os.path.exists(self.books_file):
            with open(self.books_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.books = [Book(b["name"], b["stock"]) for b in data]
        else:
            self.books = [Book("三体", 5), Book("活着", 1)]

        # 书名 -> 对象 映射（供恢复会员借阅记录用）
        book_map = {b.name: b for b in self.books}

        # 2) 加载会员
        if os.path.exists(self.members_file):
            with open(self.members_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            for md in data:
                if md["type"] == "VipMember":
                    m = VipMember(md["card_no"], md["password"], md.get("vip_level", 1))
                else:
                    m = NormalMember(md["card_no"], md["password"])
                # 恢复借阅记录：把书名映射回 Book 对象
                m.borrowed = [book_map[name] for name in md.get("borrowed", []) if name in book_map]
                self.members[m.card_no] = m
        else:
            self.add_member(NormalMember("N001", "123456"))
            self.add_member(VipMember("V001", "654321", vip_level=1))
            self.add_member(VipMember("V002", "111111", vip_level=2))

        # 3) 首次运行（任一文件缺失）把默认数据写盘
        if not os.path.exists(self.members_file) or not os.path.exists(self.books_file):
            self.save()
            print("首次运行，已生成 members.json 和 books.json")

    # ---------- 业务 ----------
    def add_member(self, member):
        self.members[member.card_no] = member

    def add_book(self, book):
        self.books.append(book)

    def register(self):
        card_no = input("请输入新卡号：")
        if card_no in self.members:
            print("该卡号已存在，注册失败")
            return
        password = input("请输入密码：")
        print("请选择会员类型：1.普通会员  2.VIP会员")
        t = input("请选择（默认1）：") or "1"
        if t == "2":
            vip_level = int(input("请输入VIP等级（默认1）：") or "1")
            member = VipMember(card_no, password, vip_level)
        else:
            member = NormalMember(card_no, password)
        self.members[card_no] = member
        self.save()                     # 注册后立即写回文件
        print(f"注册成功！欢迎 {card_no}（{member.__class__.__name__}）")

    def login(self, card_no, password):
        m = self.members.get(card_no)
        if m and m.password == password:
            print(f"登录成功，欢迎 {card_no}（{m.__class__.__name__}）")
            return m
        print("卡号或密码错误，登录失败")
        return None

    def find_book(self, name):
        for b in self.books:
            if b.name == name:
                return b
        return None

    def run(self, member):
        while True:
            print("\n1.借书  2.还书  3.查看我的借阅  4.退出")
            choice = input("请选择：")
            if choice == "1":
                name = input("请输入书名：")
                count = int(input("请输入借阅数量："))
                book = self.find_book(name)
                if book:
                    member.borrow(book, count)
                    self.save()         # 借书后写回文件
                else:
                    print("没有找到这本书")
            elif choice == "2":
                name = input("请输入书名：")
                count = int(input("请输入归还数量："))
                book = self.find_book(name)
                if book:
                    member.return_book(book, count)
                    self.save()         # 还书后写回文件
                else:
                    print("没有找到这本书")
            elif choice == "3":
                member.show_borrowed()
            elif choice == "4":
                print("退出系统")
                break


# ---------- 测试入口 ----------
if __name__ == "__main__":
    sys = LibrarySystem()               # 构造时自动 load()，读或生成两个 JSON 文件

    while True:
        print("\n===== 图书管理系统 =====")
        print("1.登录  2.注册新会员  exit.退出")
        cmd = input("请选择：")
        if cmd == "2":
            sys.register()
        elif cmd == "exit":
            break
        else:
            card = input("请输入卡号：")
            pwd = input("请输入密码：")
            member = sys.login(card, pwd)
            if member:
                sys.run(member)

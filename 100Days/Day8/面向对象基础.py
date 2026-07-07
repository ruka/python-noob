# class car:
#     def __init__(self, c_color, c_band, c_name, c_price):
#         self.color = c_color
#         self.band = c_band
#         self.name = c_name
#         self.price = c_price


# car1 = car("red", "奔驰", "e300", 1000000)
# car2 = car("black", "宝马", "x5", 800000)
# print(car1.__dict__)
# print(car2.__dict__)


# 教务管理系统
# 学生信息
class Student:
    def __init__(self, s_name, s_chinese, s_math, s_english):
        self.name = s_name
        self.chinese = s_chinese
        self.math = s_math
        self.english = s_english

    def __str__(self):
        return f"学生姓名：{self.name} | 语文成绩：{self.chinese} | 数学成绩：{self.math} | 英语成绩：{self.english} | 总成绩：{self.chinese + self.math + self.english}"

    def update(self, s_name=None, s_chinese=None, s_math=None, s_english=None):
        if s_name is not None:
            self.name = s_name
        if s_chinese is not None:
            self.chinese = s_chinese
        if s_math is not None:
            self.math = s_math
        if s_english is not None:
            self.english = s_english


class Edumanagement:
    def __init__(self):
        self.students_list = []  # 学生成绩记录在这个列表中
        # 添加学生功能

    def add_student(self):
        name = input("请输入学生姓名：")

        # 判断学生是否存在
        for s in self.students_list:
            if s.name == name:
                print("该学生已存在！")
                return

        chinese = input("请输入语文成绩：")
        math = input("请输入数学成绩：")
        english = input("请输入英语成绩：")

        # 判断成绩是否在0到100之间
        if 0 <= int(chinese) <= 100 and 0 <= int(math) <= 100 and 0 <= int(english) <= 100:
            stu = Student(name, int(chinese), int(math), int(english))
            self.students_list.append(stu)
            print("学生信息添加成功！")
        else:
            print("成绩输入有误，请输入0到100之间的成绩！")

    # 修改学生信息功能
    def update_student(self):
        name = input("要修改的学生姓名：")
        for s in self.students_list:
            if s.name == name:
                print(f"当前学生信息：{s}")
                chinese = input("请输入新的语文成绩：")
                math = input("请输入新的数学成绩：")
                english = input("请输入新的英语成绩：")
                if 0 <= int(chinese) <= 100 and 0 <= int(math) <= 100 and 0 <= int(english) <= 100:
                    s.update(s_chinese=int(chinese), s_math=int(
                        math), s_english=int(english))
                    print("学生信息修改成功！")
                    return
                else:
                    print("成绩输入有误，请输入0到100之间的成绩！")
                return
        print("未找到该学生信息！")

    # 删除学生信息功能
    def delete_student(self):
        name = input("要删除的学生姓名：")
        for s in self.students_list:
            if s.name == name:
                self.students_list.remove(s)
                print("学生信息删除成功！")
                return
        print("未找到该学生信息！")

    # 查询学生信息功能
    def query_student(self):
        name = input("要查询的学生姓名：")
        for s in self.students_list:
            if s.name == name:
                print(f"学生信息：{s}")
                return
        print("未找到该学生信息！")
    # 展示所有学生信息功能

    def show_all_students(self):
        for s in self.students_list:
            print(s)

    # 主菜单功能
    def main_menu(self):
        while True:
            print("=" * 30)
            print("欢迎使用教务管理系统")
            print("1. 添加学生信息")
            print("2. 修改学生信息")
            print("3. 删除学生信息")
            print("4. 查询学生信息")
            print("5. 展示所有学生信息")
            print("6. 退出系统")
            print("=" * 30)
            choice = input("请输入操作编号（1-6）：")
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.update_student()
            elif choice == "3":
                self.delete_student()
            elif choice == "4":
                self.query_student()
            elif choice == "5":
                self.show_all_students()
            elif choice == "6":
                print("退出系统！")
                break
            else:
                print("输入有误，请重新输入！")


# 运行代码
if __name__ == "__main__":
    edu = Edumanagement()
    edu.main_menu()

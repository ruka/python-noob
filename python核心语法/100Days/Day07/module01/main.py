# 在main.py中去调用my_module.py中的函数

from my_function import function1, NAME, PI, E  # 调用模块的某一个功能
# import my_function  # 调用整个模块
input_number = int(input("请输入一个整数: "))
result = function1(input_number)
# result = my_function.function1(input_number)  # 调用模块中的函数
print(f"{input_number}的阶乘是: {result}")

# 输出my_function.py中的常量
print(f"我的名字是：{NAME}")  # 输出我的名字
print(f"PI的值是：{PI}")  # 输出3.14159
print(f"E的值是：{E}")  # 输出2.71828


# print(f"我的名字是：{my_function.NAME}")  # 输出我的名字
# print(f"PI的值是：{my_function.PI}")  # 输出3.14159
# print(f"E的值是：{my_function.E}")  # 输出2.71828

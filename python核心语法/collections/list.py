# @Author：颜凡
# @File  ：list.py
# @Time  ：2026/3/19 22:47
"""
list1 = [10,14,1,3,11,1]
print(list1)
print(type(list1))
print(list1[3])
"""


def sum_digits(char_list):
    """计算字符列表中所有数字字符的数值之和"""
    total = 0
    for ch in reversed(char_list):
        if ch.isdigit():
            total += int(ch)
    return total


# 从用户输入读取字符串并转为字符列表
chars = list(input("请输入一串字符："))
result = sum_digits(chars)
print(f"数字之和为：{result}")

# @Author：颜凡
# @File  ：function2.py
# @Time  ：2026/3/20 20:42

# 函数的定义和使用 - 求最大公约数和最小公倍数
def function2(num1, num2):
    if num1 < num2:
        (num1, num2) = (num2, num1)
    for x in range(num1, 1, -1):
        if num1 % x == 0 and num2 % x == 0:
            return x
    return 1  #如果这两个数没有公因数则返回1


def function22(num1, num2):
    y = num1 * num2 / function2(num1, num2)
    return y


print(function2(15,27 ))
print(int(function22(15,27)))

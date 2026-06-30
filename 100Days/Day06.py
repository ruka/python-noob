'''# 练习1：实现计算求最大公约数和最小公倍数的函数。
def gys(x, y):
    if x > y:
        x, y = y, x

    for i in range(x, 0, -1):
        if x % i == 0 and y % i == 0:
            return i


def gbs(x, y):
    return x*y//gys(x, y)


x = int(input())
y = int(input())
result1 = gys(x, y)
result2 = gbs(x, y)
print("最大公约数是：", result1)
print("最小公倍数是：", result2)
'''

# 练习2：实现判断一个数是不是回文数的函数。


def function1(num):
    i = num
    total = 0
    while i > 0:
        total = total * 10 + i % 10
        i = i // 10
    return total == num


"""
x = int(input("请输入一个数："))
print(function1(x))
"""

# 练习3：实现判断一个数是不是素数的函数。


def function2(num):
    for x in range(2, num):
        if num % x == 0:
            return False
    return True


""""
x = int(input("请输入一个数："))
print(function2(x))
"""

# 练习4：写一个程序判断输入的正整数是不是回文素数。
num = int(input("输入一个正整数："))
if function1(num) and function2(num):
    print("ture")
else:
    print("flase")

# 练习1：实现计算求最大公约数和最小公倍数的函数。
def gys(x, y):
    if x > y:
        x, y = y, x

    for i in range(x, 0, -1):
        if x % i == 0 and y % i == 0:
            return i


def gbs(x, y):
    return x*y//gys(x, y)


x = int(input("请输入一个数："))
y = int(input("请输入另一个数："))
result1 = gys(x, y)
result2 = gbs(x, y)
print("最大公约数是：", result1)
print("最小公倍数是：", result2)

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


# 练习5：实现一个函数，接收任意数量的参数，返回这些参数的最小值、最大值和平均值。   //基于位置不定长参数 *args
def data(*args):
    min_args = min(args)
    max_args = max(args)
    avg_args = sum(args)/len(args)
    return min_args, max_args, round(avg_args, 1)  # 保留1位小数


print(data(1, 2, 3, 2, 3, 4, 1, 44))

# 练习6：在练习5的基础上，增加一个可选参数，指定平均值保留的小数位数，如果不指定，则默认保留1位小数。


def data(*args, **kwargs):
    min_args = min(args)
    max_args = max(args)
    avg_args = sum(args)/len(args)
    if kwargs.get('round'):  # 关键字传递 **kwargs
        return min_args, max_args, round(avg_args, kwargs['round'])  # 保留指定小数位
    return min_args, max_args, round(avg_args, 1)  # 默认保留1位小数


print(data(1, 2, 3, 2, 3, 4, 1, 43, round=3))
print(data(1, 2, 3, 2, 3, 4, 1, 44))


# 练习7：实现一个函数，接收两个参数，一个是数字，一个是函数名，返回该函数对该数字的运算结果。//当参数为函数时


def add(x, y):
    return x+y


def sub(x, y):
    return x-y


def mul(x, y):
    return x*y


def div(x, y):
    return x/y


def calculator(x, y, func):
    return func(x, y)


m = calculator(3, 5, mul)
print(m)


# 练习8：匿名函数
lambda x, y: x + y


def add(x, y): return x + y


x = int(input())
y = int(input())
print(add(x, y))

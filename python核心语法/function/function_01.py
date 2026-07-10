def cry():
    """打印小猫叫声"""
    print("小猫喵喵叫")


cry()


def cal01():
    """计算从1到用户输入值的累加和"""
    n = int(input("请输入a的值:"))
    total = 0
    for i in range(1, n + 1):
        total += i
    else:
        print(total)


cal01()


def get_sum(a, b):
    """返回两个数之和"""
    result = a + b
    return result


a = float(input("请输入一个数的值："))
b = float(input("请输入另一个数的值："))
result = get_sum(a, b)
print(result)

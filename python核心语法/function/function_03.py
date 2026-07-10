def my_sum(*args):
    """计算任意数量参数的总和"""
    print(f"输入的值为：{args}, args的数据类型: {type(args)}")
    total = 0
    for n in args:
        total += n
    return total


# a = tuple(input())
result = my_sum(1, 2, 3)
print(f"输出总和: {result}")

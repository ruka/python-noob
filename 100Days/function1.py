# @Author：颜凡
# @File  ：function1.py
# @Time  ：2026/3/20 20:29

# 将求阶乘的功能封装成一个函数
def function1(n):
    result=1
    for num in range(1,n+1):
        result *=num
    return result
print(function1(5))

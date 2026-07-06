# 这是一个计算阶乘的函数

def function1(n):
    result = 1
    for num in range(1, n+1):
        result *= num
    return result


# 几个常量
PI = 3.14159
E = 2.71828
NAME = "yanfan"

# 内置函数 "__name__" 的作用是判断当前模块是否是主程序入口，如果是主程序入口，则执行下面的代码块
if __name__ == "__main__":
    num = int(input("请输入一个整数: "))
    m = function1(num)  # 调用函数测试
    print(f"{num}的阶乘是: {m}")  # 调用函数测试

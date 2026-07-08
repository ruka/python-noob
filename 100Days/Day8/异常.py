try:
    a = int(input("请输入一个整数: "))
    b = int(input("请输入另一个整数: "))
    result = a / b
    print("结果是:", result)
except ValueError:
    print("输入的不是整数！")
except ZeroDivisionError:
    print("除数不能为零！")
except Exception as e:  # 捕获其他所有未被处理的异常
    print("发生了一个异常:", e)
finally:                # 无论是否发生异常，都会执行，可有可无
    print("程序执行结束。")

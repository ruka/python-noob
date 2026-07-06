# # 练习1：导入随机数模块
# import random

# i = 0
# while i < 10:
#     i += 1
#     print(random.randint(1, 10))  # 随机生成1到10之间的整数


# # 练习2：用别名调用
# import random as rd

# i = 0
# while i < 10:
#     i += 1
#     print(rd.randint(90, 100))  # 随机生成90到100之间的整数


# # 练习3：导入模块中的指定函数
# from random import randint as rd1
# for i in range(10):
#     print(rd1(1, 100))  # 随机生成1到100之间的整数


# 练习4：导入模块中的所有函数/功能
from random import *
for i in range(10):
    print(randint(1, 100))  # 随机生成1到100之间的整数

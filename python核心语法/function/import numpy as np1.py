import numpy as np

np.random.seed(1)
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.random.randint(2, 20, size=(3, 3)).astype("int64")
print("数组a：")
print(a)
print("\n数组b：")
print(b)

print("(1):")
print("a + b :")
print(a + b)
print("\na - b :")
print(a - b)
print("\na * b :")
print(a * b)
print("\na / b :")
print(a / b)
print("\nb **  a:")
print(b**a)
print("a ** 2 :")
print(a**2)
print("a > b :")
print(a > b)

print("(2):")
ab = np.vstack((a, b))
print(ab)
print("\nab 的第 3 行（索引 2）:")
print(ab[2, :])
print("\nab 的第 1 列（索引 0）:")
print(ab[:, 0])

a_row_rev = a[::-1, :]
b_col_rev = b[:, ::-1]
print("\n(3)")
print(a_row_rev)
print("\n按列逆序后的 b:")
print(b_col_rev)

a_del_row1 = np.delete(a, 0, axis=0)
b_del_col1 = np.delete(b, 0, axis=1)
print("\n(4):")
print(a_del_row1)
print("\n删除 b 的第 1 列后:")
print(b_del_col1)

"""
import numpy as np

a = np.array([[2, 10, 20], [80, 43, 31], [22, 43, 10]])

print('原始数组：\n')
print(a)
print('\n')

print('数组中最小元素：', np.min(a))
print('数组中最大元素：', np.max(a))
print('\n')
print('数组列中最小元素：', np.min(a, axis=0))
print('数组列中最大元素：', np.max(a, axis=0))
print('\n')
print('数组行中最小元素：', np.min(a, axis=1))
print('数组行中最大元素：', np.max(a, axis=1))
print('行峰间值：', np.ptp(a, axis=1))
print('列峰间值：', np.ptp(a, axis=0))
print('列10%分位数', np.percentile(a, 10, axis=0))
print('行10%分位数', np.percentile(a, 10, axis=1))
print('列中位数：', np.median(a, axis=0))
print('行平均值：', np.mean(a, axis=1))
print('数组a的方差：', np.var(a))
print('数组a的标准差：', np.std(a))
"""

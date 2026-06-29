# ==================== 递归与高阶函数练习 ====================

# ---------- 1. 递归基本示例 ----------
def test(n):
    """递归打印：先递推再回归时打印"""
    if n > 2:
        test(n - 1)
    print(f"n = {n}")


# ---------- 2. 斐波那契数列 ----------
def fibonacci(n):
    """返回第 n 项斐波那契数（1-based：F(1)=1, F(2)=2）"""
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


# ---------- 3. 猴子吃桃问题 ----------
def monkey_peach(day):
    """第10天剩1个桃，每天吃一半+1个，求第1天共多少桃"""
    if day == 10:
        return 1
    else:
        return 2 * (monkey_peach(day + 1) + 1)


# ---------- 4. 递推公式 f(1)=3, f(n)=2*f(n-1)+1 ----------
def recurrence(n):
    """递推公式：f(1)=3, f(n) = 2*f(n-1) + 1"""
    if n == 1:
        return 3
    else:
        return 2 * recurrence(n - 1) + 1


# ---------- 5. 汉诺塔问题 ----------
def hanoi_tower(num, a, b, c):
    """汉诺塔：将 num 个盘从柱 a 经过柱 b 移到柱 c"""
    if num == 1:
        print(f"第1个盘从：{a} -> {c}")
    else:
        hanoi_tower(num - 1, a, c, b)   # 将 n-1 个盘从 A 经 C 移到 B
        print(f"第{num}个盘从：{a} -> {c}")
        hanoi_tower(num - 1, b, a, c)   # 将 n-1 个盘从 B 经 A 移到 C


# ---------- 6. 函数作为参数传递（高阶函数） ----------
def num_max(num1, num2):
    """返回两数中的较大值"""
    return num1 if num1 > num2 else num2


def num_min(num1, num2):
    """返回两数中的较小值"""
    return num1 if num1 < num2 else num2


def num_sum(myfun, num1, num2):
    """高阶函数：用传入的函数处理两数后与两数和相乘"""
    value = myfun(num1, num2)
    return (num1 + num2) * value


# ==================== 测试入口 ====================
if __name__ == "__main__":
    print("=== 1. 递归打印 ===")
    test(4)

    print("\n=== 2. 斐波那契数列 ===")
    m = int(input("请输入斐波那契项数："))
    print(f"第{m}项斐波那契数为：{fibonacci(m)}")

    print("\n=== 3. 猴子吃桃 ===")
    print(f"最初有桃子：{monkey_peach(1)}")

    print("\n=== 4. 递推公式 ===")
    n = int(input("请输入 n："))
    print(f"f({n}) = {recurrence(n)}")

    print("\n=== 5. 汉诺塔 ===")
    disks = int(input("请输入汉诺塔盘子数："))
    hanoi_tower(disks, "A", "B", "C")

    print("\n=== 6. 高阶函数 ===")
    result = num_sum(num_max, 3, 5)
    print(f"num_sum(num_max, 3, 5) = {result}")
    result2 = num_sum(num_min, 3, 5)
    print(f"num_sum(num_min, 3, 5) = {result2}")
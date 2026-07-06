# 直接导入模块
import utils.function01
from utils.function01 import function1, function2, PI, E, NAME
from utils import function01
function01.function1()
function01.function2()
print(function01.PI)
print(function01.E)
print(function01.NAME)

utils.function01.function1()
utils.function01.function2()
print(utils.function01.PI)
print(utils.function01.E)
print(utils.function01.NAME)


# 导入模块的某一个功能
function1()
function2()
print(PI)
print(E)
print(NAME)

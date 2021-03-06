"""
    函数参数
        实际参数
            字典实参

        形式参数
            双星号字典形参
"""


def func01(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)


# 字典实参:将一个字典 拆分为 多个实参,按照名字对应
# 适用性:需要在其他环境中构建实参
dict01 = {"p2": 20, "p3": 30, "p1": 10}
func01(**dict01)

# 双星号字典形参:将多个关键字实参 合并为 一个字典
# 适用性:需要关键字实参数量无限
def func02(**kwargs):
    print(kwargs)

# 关键字实参
func02()
func02(p1=1, p2=2)

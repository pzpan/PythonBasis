# -*- coding = utf-8 -*-
# @Time : 2020/4/22  下午 12:51
# @Author : 潘
# @File : BasicDataType.py
# @Software : PyCharm
# @Description : 基本数据类型

"""
1. Python中变量是不需要声明, 但使用前必须进行赋值, 然后才能够使用
2. 变量是没有类型的, 但是值是有类型的
    可以使用type 函数来获取变量值的类型
    可以使用 isinstance 来检查变量值是否为某个类型
    这连个函数的区别是:
        type 不会认为子类是一种父类类型
        isinstance 认为子类是一种父类的类型
3. 变量赋值
    变量名 = 值 => 对变量进行赋值
    变量1 = 变量2 = 变量3 = 值  => 来对多个变量赋一样的值
    变量1, 变量2, 变量3 = 变量1的值, 变量2的值, 变量3的值 => 多个变量给予不同的值, 但是变量个数必须和值的个数一样
        a, b, c = 1, 3.1415 # 报错 ValueError: not enough values to unpack (expected 3, got 2)

"""

# 变量赋值
a = 1
print(f'a = {a}, a的类型是: {type(a)}, a的值是int类型吗? {isinstance(a, int)}')
print('-' * 20)
# 多个变量赋同一个值
a = b = c = '1'
print(f'a = {a}, a的类型是: {type(a)}, a的值是str类型吗? {isinstance(a, str)}')
print(f'b = {b}, b的类型是: {type(b)}, b的值是int类型吗? {isinstance(b, int)}')
print('-' * 20)
# 多个变量赋值不同的值
a, b, c, = 1, 3.1415, 'pan'
print(f'a的类型是: {type(a)}, b的类型是: {type(b)}, c的类型是: {type(c)}.')
print('-' * 20)


# type 和 isinstance的区别
class A:
    pass  # 占位, 啥用没有


class B(A):
    pass


class C(A):
    pass


print(f'type: B=A? {type(B()) == A}, C=A? {type(C()) == A}, B=C? {type(B()) == C}')
print(f'isinstance: B=A? {isinstance(B(), A)}, C=A?{isinstance(C(), A)}, B=C? {isinstance(B(), C)}')


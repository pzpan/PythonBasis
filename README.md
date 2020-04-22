# PythonBasis
# Python基础学习

## 基本数据类型

### 变量及变量赋值

> Python中的变量不需要进行声明
>
> 每个变量在使用前必须进行赋值
>
> 变量没有类型, 但变量的值有类型
>
> Python允许同时对多个变量进行赋值
>
> 变量1 = 变量2 = 变量3 = 1  # 多个变量赋值为同一个值
>
> 变量1, 变量2, 变量3 = 1, 3.1415, 'runoob'  # 多个变量赋值为不同的值

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

counter = 100  # 整型变量
miles = 1000.0  # 浮点数变量
name = 'runoob'  # 字符串变量

print(counter)
print(miles)
print(name)

a = b = c = 1
print(f'a = {a}, b = {b}, c = {c}')
a, b, c = 1, 3.1415, 'runoob'  # 多个变量分别赋值, 并且值的类型是不同的
print(f'a = {a}, b = {b}, c = {c}')
```

> 使用type函数来查看变量的类型,使用isinstance函数来检查变量的类型
>
> 它们的区别是:
>
> type 认为子类不等于父类
>
> isinstance 认为子类等于父类

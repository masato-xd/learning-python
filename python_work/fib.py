# coding: utf-8
# 斐波拉函数


def fib(max):
    n, a, b = (0, 0, 1)
    while n < max:
        print b
        a, b = b, a + b
        n = n + 1

fib(5)

# 列表生成式
l = [x * x for x in range(10)]
print l

"""
https://en.wikipedia.org/wiki/Exponentiation_by_squaring
method for fast computation of large positive integer powers of a number
"""


def exp_by_sq(x: int, n: int) -> int:
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n % 2 == 0:
        return exp_by_sq(x * x, n // 2)
    else:
        return x * exp_by_sq(x * x, (n - 1) // 2)


def naive_exp(x: int, n: int) -> int:
    result = x
    for _ in range(n - 1):
        result *= x
    return result


# example
print('example')
print(exp_by_sq(2, 10))
print(naive_exp(2, 10))

print('timing')
import timeit
print('by sq', timeit.timeit('exp_by_sq(2, 100)', setup="from __main__ import exp_by_sq"))
print('naive', timeit.timeit('naive_exp(2, 100)', setup="from __main__ import naive_exp"))

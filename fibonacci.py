import time
from functools import lru_cache, reduce
from math import sqrt

import numpy as np

cache = {1: 1}


def timer(func):
    start = time.perf_counter()
    print(func)
    timing = ((time.perf_counter() - start) * 1000000)
    print(f'Elapsed time {timing} microseconds')
    return


def fib0(n):
    """
    fibonacci number until n with only recursion but without cache
    """
    if n < 2:
        return n
    result = fib1(n - 2) + fib1(n - 1)
    return result


def fib1(n):
    """
    fibonacci number until n with recursion and simple cache
    """
    if n in cache:
        return cache[n]
    if n < 2:
        return n
    result = fib1(n - 2) + fib1(n - 1)
    cache[n] = result
    return result


@lru_cache(maxsize=None)
def fib2(n):
    """
    fibonacci number until n with recursion and lru cache
    """
    if n < 2:
        return n
    result = fib1(n - 2) + fib1(n - 1)
    return result


def fib3(n):
    """
    fibonacci until n without any recursion/cache. Simple and surprisingly not slow.
    """
    if n <= 1:
        return n
    fibonacci_current = 1
    fibonacci_previous = 1
    for i in range(2, n):
        fibonacci_previous, fibonacci_current = fibonacci_current, fibonacci_current + fibonacci_previous
    return fibonacci_current


def fib5(n):
    """
    With numpy and arrays. Very slow. Almost brute.
    """
    fib = np.array([0, 1], dtype=object)
    for i in range(2, n + 1):
        fib = np.append(fib, fib[-2] + fib[-1])
    return fib[-1]


def fib6(n):
    """
    with reduce
    """
    return reduce(lambda x, n: [x[1], x[0] + x[1]], range(n), [0, 1])[0]


def fib8(n):
    """
    with powers
    """
    return pow(2 << n, n + 1, (4 << 2 * n) - (2 << n) - 1) % (2 << n)


def fib9(n):
    """
    with generator
    """
    for x in fibonacci_gen(n):
        if x < 3:
            pass
    return x


def fibonacci_gen(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


def is_fibonacci(n):
    """
    Check is it correct Fibonacci number.
    This is true if and only if at least one of 5x^2+4 or 5x^2-4 is a perfect square.
    """
    return True if sqrt(5 * (n ** 2) - 4) % 1 == 0 or sqrt(5 * (n ** 2) + 4) % 1 == 0 else False


def find_sequence_number(value):
    """
    find number in sequence
    """
    if value == 0:
        return 0
    fibonacci_previous, fibonacci_next = 0, 1
    n = 1
    while fibonacci_next <= value:
        if fibonacci_next == value:
            return n
        fibonacci_previous, fibonacci_next = fibonacci_next, fibonacci_previous + fibonacci_next
        n += 1
    return -1


def main():
    n = 101

    timer(fib0(n))
    timer(fib1(n))
    timer(fib2(n))
    timer(fib3(n))
    timer(fib5(n))
    timer(fib6(n))
    timer(fib8(n))
    timer(fib9(n))

    position = 15
    a1_position = find_sequence_number(354224848179261915075)
    a2_position = find_sequence_number(573147844013817084101)
    new_number = fib8(a1_position + position)
    print(is_fibonacci(new_number))
    print(new_number)


if __name__ == "__main__":
    main()

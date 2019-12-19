"""
Version1
Calculating the n-th term of the Fibonacci series.
With eight variants of calculating the series itself (yes, you can painlessly remove seven of them).
"""

from functools import lru_cache, reduce
from math import sqrt

import numpy as np

cache = {1: 1}


def recursion(number):
    """
    Fibonacci number until n with only recursion but without cache. Very slow.
    With n greater than 50 it can take almost forever to count.
    """
    if number in (1, 2):
        return 1
    return recursion(number - 1) + recursion(number - 2)


def cache_recursion(number):
    """
    Fibonacci number until n with recursion and simple cache
    """
    if number in cache:
        return cache[number]
    if number in (1, 2):
        return 1
    result = cache_recursion(number - 2) + cache_recursion(number - 1)
    cache[number] = result
    return result


@lru_cache(maxsize=None)
def lru_cache_recursion(number):
    """
    Fibonacci number until n with recursion and lru cache
    """
    if number in (1, 2):
        return 1
    return lru_cache_recursion(number - 2) + lru_cache_recursion(number - 1)


def simple(number):
    """
    Fibonacci until n without any recursion/cache. Simple and surprisingly not slow.
    """
    if number in (1, 2):
        return 1
    fibonacci_previous = fibonacci_current = 1
    for _ in range(2, number):
        fibonacci_previous, fibonacci_current = fibonacci_current, fibonacci_current + \
            fibonacci_previous
    return fibonacci_current


def np_array(number):
    """
    With numpy and arrays. Very slow. Almost brute.
    """
    fib = np.array([0, 1], dtype=object)
    for _ in range(2, number + 1):
        fib = np.append(fib, fib[-2] + fib[-1])
    return fib[-1]


def f_reduce(number):
    """
    With reduce
    """
    return reduce(lambda x, t: [x[1], x[0] + x[1]], range(number), [0, 1])[0]


def powers_shift(number):
    """
    With powers
    """
    return pow(2 << number, number + 1, (4 << 2 * number) - (2 << number) - 1) % (2 << number)


def generator_series(number):
    """
    With generator
    """
    for pos_number in fibonacci_gen(number):
        if pos_number < 3:
            pass
    return pos_number


def fibonacci_gen(number):
    """
    Generator itself. Formally it's modified version of usual loop with summary Fn and Fn+1
    """
    fibonacci_current = fibonacci_previous = 1
    for _ in range(number):
        yield fibonacci_current
        fibonacci_current, fibonacci_previous = fibonacci_previous, \
            fibonacci_current + fibonacci_previous


def is_fibonacci(number):
    """
    Check is it correct Fibonacci number.
    This is true if and only if at least one of 5x^2+4 or 5x^2-4 is a perfect square.
    """
    return sqrt(5 * (number ** 2) - 4) % 1 == 0 or sqrt(5 * (number ** 2) + 4) % 1 == 0


def position(value):
    """
    Find number in sequence
    """
    if value == 0:
        return 0
    fibonacci_previous, fibonacci_next = 0, 1
    counter = 1
    while fibonacci_next <= value:
        if fibonacci_next == value:
            return counter
        fibonacci_previous, fibonacci_next = fibonacci_next, fibonacci_previous + fibonacci_next
        counter += 1
    return -1


def next_seq(steps, fibonacci_previous, fibonacci_current):
    """
    Find next n numbers in fibonacci sequence. Simular to fib3.
    """
    for _ in range(steps):
        fibonacci_previous, fibonacci_current = fibonacci_current, fibonacci_current + \
            fibonacci_previous
    return fibonacci_current


def main():
    """
    Main function
    a1 - Fn number of sequence
    a2 - Fn+1 number of sequence
    n - length of sequence

    Calculating the n-th term of the Fibonacci series with simply loop as Fn+2 = Fn + Fn+1,
    i.e. Fn+2 = a1 + a2 and so on

    Other functions are only called to check input values
    """
    # 354224848179261915075 573147844013817084101 10
    # a1 = 354224848179261915075
    # a2 = 573147844013817084101
    # n = 10
    while True:
        previous = current = steps = 1
        try:
            previous, current, steps = map(int,
                                           input("""[to quit - press Ctrl-C]
                                                 Enter space separated a1 a2 n: """)
                                           .split())
        except ValueError:
            print('Enter values in numeric format')

        if is_fibonacci(previous) and is_fibonacci(current):
            if position(previous) + 1 == position(current):
                print(next_seq(steps, previous, current))
            else:
                print(
                    "That's correct Fibonacci's numbers, but they not in a correct sequence")
        else:
            print('Something goes wrong. Enter correct Fibonacci numbers')


if __name__ == "__main__":
    main()

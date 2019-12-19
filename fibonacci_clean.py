"""
Version 4
Not quite consistent with PEP8 in the docstring part
"""

from math import sqrt


def next_seq(steps, fibonacci_previous, fibonacci_current):
    for _ in range(steps):
        fibonacci_previous, fibonacci_current = fibonacci_current, fibonacci_current + \
                                                fibonacci_previous
    return fibonacci_current


def is_fibonacci(number):
    return sqrt(5 * (number ** 2) - 4) % 1 == 0 or sqrt(5 * (number ** 2) + 4) % 1 == 0


def position(number):
    if number == 0:
        return 0
    fibonacci_previous, fibonacci_next = 0, 1
    count = 1
    while fibonacci_next <= number:
        if fibonacci_next == number:
            return count
        fibonacci_previous, fibonacci_next = fibonacci_next, fibonacci_previous + fibonacci_next
        count += 1
    return -1


def is_data_correct(previous, current, steps):
    return is_fibonacci(previous) and is_fibonacci(current) and \
           is_right_sequence(previous, current) and steps > 0


def is_right_sequence(previous, current):
    return position(previous) + 1 == position(current)


def main():
    while True:
        previous = current = steps = 1
        try:
            previous, current, steps = map(int, input('Enter space separated a1 a2 n: ').split())
        except ValueError:
            print('Enter values in numeric format')

        if is_data_correct(previous, current, steps):
            final = next_seq(steps, previous, current)
            print(final)


if __name__ == '__main__':
    main()

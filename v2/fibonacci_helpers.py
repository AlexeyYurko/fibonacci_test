from math import sqrt


def next_seq(n, fibonacci_previous, fibonacci_current):
    for _ in range(n):
        fibonacci_previous, fibonacci_current = fibonacci_current, fibonacci_current + \
                                                fibonacci_previous
    return fibonacci_current


def is_fibonacci(number):
    """
    Check is it correct Fibonacci number.
    This is true if and only if at least one of 5x^2+4 or 5x^2-4 is a perfect square.
    """
    return sqrt(5 * (number ** 2) - 4) % 1 == 0 or sqrt(5 * (number ** 2) + 4) % 1 == 0


def position(number):
    """
    find number in sequence with summary in loop
    """
    if number == 0:
        return 0
    fibonacci_previous, fibonacci_next = 0, 1
    n = 1
    while fibonacci_next <= number:
        if fibonacci_next == number:
            return n
        fibonacci_previous, fibonacci_next = fibonacci_next, fibonacci_previous + fibonacci_next
        n += 1
    return -1


class DataValidator:
    def __init__(self, line):
        self.line = line
        try:
            self.a1, self.a2, self.n = map(int, line.split())
        except ValueError:
            print('Enter values in numeric format')
            exit()

    def is_data_correct(self):
        return is_fibonacci(self.a1) and is_fibonacci(self.a2) and self.is_right_sequence() and self.n > 0

    def is_right_sequence(self):
        return position(self.a1) + 1 == position(self.a2)

    @property
    def values(self):
        return self.n, self.a1, self.a2

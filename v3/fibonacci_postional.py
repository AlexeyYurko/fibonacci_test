"""
Version 3
Lack of fantasy.
Find the position of a2 in Fibonacci sequence and calculate the A2pos + n value.
Not optimal, but we don't need a1.
"""

from math import sqrt


def fibonacci(number):
    """
    With powers
    """
    return pow(2 << number, number + 1, (4 << 2 * number) - (2 << number) - 1) % (2 << number)


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
    count = 1
    while fibonacci_next <= number:
        if fibonacci_next == number:
            return count
        fibonacci_previous, fibonacci_next = fibonacci_next, fibonacci_previous + fibonacci_next
        count += 1
    return -1


def is_data_correct(previous, current, steps):
    """
    Check the entered data for 'fibbonacy' and control is the a1 .. a2 are right sequence or not
    """
    return is_fibonacci(previous) and is_fibonacci(current) and \
           is_right_sequence(previous, current) and steps > 0


def is_right_sequence(previous, current):
    """
    and control is the a1 .. a2 are right sequence or not
    by finding and compare positions of both
    """
    return position(previous) + 1 == position(current)


def main():
    """
    Main function
    a1 - Fn number of sequence
    a2 - Fn+1 number of sequence
    n - length of sequence

    Calculation of the nth term of the Fibonacci series by determining the position a2
    and calculating the series by the formula A2pos+N
    """
    while True:
        previous = current = steps = 1
        try:
            previous, current, steps = map(int, input('Enter space separated a1 a2 n: ').split())
        except ValueError:
            print('Enter values in numeric format')

        if is_data_correct(previous, current, steps):
            final = fibonacci(position(current) + steps)
            print(final)


if __name__ == '__main__':
    main()

"""
Version2
Pseudo-OOP version of calculating the n-th term of the Fibonacci series.
Why pseudo? Because in this case it's seems little over.
Where is no DRY, most functions/methods are same as in the fibonacci_procedure.py
"""

from fibonacci_helpers import DataValidator, next_seq


def main():
    """
    Main function
    a1 - Fn number of sequence
    a2 - Fn+1 number of sequence
    n - length of sequence

    Calculating the n-th term of the Fibonacci series with simply loop as Fn+2 = Fn + Fn+1,
    i.e. Fn+2 = a1 + a2 and so on
    """
    # 354224848179261915075 573147844013817084101 10
    # a1 = 354224848179261915075
    # a2 = 573147844013817084101
    # n = 10

    while True:
        line = input('[to quit - press Ctrl-C] Enter space separated a1 a2 n: ')
        validate = DataValidator(line)
        if validate.is_data_correct():
            solver = next_seq(*validate.values)
            print(solver)


if __name__ == "__main__":
    main()

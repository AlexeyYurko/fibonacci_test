import fibonacci_procedure

ten = 55
fifty = 12586269025
hundred = 354224848179261915075

small = 10
middle = 50
large = 100


class TestClass:
    def test_fib0(self):
        """
        Due to extra slow nature of this variant check only 10th
        """
        assert ten == fibonacci_procedure.recursion(10)

    def test_fib1(self):
        assert ten == fibonacci_procedure.lru_cache_recursion(small)
        assert fifty == fibonacci_procedure.lru_cache_recursion(middle)
        assert hundred == fibonacci_procedure.lru_cache_recursion(large)

    def test_fib2(self):
        assert ten == fibonacci_procedure.cache_recursion(small)
        assert fifty == fibonacci_procedure.cache_recursion(middle)
        assert hundred == fibonacci_procedure.cache_recursion(large)

    def test_fib3(self):
        assert ten == fibonacci_procedure.simple(small)
        assert fifty == fibonacci_procedure.simple(middle)
        assert hundred == fibonacci_procedure.simple(large)

    def test_fib5(self):
        assert ten == fibonacci_procedure.np_array(small)
        assert fifty == fibonacci_procedure.np_array(middle)
        assert hundred == fibonacci_procedure.np_array(large)

    def test_fib6(self):
        assert ten == fibonacci_procedure.f_reduce(small)
        assert fifty == fibonacci_procedure.f_reduce(middle)
        assert hundred == fibonacci_procedure.f_reduce(large)

    def test_fib8(self):
        assert ten == fibonacci_procedure.powers_shift(small)
        assert fifty == fibonacci_procedure.powers_shift(middle)
        assert hundred == fibonacci_procedure.powers_shift(large)

    def test_fib9(self):
        assert ten == fibonacci_procedure.generator_series(small)
        assert fifty == fibonacci_procedure.generator_series(middle)
        assert hundred == fibonacci_procedure.generator_series(large)

    def test_is_fibonacci(self):
        assert fibonacci_procedure.is_fibonacci(ten)
        assert fibonacci_procedure.is_fibonacci(fifty)
        assert fibonacci_procedure.is_fibonacci(hundred)
        assert fibonacci_procedure.is_fibonacci(fibonacci_procedure.np_array(large))
        assert not fibonacci_procedure.is_fibonacci(10)
        assert not fibonacci_procedure.is_fibonacci(12311233)

    def test_position(self):
        assert fibonacci_procedure.position(ten) == small
        assert fibonacci_procedure.position(fifty) == middle
        assert fibonacci_procedure.position(hundred) == large

    def test_next_seq(self):
        assert fibonacci_procedure.next_seq(1, 8, 13) == 21

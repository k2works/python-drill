import unittest
import doctest
from typing import Any

# %% [markdown]
# # 再帰的アルゴリズム
# %%

# %% [markdown]
# ## 再帰の基本


class TestFactorial(unittest.TestCase):
    def test_3の階乗は6であること(self):
        self.assertEqual(factorial(3), 6)


def factorial(n: int) -> int:
    """
    非負の整数の階乗値を求める
    >>> factorial(3)
    6
    """
    if n > 0:
        return n * factorial(n - 1)
    else:
        return 1


class TestGcd(unittest.TestCase):
    def test_22と8の最大公約数は2であること(self):
        self.assertEqual(gcd(22, 8), 2)


def gcd(x: int, y: int) -> int:
    """
    ユークリッドの互除法を用いて、xとyの最大公約数を求める。
    >>> gcd(22, 8)
    2
    """
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

# %% [markdown]
# ## ハノイの塔

# %% [markdown]
# ## 8王妃問題


doctest.testmod(verbose=True)
unittest.main(argv=[''], verbosity=2, exit=False)

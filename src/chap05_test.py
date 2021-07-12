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

# %% [markdown]
# ## ハノイの塔

# %% [markdown]
# ## 8王妃問題

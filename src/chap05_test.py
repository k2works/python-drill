import unittest
import doctest
from typing import Any
from chap04_test import Stack

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


class TestRecur(unittest.TestCase):
    def test_実行結果を配列で返すこと(self):
        self.assertEqual(recur(4, []), [1, 2, 3, 1, 4, 1, 2])

    def test_末尾再帰を除去した実行結果を配列で返すこと(self):
        self.assertEqual(recur2(4, []), [1, 2, 3, 1, 4, 1, 2])

    def test_スタックを用いて末尾再帰を除去した実行結果を配列で返すこと(self):
        self.assertEqual(recur3(4, []), [1, 2, 3, 1, 4, 1, 2])


def recur(n: int, result: list) -> list:
    """真に再帰的な関数

    >>> recur(4, [])
    [1, 2, 3, 1, 4, 1, 2]
    """
    if n > 0:
        recur(n - 1, result)
        result.append(n)
        recur(n - 2, result)

    return result

def recur2(n: int, result: list) -> list:
    """末尾再帰を除去した関数

    >>> recur2(4, [])
    [1, 2, 3, 1, 4, 1, 2]
    """
    while n > 0:
        recur(n - 1, result)
        result.append(n)
        n = n - 2

    return result

def recur3(n: int, result: list) -> list:
    """スタックを用いて末尾再帰を除去した関数

    >>> recur3(4, [])
    [1, 2, 3, 1, 4, 1, 2]
    """
    s = Stack(n)

    while True:
        if n > 0:
            s.push(n)
            n = n - 1
            continue
        if not s.is_empty():
            n = s.pop()
            result.append(n)
            n = n - 2
            continue
        break

    return result

# %% [markdown]
# ## ハノイの塔

# %% [markdown]
# ## 8王妃問題


doctest.testmod(verbose=True)
unittest.main(argv=[''], verbosity=2, exit=False)

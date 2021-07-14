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


class TestMove(unittest.TestCase):
    def test_円盤3枚(self):
        excepted = [
            '円盤[1]を1軸から3軸へ移動',
            '円盤[2]を1軸から2軸へ移動',
            '円盤[1]を3軸から2軸へ移動',
            '円盤[3]を1軸から3軸へ移動',
            '円盤[1]を2軸から1軸へ移動',
            '円盤[2]を2軸から3軸へ移動',
            '円盤[1]を1軸から3軸へ移動'
        ]
        actual = move(3, 1, 3, [])
        self.assertEquals(actual, excepted)


def move(no: int, x: int, y: int, result: list) -> list:
    """no枚の円盤x軸からy軸へ移動
    >>> move(3, 1, 3, [])
    ['円盤[1]を1軸から3軸へ移動', '円盤[2]を1軸から2軸へ移動', '円盤[1]を3軸から2軸へ移動', '円盤[3]を1軸から3軸へ移動', '円盤[1]を2軸から1軸へ移動', '円盤[2]を2軸から3軸へ移動', '円盤[1]を1軸から3軸へ移動']
    """
    if no > 1:
        move(no - 1, x, 6 - x - y, result)

    result.append(f'円盤[{no}]を{x}軸から{y}軸へ移動')

    if no > 1:
        move(no - 1, 6 - x - y, y, result)

    return result


# %% [markdown]
# ## 8王妃問題


doctest.testmod(verbose=True)
unittest.main(argv=[''], verbosity=2, exit=False)

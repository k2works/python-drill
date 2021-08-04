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

class TestEightQueen(unittest.TestCase):
    def test_各列に1個の王妃を配置する組み合わせを再帰的に列挙(self):
        eight_queen = EightQueen()
        eight_queen.set(0)
        self.assertEqual(len(eight_queen.result), 16777216)

    def test_各列に1個の王妃を配置する組み合わせを再帰的に列挙2(self):
        eight_queen = EightQueen2()
        eight_queen.set(0)
        self.assertEqual(len(eight_queen.result), 40320)

    def test_8王妃問題を解くプログラム(self):
        eight_queen = EightQueen3()
        eight_queen.set(0)
        self.assertEqual(len(eight_queen.result), 92)


class EightQueen:
    def __init__(self) -> None:
        self.result = []
        self.__pos = [0] * 8

    def set(self, i:int) -> None:
        """i列目に王妃を配置"""
        for j in range(8):
            self.__pos[i] = j
            if i == 7:
                self.put()
            else:
                self.set(i + 1)

    def put(self) -> None:
        """盤面(各列の王妃の位置)"""
        row = []
        for i in range(8):
            row.append(self.__pos[i])
        self.result.append(row)


class EightQueen2:
    def __init__(self) -> None:
        self.result = []
        self.__pos = [0] * 8
        self.__flag = [False] * 8

    def set(self, i: int) -> None:
        """i列目の適切な位置に王妃を配置"""
        for j in range(8):
            if not self.__flag[j]:
                self.__pos[i] = j
                if i == 7:
                    self.put()
                else:
                    self.__flag[j] = True
                    self.set(i + 1)
                    self.__flag[j] = False

    def put(self) -> None:
        """盤面(各列の王妃の位置)"""
        row = []
        for i in range(8):
            row.append(self.__pos[i])
        self.result.append(row)


class EightQueen3:
    def __init__(self) -> None:
        self.result = []
        self.__pos = [0] * 8
        self.__flag_a = [False] * 8
        self.__flag_b = [False] * 15
        self.__flag_c = [False] * 15

    def set(self, i: int) -> None:
        """i列目の適切な位置に王妃を配置"""
        for j in range(8):
            if (not self.__flag_a[j]
                and not self.__flag_b[i + j]
                    and not self.__flag_c[i - j + 7]):
                self.__pos[i] = j
                if i == 7:
                    self.put()
                    self.put2()
                else:
                    self.__flag_a[j] = self.__flag_b[i +
                                                     j] = self.__flag_c[i - j + 7] = True
                    self.set(i + 1)
                    self.__flag_a[j] = self.__flag_b[i +
                                                     j] = self.__flag_c[i - j + 7] = False

    def put(self) -> None:
        """盤面(各列の王妃の位置)"""
        row = []
        for i in range(8):
            row.append(self.__pos[i])
        self.result.append(row)

    def put2(self) -> None:
        """盤面を□と■で出力"""
        for j in range(8):
            for i in range(8):
                print('■' if self.__pos[i] == j else '□', end='')
            print()
        print()



doctest.testmod(verbose=True)
unittest.main(argv=[''], verbosity=2, exit=False)

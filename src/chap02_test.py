# %% [markdown]
# # データ構造と配列
# %%
import doctest
from typing import Any, MutableSequence, Sequence
import unittest
from unittest import result
from unittest.case import skip
import functools

# %% [markdown]
# ## データ構造と配列

# %% [markdown]
# ### 配列の必要性


class TestTotal(unittest.TestCase):
    def test_5人の点数を読み込んで合計点平均点を返す(self):
        self.assertEqual(total([32, 68, 72, 54, 92]), '318,63.6')


def total(tensu_list):
    """ 5人の点数を読み込んで合計点平均点を返す

    >>> total([32,68,72,54,92])
    '318,63.6'
    """
    total = functools.reduce(
        lambda a, b: a+b, tensu_list)
    mean = total/len(tensu_list)
    result = ','.join([str(i) for i in [total, mean]])

    return result


# %% [markdown]
# ## 配列

# %% [markdown]
# ### シーケンスの要素の最大値を表示する

class TestMax(unittest.TestCase):
    def test_シーケンスaの要素の最大値を返却する(self):
        self.assertEqual(max_of([172, 153, 192, 140, 165]), 192)


def max_of(a: Sequence) -> Any:
    """ シーケンスaの要素の最大値を返却する

    >>> max_of([172, 153, 192, 140, 165])
    192
    """
    return max(a)

# %% [markdown]
# ### ミュータブルなシーケンスの要素の並びを反転

class TestReverseArray(unittest.TestCase):
    def test_ミュータブルなシーケンスaの要素の並びを反転(self):
        a = [2, 5, 1, 3, 9, 6, 7]
        reverse_array_mutable(a)
        self.assertEqual(a, [7, 6, 9, 3, 1, 5, 2])

    def test_イミュータブルなシーケンスaの要素の並びを反転(self):
        a = [2, 5, 1, 3, 9, 6, 7]
        result = reverse_array_imutable(a)

        self.assertEqual(a, [2, 5, 1, 3, 9, 6, 7])
        self.assertEqual(result, [7, 6, 9, 3, 1, 5, 2])


def reverse_array(配列: MutableSequence) -> None:
    配列の長さ = len(配列)
    配列の半分の長さ = (配列の長さ // 2)
    def 両端の数値を交換した配列(配列, n, i): return 配列[n - i - 1], 配列[i]
    def 配列の要素の並びを反転(配列, n, i): 配列[i], 配列[n - i - 1] = 両端の数値を交換した配列(配列, 配列の長さ, i)

    [配列の要素の並びを反転(配列, 配列の長さ, i) for i in range(配列の半分の長さ)]


def reverse_array_mutable(配列: MutableSequence) -> None:
    """ ミュータブルなシーケンスの要素の並びを反転
    """
    reverse_array(配列)


def reverse_array_imutable(a: MutableSequence) -> MutableSequence:
    """ イミュータブルなシーケンスの要素の並びを反転
    """
    配列 = a[:]
    reverse_array(配列)
    return 配列

# %% [markdown]
# ### 基数変換


class TestCardConv(unittest.TestCase):
    def test_整数値xをr進数に変換した数値を表す文字列を返却(self):
        self.assertEqual(card_conv(29, 2), '11101')

def card_conv(x: int, r: int) -> str:
    """ 整数値xをr進数に変換した数値を表す文字列を返却

    >>> card_conv(29, 2)
    '11101'
    """
    def 反転して返却(d): return d[::-1]

    def 該当文字を取り出して連結(x, r):
        d = ''
        dchar = '0123456789ACDEFGHIJKLMNOPQRSTUVWXYZ'
        while x > 0:
            d += dchar[x % r]
            x //= r 
        return d

    連結文字列 = 該当文字を取り出して連結(x, r)
    return 反転して返却(連結文字列)

# %% [markdown]
# ### 素数の列挙

class TestPrime(unittest.TestCase):
    def test_x以下の素数を列挙_1(self):
        self.assertEqual(prime_1(1000), 78022)

    def test_x以下の素数を列挙_2(self):
        self.assertEqual(prime_2(1000), 14622)

    def test_x以下の素数を列挙_3(self):
        self.assertEqual(prime_3(1000), 3774)

def prime_1(x: int) -> int:
    """ x以下の素数を列挙（第1版）
    """
    counter = 0
    for n in range(2, x+1):
        for i in range(2, n):
            counter += 1
            if n % i == 0:
                break
        else:
            print(n)

    return counter

def prime_2(x: int) -> int:
    """ x以下の素数を列挙（第2版）
    """
    counter = 0
    ptr = 0
    prime = [None] * 500

    prime[ptr] = 2
    ptr += 1

    for n in range(3, x+1, 2):
        for i in range(1, ptr):
            counter += 1
            if n % prime[i] == 0:
                break
        else:
            print(n)
            prime[ptr] = n
            ptr += 1

    return counter


def prime_3(x: int) -> int:
    """ x以下の素数を列挙（第3版）
    """
    counter = 0
    ptr = 0
    prime = [None] * 500

    prime[ptr] = 2
    ptr += 1
    prime[ptr] = 3
    ptr += 1

    for n in range(5, 1001, 2):
        i = 1
        while prime[i] * prime[i] <= n:
            counter += 2
            if n % prime[i] == 0:
                break
            i += 1
        else:
            print(n)
            prime[ptr] = n
            ptr += 1
            counter += 1

    return counter

doctest.testmod(verbose=True)
unittest.main(argv=[''], verbosity=2, exit=False)

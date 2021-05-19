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


def reverse_array(配列):
    配列の長さ = len(配列)
    配列の半分の長さ = (配列の長さ // 2)
    def 両端の数値を交換した配列(配列, n, i): return 配列[n - i - 1], 配列[i]
    def 配列の要素の並びを反転(配列, n, i): 配列[i], 配列[n - i - 1] = 両端の数値を交換した配列(配列, 配列の長さ, i)

    [配列の要素の並びを反転(配列, 配列の長さ, i) for i in range(配列の半分の長さ)]


def reverse_array_mutable(配列: MutableSequence) -> None:
    """ ミュータブルなシーケンスの要素の並びを反転
    """
    reverse_array(配列)


def reverse_array_imutable(a: MutableSequence) -> None:
    """ イミュータブルなシーケンスの要素の並びを反転
    """
    配列 = a[:]
    reverse_array(配列)
    return 配列

doctest.testmod(verbose=True)
unittest.main(argv=[''], verbosity=2, exit=False)

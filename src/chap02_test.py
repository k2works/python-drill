# %% [markdown]
# # データ構造と配列
# %%
import doctest
from typing import Any, Sequence
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
    def aがbより大きい(a, b): return True if a > b else False
    maximum = [int(a[i]) for i in range(1, len(a)) if aがbより大きい(a[i], a[0])][0]
    return maximum


doctest.testmod(verbose=True)
unittest.main(argv=[''], verbosity=2, exit=False)

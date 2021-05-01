# %% [markdown]
#　アルゴリズムとは
# %%
import unittest
import doctest
# %% [markdown]
# ## 3値の最大値
#
# 1. maximumにaの値を代入する。
# 1. bの値がmaximumよりも大きければ、maximumにbの値を代入する。
# 1. cの値がmaximumよりも大きければ、maximumにcの値を代入する。
#
# 実行例
#
#     三つの整数の最大値を求めます。
#     整数aの値 : 1
#     整数bの値 : 3
#     整数cの値 : 2


class TestMax3(unittest.TestCase):
    def test_max(self):
        for a, b, c, ans in [
            (3, 2, 1, 3),
            (3, 2, 2, 3),
            (3, 1, 2, 3),
            (3, 2, 3, 3),
            (2, 1, 3, 3),
            (3, 3, 2, 3),
            (3, 3, 3, 3),
            (2, 2, 3, 3),
            (2, 3, 1, 3),
            (2, 3, 2, 3),
            (1, 3, 2, 3),
            (2, 3, 3, 3),
            (1, 2, 3, 3),
        ]:
            with self.subTest(a=a, b=b, c=c, ans=ans):
                self.assertEqual(max3(a, b, c), ans)


def max3(a, b, c):
    """3つの整数値を読み込んで最大値を求めて表示

    >>> max3(1, 3, 2)
    3
    """
    maximum = a
    if b > maximum:
        maximum = b
    if c > maximum:
        maximum = c

    return maximum


doctest.testmod(verbose=True)
unittest.main(argv=[''], verbosity=2, exit=False)

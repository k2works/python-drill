
# %% [markdown]
# # 探索
# %%
import doctest
import unittest
from unittest import result
from unittest.case import skip
from typing import Any, MutableSequence, Sequence
import copy

# %% [markdown]
# ## 線形探索

# %% [markdown]
# ### 線形探索

class TestSearch(unittest.TestCase):
    def test_シーケンスaからkeyと等価な要素を線形探索_1(self):
        self.assertEqual(ssearch_while([6, 4, 3, 2, 1, 2, 8], 2), 3)
        self.assertEqual(ssearch_while([12.7, 3.14, 6.4, 7.2, 'End'], 6.4), 2)
        self.assertEqual(ssearch_while((4, 7, 5.6, 2, 3.14, 1), 5.6), 2)
        self.assertEqual(ssearch_while(['DTS', 'AAC', 'FLAC'], 'DTS'), 0)

    def test_シーケンスaからkeyと等価な要素を線形探索_2(self):
        self.assertEqual(ssearch_for([6, 4, 3, 2, 1, 2, 8], 9), -1)
        self.assertEqual(ssearch_for([6, 4, 3, 2, 1, 2, 8], 2), 3)
        self.assertEqual(ssearch_for([12.7, 3.14, 6.4, 7.2, 'End'], 6.4), 2)
        self.assertEqual(ssearch_for((4, 7, 5.6, 2, 3.14, 1), 5.6), 2)
        self.assertEqual(ssearch_for(['DTS', 'AAC', 'FLAC'], 'DTS'), 0)

def ssearch_while(a: Sequence, key: Any) -> int:
    """シーケンスaからkeyと等価な要素を線形探索(while文)
    >>> ssearch_while([6, 4, 3, 2, 1, 2, 8], 2)
    3
    """
    i = 0
    def シーケンスと同じ長さ(a, i): return True if i == len(a) else False
    def シーケンス要素とキーが同じ(a, key): return True if a[i] == key else False

    while True:
        if シーケンスと同じ長さ(a, i):
            return -1
        if シーケンス要素とキーが同じ(a, key):
            return i
        i += 1


def ssearch_for(a: Sequence, key: Any) -> int:
    """シーケンスaからkeyと等価な要素を線形探索(for文)
    >>> ssearch_for([6, 4, 3, 2, 1, 2, 8], 2)
    3
    """
    def シーケンス要素とキーが同じ(a, key): return True if a == key else False
    def 結果を返す(list): return -1 if not list else list[0]

    検索結果 = [i for i in range(len(a)) if シーケンス要素とキーが同じ(a[i], key)]
    return 結果を返す(検索結果)

# %% [markdown]
# ### 線形探索(番兵法)


class TestSsearchSentinel(unittest.TestCase):
    def test_シーケンスからキーに一致する要素を線形検索_番兵法(self):
        self.assertEqual(ssearch_sentinel([6, 4, 3, 2, 1, 2, 8], 2), 3)

def ssearch_sentinel(seq: Sequence, key: Any) -> int:
    """シーケンスseqからkeyと一致する要素を線形探索（番兵法）

    >>> ssearch_sentinel([6, 4, 3, 2, 1, 2, 8], 2)
    3
    """
    def キーと一致する(v, key): return True if v == key else False
    def シーケンスの最後か判定する(i, seq): return -1 if i == len(seq) else i

    def シーケンスのコピー(seq, key):
        tmp = copy.deepcopy(seq)
        tmp.append(key)
        return tmp

    番兵を追加したシーケンスのコピー = シーケンスのコピー(seq, key)
    i = 0
    while True:
        if キーと一致する(番兵を追加したシーケンスのコピー[i], key):
            break
        i += 1
    return シーケンスの最後か判定する(i, seq)

# %% [markdown]
# ### 二分探索

class TestBsearch(unittest.TestCase):
    def test_シーケンスからキーに一致する要素を二分検索(self):
        self.assertEqual(bsearch([1, 2, 3, 5, 7, 8, 9], 5), 3)
        self.assertEqual(bsearch([1, 2, 3, 5, 7, 8, 9], 7), 4)
        self.assertEqual(bsearch([1, 2, 3, 5, 7, 8, 9], 3), 2)


def bsearch(a: Sequence, key: Any) -> int:
    """シーケンスaからkeyと一致する要素を二分検索

    >>> bsearch([1, 2, 3, 5, 7, 8, 9], 5)
    3
    """
    def 中間位置の値は検索値と一致する(中間位置の値, 検索値): return 中間位置の値 == 検索値
    def 中間位置の値は検索値より少ない(中間位置の値, 検索値): return 中間位置の値 < 検索値
    def 開始位置を一つ進める(中間位置):  return 中間位置 + 1
    def 開始位置を一つ戻す(中間位置): return 中間位置 - 1
    def 検索終了(開始位置, 終了位置): 開始位置 > 終了位置

    def 開始位置と終了位置を調整する(中間位置の値, 検索値, 開始位置, 終了位置):
        if 中間位置の値は検索値より少ない(a[中間位置], key):
            開始位置 = 開始位置を一つ進める(中間位置)
        else:
            終了位置 = 開始位置を一つ戻す(中間位置)
        return 開始位置, 終了位置


    開始位置 = 0
    終了位置 = len(a) - 1

    while True:
        中間位置 = (開始位置 + 終了位置) // 2
        if 中間位置の値は検索値と一致する(a[中間位置], key):
            return 中間位置

        開始位置, 終了位置 = 開始位置と終了位置を調整する(a[中間位置], key, 開始位置,終了位置)

        if 検索終了(開始位置,終了位置):
            break
    return -1


doctest.testmod(verbose=True)
unittest.main(argv=[''], verbosity=2, exit=False)

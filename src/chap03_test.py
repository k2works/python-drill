
# %% [markdown]
# # 探索
# %%
import doctest
import unittest
from unittest import result
from unittest.case import skip
from typing import Any, MutableSequence, Sequence

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
    ret = [i for i in range(len(a)) if シーケンス要素とキーが同じ(a[i], key)]
    if not ret:
        return -1
    else:
        return ret[0]

doctest.testmod(verbose=True)
unittest.main(argv=[''], verbosity=2, exit=False)

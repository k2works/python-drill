
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

def ssearch_while(a: Sequence, key: Any) -> int:
    """シーケンスaからkeyと等価な要素を線形探索(while文)
    >>> ssearch_while([6, 4, 3, 2, 1, 2, 8], 2)
    3
    """
    i = 0

    while True:
        if i == len(a):
            return -1
        if a[i] == key:
            return i
        i += 1

doctest.testmod(verbose=True)
unittest.main(argv=[''], verbosity=2, exit=False)


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
        self.assertEqual(search_while([6, 4, 3, 2, 1, 2, 8], 2), 3)
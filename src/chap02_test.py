# %% [markdown]
# # データ構造と配列
# %%
import doctest
import unittest
from unittest.case import skip

# %% [markdown]
# ## データ構造と配列

# %% [markdown]
# ### 配列の必要性

class TestTotal(unittest.TestCase):
    def test_5人の点数を読み込んで合計点平均点を返す(self):
        self.assertEqual(total(32, 68, 72, 54, 92), '318,63.6')


# %% [markdown]
# ## 配列

doctest.testmod(verbose=True)
unittest.main(argv=[''], verbosity=2, exit=False)
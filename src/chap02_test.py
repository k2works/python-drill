# %% [markdown]
# # データ構造と配列
# %%
import doctest
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
        self.assertEqual(total(32, 68, 72, 54, 92), '318,63.6')

def total(tensu1, tensu2, tensu3, tensu4, tensu5):
    """ 5人の点数を読み込んで合計点平均点を返す

    >>> total(32,68,72,54,92)
    '318,63.6'
    """
    result = ''
    total = functools.reduce(
        lambda a, b: a+b, [tensu1, tensu2, tensu3, tensu4, tensu5])
    result = str(total)
    result += ','
    result += str(total/5)

    return result


# %% [markdown]
# ## 配列

doctest.testmod(verbose=True)
unittest.main(argv=[''], verbosity=2, exit=False)


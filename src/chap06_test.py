from typing import MutableSequence
import unittest
import doctest
# %% [markdown]
# # ソート
# %%

# %% [markdown]
# ## 単純交換ソート（バブルソート）


class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort(self):
        array = [6, 4, 3, 7, 1, 9, 8]
        bubule_sort(array)
        self.assertEqual(array, [1, 3, 4, 6, 7, 8, 9])

    def test_bubble_sort2(self):
        array = [6, 4, 3, 7, 1, 9, 8]
        bubule_sort2(array)
        self.assertEqual(array, [1, 3, 4, 6, 7, 8, 9])


def bubule_sort(a: MutableSequence):
    """ 単純交換ソート"""
    n = len(a)
    for i in range(n-1):
        for j in range(n-1, i, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]


def bubule_sort2(a: MutableSequence):
    """ 単純交換ソート (第２版：交換回数による打ち切り）"""
    n = len(a)
    for i in range(n-1):
        exchange = 0
        for j in range(n-1, i, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                exchange += 1
        if exchange == 0:
            break


# %% [markdown]
# ## 単純選択ソート

# %% [markdown]
# ## 単純挿入ソート

# %% [markdown]
# ## シェルソート

# %% [markdown]
# ## クイックソート

# %% [markdown]
# ## マージソート

# %% [markdown]
# ## ヒープソート

# %% [markdown]
# ## 度数ソート

doctest.testmod(verbose=True)
unittest.main(argv=[''], verbosity=2, exit=False)

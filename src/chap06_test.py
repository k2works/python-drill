import bisect
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
        bubble_sort(array)
        self.assertEqual(array, [1, 3, 4, 6, 7, 8, 9])

    def test_bubble_sort2(self):
        array = [6, 4, 3, 7, 1, 9, 8]
        bubble_sort2(array)
        self.assertEqual(array, [1, 3, 4, 6, 7, 8, 9])

    def test_bubble_sort3(self):
        array = [6, 4, 3, 7, 1, 9, 8]
        bubble_sort3(array)
        self.assertEqual(array, [1, 3, 4, 6, 7, 8, 9])


def bubble_sort(a: MutableSequence):
    """ 単純交換ソート"""
    n = len(a)
    for i in range(n-1):
        for j in range(n-1, i, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]


def bubble_sort2(a: MutableSequence):
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


def bubble_sort3(a: MutableSequence):
    """ 単純選択ソート（第3版：捜査範囲を限定）"""
    n = len(a)
    k = 0
    while k < n - 1:
        last = n - 1
        for j in range(n - 1, k, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        k = last


class TestShakerSort(unittest.TestCase):
    def test_shaker_sort(self):
        array = [9, 1, 3, 4, 6, 7, 8]
        shaker_sort(array)
        self.assertEqual(array, [1, 3, 4, 6, 7, 8, 9])


def shaker_sort(a: MutableSequence):
    """シェーカーソート（双方向バブルソート）"""
    left = 0
    right = len(a) - 1
    while left < right:
        for j in range(right, left, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        left = last

        for j in range(left, right):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                last = j
        right = last


# %% [markdown]
# ## 単純選択ソート

class TestSelectionSort(unittest.TestCase):
    def test_selection_sort(self):
        array = [6, 4, 8, 3, 1, 9, 7]
        selection_sort(array)
        self.assertEqual(array, [1, 3, 4, 6, 7, 8, 9])


def selection_sort(a: MutableSequence):
    """ 単純選択ソート"""
    n = len(a)
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]


# %% [markdown]
# ## 単純挿入ソート

class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        array = [6, 4, 8, 3, 1, 9, 7]
        insertion_sort(array)
        self.assertEqual(array, [1, 3, 4, 6, 7, 8, 9])


def insertion_sort(a: MutableSequence):
    """ 単純挿入ソート"""
    n = len(a)
    for i in range(1, n):
        j = i
        tmp = a[i]
        while j > 0 and a[j - 1] > tmp:
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp


class TestBinaryInsertionSort(unittest.TestCase):
    def test_binary_insertion_sort(self):
        array = [6, 4, 8, 3, 1, 9, 7]
        binary_insertion_sort(array)
        self.assertEqual(array, [1, 3, 4, 6, 7, 8, 9])

    def test_binary_insertion_sort2(self):
        array = [6, 4, 8, 3, 1, 9, 7]
        binary_insertion_sort2(array)
        self.assertEqual(array, [1, 3, 4, 6, 7, 8, 9])


def binary_insertion_sort(a: MutableSequence):
    """ 二分挿入ソート """
    n = len(a)
    for i in range(1, n):
        key = a[i]
        pl = 0
        pr = i - 1

        while True:
            pc = (pl + pr) // 2
            if a[pc] == key:
                break
            elif a[pc] < key:
                pl = pc + 1
            else:
                pr = pc - 1
            if pl > pr:
                break
        pd = pc + 1 if pl < pr else pr + 1
        for j in range(i, pd, -1):
            a[j] = a[j - 1]
        a[pd] = key


def binary_insertion_sort2(a: MutableSequence):
    """ 二分挿入ソート """
    for i in range(1, len(a)):
        bisect.insort(a, a.pop(i), 0, i)


# %% [markdown]
# ## シェルソート
class TestShellSort(unittest.TestCase):
    def test_shell_sort(self):
        array = [6, 4, 8, 3, 1, 9, 7]
        shell_sort(array)
        self.assertEqual(array, [1, 3, 4, 6, 7, 8, 9])

    def test_shell_sort2(self):
        array = [6, 4, 8, 3, 1, 9, 7]
        shell_sort2(array)
        self.assertEqual(array, [1, 3, 4, 6, 7, 8, 9])

def shell_sort(a: MutableSequence):
    """ シェルソート"""
    n = len(a)
    h = n // 2
    while h > 0:
        for i in range(h, n):
            j = i - h
            tmp = a[i]
            while j >= 0 and a[j] > tmp:
                a[j + h] = a[j]
                j -= h
            a[j + h] = tmp
        h //= 2

def shell_sort2(a: MutableSequence):
    """ シェルソート（第２版）"""
    n = len(a)
    h = 1 
    while (h < n // 9):
        h = 3 * h + 1
    while h > 0:
        for i in range(h, n):
            j = i - h
            tmp = a[i]
            while j >= 0 and a[j] > tmp:
                a[j + h] = a[j]
                j -= h
            a[j + h] = tmp
        h //= 3

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

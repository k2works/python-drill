
# %% [markdown]
# # 探索
# %%
from enum import Enum
import hashlib
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
    def 開始位置を一つ進める(中間位置): return 中間位置 + 1
    def 開始位置を一つ戻す(中間位置): return 中間位置 - 1
    def 検索終了(開始位置, 終了位置): 開始位置 > 終了位置

    def 開始位置と終了位置を調整する(中間位置の値, 検索値, 開始位置, 終了位置):
        def 中間位置の値は検索値より少ない(中間位置の値, 検索値): return 中間位置の値 < 検索値

        if 中間位置の値は検索値より少ない(中間位置の値, 検索値):
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

        開始位置, 終了位置 = 開始位置と終了位置を調整する(a[中間位置], key, 開始位置, 終了位置)

        if 検索終了(開始位置, 終了位置):
            break
    return -1


# %% [markdown]
# ### ハッシュ法

class TestChainedHash(unittest.TestCase):

    def setUp(self):
        self.hash = ChainedHash(13)
        self.hash.add(1, '赤尾')
        self.hash.add(5, '武田')
        self.hash.add(10, '小野')
        self.hash.add(12, '鈴木')
        self.hash.add(14, '神崎')

    def test_search(self):
        self.assertEqual(self.hash.search(1), '赤尾')

    def test_add(self):
        self.hash.add(100, '山田')
        self.assertEqual(self.hash.search(100), '山田')

    def test_remove(self):
        self.hash.add(100, '山田')
        self.hash.remove(100)
        self.assertEqual(self.hash.search(100), None)

    def test_dump(self):
        expected = """\
0
1   -> 14 (神崎)   -> 1 (赤尾)
2
3
4
5   -> 5 (武田)
6
7
8
9
10   -> 10 (小野)
11
12   -> 12 (鈴木)
"""
        actual = self.hash.dump()
        self.assertEqual(actual, expected)


class Node:
    """ハッシュを構成するノード
    """

    def __init__(self, key: Any, value: Any, next: Any) -> None:
        self.key = key
        self.value = value
        self.next = next


class ChainedHash:
    """チェイン法を実現するハッシュクラス
    >>> hash = ChainedHash(13)
    >>> hash.add(1, '赤尾')
    True
    >>> hash.search(1)
    '赤尾'
    >>> hash.remove(1)
    True
    >>> hash.search(1)
    """

    def __init__(self, capacity: int) -> None:
        def ハッシュテーブルを作る(capacity):
            self.capacity = capacity
            self.table = [None] * self.capacity

        ハッシュテーブルを作る(capacity)

    def __ハッシュ値(self, key):
        def 整数型または文字列型のキーを基にハッシュ値を計算する(key):
            if isinstance(key, int):
                return key % self.capacity
            return (int(hashlib.sha256(str(key).encode())).hexdigest(), 16)

        return 整数型または文字列型のキーを基にハッシュ値を計算する(key)

    def __キーからノードを取得する(self, key: Any) -> Node:
        return self.table[self.__ハッシュ値(key)]

    def __ハッシュテーブルを更新する(self, key: Any, value: Any) -> None:
        temp = Node(key, value, self.table[self.__ハッシュ値(key)])
        self.table[self.__ハッシュ値(key)] = temp

    def search(self, key: Any) -> Any:
        def ノードのキーに対応する値を返す(node: Node, key: Any) -> Any:
            while node is not None:
                if node.key == key:
                    return node.value
                node = node.next
            return None

        node = self.__キーからノードを取得する(key)
        return ノードのキーに対応する値を返す(node, key)

    def add(self, key: Any, value: Any) -> bool:
        def ノードに対応するキーが存在する(node: Node, key: Any) -> bool:
            while node is not None:
                if node.key == key:
                    return True
                node = node.next
            return False

        node = self.__キーからノードを取得する(key)
        if ノードに対応するキーが存在する(node, key):
            return False
        else:
            self.__ハッシュテーブルを更新する(key, value)
            return True

    def remove(self, key: Any) -> bool:
        node = self.__キーからノードを取得する(key)
        pre_node = None

        while node is not Node:
            if node.key == key:
                if pre_node is None:
                    self.table[self.__ハッシュ値(key)] = node.next
                else:
                    pre_node.next = node.next
                return True
            pre_node = node
            node = node.next
        return False

    def dump(self) -> str:
        result = ''
        for i in range(self.capacity):
            node = self.table[i]
            result += f'{i}'
            while node is not None:
                result += f'   -> {node.key} ({node.value})'
                node = node.next
            result += '\n'
        return result

# %% [markdown]
# ### オープンアドレス法


class TestOpenHash(unittest.TestCase):
    def setUp(self) -> None:
        self.hash = OpenHash(13)
        self.hash.add(1, '赤尾')
        self.hash.add(5, '武田')
        self.hash.add(10, '小野')
        self.hash.add(12, '鈴木')
        self.hash.add(14, '神崎')

    def test_add(self):
        self.hash.add(100, '山田')
        self.assertEqual(self.hash.search(100), '山田')

    def test_remove(self):
        self.hash.remove(100)
        self.assertEqual(self.hash.search(100), None)


class Status(Enum):
    OCCUPIED = 0
    EMPTY = 1
    DELETED = 2


class Bucket:
    def __init__(self, key: Any = None, value: Any = None, stat: Status = Status.EMPTY) -> None:
        self.key = key
        self.value = value
        self.stat = stat

    def set(self, key: Any, value: Any, stat: Status) -> None:
        self.key = key
        self.value = value
        self.stat = stat

    def set_status(self, stat: Status) -> None:
        self.stat = stat


class OpenHash:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.table = [Bucket()] * self.capacity

    def hash_value(self, key: Any) -> int:
        if isinstance(key, int):
            return key % self.capacity
        return (int(hashlib.md5(str(key).encode()).hexdigest(), 16) % self.capacity)

    def rehash_value(self, key: Any) -> int:
        return (self.hash_value(key) + 1) % self.capacity

    def search_node(self, key: Any) -> Any:
        hash = self.hash_value(key)
        p = self.table[hash]
        for i in range(self.capacity):
            if p.stat == Status.EMPTY:
                break
            elif p.stat == Status.OCCUPIED and p.key == key:
                return p
            hash = self.rehash_value(hash)
            p = self.table[hash]
        return None

    def search(self, key: Any) -> Any:
        p = self.search_node(key)
        if p is not None:
            return p.value
        else:
            return None

    def add(self, key: Any, value: Any) -> bool:
        if self.search(key) is not None:
            return False

        hash = self.hash_value(key)
        p = self.table[hash]
        for i in range(self.capacity):
            if p.stat == Status.EMPTY or p.stat == Status.DELETED:
                self.table[hash] = Bucket(key, value, Status.OCCUPIED)
                return True
            hash = self.rehash_value(hash)
            p = self.table[hash]
        return False

    def remove(self, key: Any) -> int:
        p = self.search_node(key)
        if p is None:
            return False
        p.set_status(Status.DELETED)
        return True




doctest.testmod(verbose=True)
unittest.main(argv=[''], verbosity=2, exit=False)

# %%

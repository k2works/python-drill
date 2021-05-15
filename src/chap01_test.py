# %% [markdown]
# # アルゴリズムとは
# %%
import doctest
import unittest
from unittest.case import skip

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


# %% [markdown]
# ## 条件判定と分岐
# %%

class TestjudgeSign(unittest.TestCase):
    def test_judge_sign(self):
        self.assertEqual(judge_sign(17), 'その値は正です。')
        self.assertEqual(judge_sign(-5), 'その値は負です。')
        self.assertEqual(judge_sign(0), 'その値は0です。')


def judge_sign(n):
    """ 読み込んだ整数値の符号を表示

    >>> judge_sign(17)
    'その値は正です。'
    """
    if n > 0:
        return 'その値は正です。'
    if n < 0:
        return 'その値は負です。'
    else:
        return 'その値は0です。'

# %% [markdown]
# # 繰り返し

# %% [markdown]
# ## 1からnまでの整数の総和を求める
# %%


class TestSum1ToNWhile(unittest.TestCase):
    def test_while文による繰り返し(self):
        self.assertEqual(sum_1_to_n_while(5), 15)

    def test_for文による繰り返し(self):
        self.assertEqual(sum_1_to_n_for(5), 15)

    def test_ガウスの方法(self):
        self.assertEqual(sum_1_to_n_gauss(5), 15)


def sum_1_to_n_while(n):
    """ while文による繰り返し

    >>> sum_1_to_n_while(5)
    15
    """
    sum = 0
    i = 1
    while i <= n:
        sum += i
        i += 1
    return sum


def sum_1_to_n_for(n):
    """ for文による繰り返し

    >>> sum_1_to_n_for(5)
    15
    """
    sum = 0
    i = 1
    for i in range(i, n + 1):
        sum += i
    return sum


def sum_1_to_n_gauss(n):
    """ ガウスの方法

    >>> sum_1_to_n_gauss(5)
    15
    """
    return n * (n + 1) // 2

# %% [markdown]
# ## ２値のソートと２価の交換
# %%


class TestSum(unittest.TestCase):
    def test_aからbまでの総和を求める(self):
        self.assertEqual(sum_range(3, 8), 33)
        self.assertEqual(sum_range(8, 3), 33)


def sum_range(a, b):
    """ aからbまでの総和を求める

    >>> sum_range(3,8)
    33
    """
    def swap(a, b):
        if a > b:
            return b, a
        else:
            return a, b
    a, b = swap(a, b)
    return sum(range(a, b + 1))


# %% [markdown]
# ## 繰返しの過程における条件判定（その１）
# %%


class TestSumVerbose(unittest.TestCase):
    def test_aからbまでの総和を求める_1(self):
        self.assertEqual(sum_verbose_1(3, 3), '3 = 3')
        self.assertEqual(sum_verbose_1(3, 4), '3 + 4 = 7')
        self.assertEqual(sum_verbose_1(3, 7), '3 + 4 + 5 + 6 + 7 = 25')

    def test_aからbまでの総和を求める_2(self):
        self.assertEqual(sum_verbose_2(3, 3), '3 = 3')
        self.assertEqual(sum_verbose_2(3, 4), '3 + 4 = 7')
        self.assertEqual(sum_verbose_2(3, 7), '3 + 4 + 5 + 6 + 7 = 25')


def sum_verbose_1(a, b):
    """ aからbまでの総和を求める

    >>> sum_verbose_1(3, 4)
    '3 + 4 = 7'
    """

    if a > b:
        a, b = b, a

    sum = 0
    def buildExpression(i, b): return f'{i} + ' if i < b else f'{i} ='
    result = ''
    for i in range(a, b + 1):
        result += buildExpression(i, b)
        sum += i
    result += f' {sum}'
    return result


def sum_verbose_2(a, b):
    """ aからbまでの総和を求める

    >>> sum_verbose_2(3, 4)
    '3 + 4 = 7'
    """

    if a > b:
        a, b = b, a

    sum = 0
    result = ''
    for i in range(a, b):
        result += f'{i} + '
        sum += i
    sum += b
    result += f'{b} = {sum}'
    return result

# %% [markdown]
# ## 繰返しの過程における条件判定（その２）
# %%


class TestAlternative(unittest.TestCase):
    def test_記号文字を交互に表示_1(self):
        self.assertEqual(alternative_1(12), '+-+-+-+-+-+-')
        self.assertEqual(alternative_1(13), '+-+-+-+-+-+-+')

    def test_記号文字を交互に表示_2(self):
        self.assertEqual(alternative_2(12), '+-+-+-+-+-+-')
        self.assertEqual(alternative_2(13), '+-+-+-+-+-+-+')


def alternative_1(n):
    """ 記号文字+と-を交互に表示（その１）

    >>> alternative_1(12)
    '+-+-+-+-+-+-'
    """
    def build_symbol(i): return '-' if i % 2 else '+'
    return ''.join(map(build_symbol, range(n)))


def alternative_2(n):
    """ 記号文字+と-を交互に表示（その２）

    >>> alternative_2(12)
    '+-+-+-+-+-+-'
    """
    result = ''.join(map(lambda i: '+-', range(n // 2)))
    return result + '+' if n % 2 else result


# %% [markdown]
# ## 繰返しの過程における条件判定（その３）
# %%

class TestPrintStars(unittest.TestCase):
    def test_n個の記号文字をw個ごとに改行しながら表示_1(self):
        self.assertEqual(print_starts_1(14, 5), '*****\n*****\n****\n')

    def test_n個の記号文字をw個ごとに改行しながら表示_2(self):
        self.assertEqual(print_starts_2(14, 5), '*****\n*****\n****\n')


def print_starts_1(n, w):
    """ n個の記号文字*をw個ごとに改行しながら表示（その１）

    >>> print_starts_1(14, 5)
    '*****\\n*****\\n****\\n'
    """
    def build_symbole_with_word_wrap(
        i): return '*\n' if i % w == w - 1 else '*'
    result = ''.join(map(build_symbole_with_word_wrap, range(n)))
    result += '\n'

    return result


def print_starts_2(n, w):
    """ n個の記号文字*をw個ごとに改行しながら表示（その２）

    >>> print_starts_2(14, 5)
    '*****\\n*****\\n****\\n'
    """
    def build_symbole_with_word_wrap(i): return '*' * w + '\n'
    result = ''.join(map(build_symbole_with_word_wrap, range(n // w)))
    rest = n % w
    result += '*' * rest + '\n'

    return result

# %% [markdown]
# ## 正の値の読み込み
# %%


class TestSum1ToPositive(unittest.TestCase):
    def test_1からnまでの総和を求める(self):
        self.assertEqual(sum_1_to_positive(-6), None)
        self.assertEqual(sum_1_to_positive(0), None)
        self.assertEqual(sum_1_to_positive(10), 55)


def sum_1_to_positive(n):
    """ 1からnまでの総和を求める（nに正の整数値を読み込む）

    >>> sum_1_to_positive(10)
    55
    """
    if n <= 0:
        return None

    while True:
        if n > 0:
            break

    return sum(range(1, n + 1))

# %% [markdown]
# ## 辺と面積が整数値である長方形
# %%


class TestRectangle(unittest.TestCase):
    def test_縦横が整数で面積がareaの長方形の辺の長さを列挙(self):
        self.assertEqual(rectangle(32), '1x32 2x16 4x8 ')


def rectangle(area):
    """ 縦横が整数で面積がareaの長方形の辺の長さを列挙

    >>> rectangle(32)
    '1x32 2x16 4x8 '
    """
    def 条件を満たす(i, area):
        if i * i > area:
            return False
        if area % i:
            return False
        return True

    条件を満たす辺の長さリスト = [i for i in range(1, area + 1) if 条件を満たす(i, area)]
    縦横が整数で面積がareaの長方形の辺の長さを列挙リスト = [f'{i}x{area // i} ' for i in 条件を満たす辺の長さリスト]

    return ''.join(縦横が整数で面積がareaの長方形の辺の長さを列挙リスト)

# %% [markdown]
# ## 繰り返しのスキップと複数のrangeの走査
# %%


class TestSkip(unittest.TestCase):
    def test_1から12までを8をスキップして繰り返す(self):
        self.assertEqual(skip_1(), '1 2 3 4 5 6 7 9 10 11 12')
        self.assertEqual(skip_2(), '1 2 3 4 5 6 7 9 10 11 12')


def リストを文字列に結合する(list):
    return ' '.join(f'{i}' for i in list)


def skip_1():
    """ 1から12までを8をスキップして繰り返す（その１）

    >>> skip_1()
    '1 2 3 4 5 6 7 9 10 11 12 '
    """
    条件を満たすリスト = [i for i in range(1, 13) if i != 8]
    return リストを文字列に結合する(条件を満たすリスト)


def skip_2():
    """ 1から12までを8をスキップして繰り返す（その２）

    >>> skip_2()
    '1 2 3 4 5 6 7 9 10 11 12 '
    """
    合成リスト = list(list(range(1, 8)) + list(range(9, 13)))
    return リストを文字列に結合する(合成リスト)


# %% [markdown]
# ## 多重ループ
# %%

class TestMultiplicationTable(unittest.TestCase):
    def test_九九の表を表示(self):
        expected = """\
---------------------------
  1  2  3  4  5  6  7  8  9
  2  4  6  8 10 12 14 16 18
  3  6  9 12 15 18 21 24 27
  4  8 12 16 20 24 28 32 36
  5 10 15 20 25 30 35 40 45
  6 12 18 24 30 36 42 48 54
  7 14 21 28 35 42 49 56 63
  8 16 24 32 40 48 56 64 72
  9 18 27 36 45 54 63 72 81
---------------------------\
"""
        self.assertEqual(multiplication_table(), expected)       

def multiplication_table():
    """ 九九の表を表示
    >>> multiplication_table()
    '---------------------------\\n  1  2  3  4  5  6  7  8  9\\n  2  4  6  8 10 12 14 16 18\\n  3  6  9 12 15 18 21 24 27\\n  4  8 12 16 20 24 28 32 36\\n  5 10 15 20 25 30 35 40 45\\n  6 12 18 24 30 36 42 48 54\\n  7 14 21 28 35 42 49 56 63\\n  8 16 24 32 40 48 56 64 72\\n  9 18 27 36 45 54 63 72 81\\n---------------------------'
    """
    header = ''.join(['-' for _ in range(27)]) + '\n'

    def row(i): return ''.join([f'{i * j:3}' for j in range(1, 10)]) + '\n'
    body = ''.join([row(i) for i in range(1, 10)])

    footer = ''.join(['-' for _ in range(27)])

    return header + body + footer

# %% [markdown]
# ## 直角三角形の表示
# %%


class TestTraiangleLb(unittest.TestCase):
    def test_左下側が直角の二等辺三角形を表示(self):
        expected = """\
*
**
***
****
*****
"""
        self.assertEqual(traiangle_lb(5), expected)


def traiangle_lb(n):
    """ 左下側が直角の二等辺三角形を表示

    >>> traiangle_lb(5)
    '*\\n**\\n***\\n****\\n*****\\n'
    """
    右側 = lambda i: ''.join(['*' for _ in range(i + 1)]) + '\n'
    return ''.join([右側(i) for i in range(n)])

class TestTraiangleRb(unittest.TestCase):
    def test_traiangle_rb(self):
        expected = """\
    *
   **
  ***
 ****
*****
"""
        self.assertEqual(traiangle_rg(5), expected)

def traiangle_rg(n):
    """ 右下側が直角の二等辺三角形を表示

    >>> traiangle_rg(5)
    '    *\\n   **\\n  ***\\n ****\\n*****\\n'
    """
    result = ''
    right = lambda i: ''.join(' ' for _ in range(n - i - 1))
    left = lambda i: ''.join('*' for _ in range(i + 1))
    for i in range(n):
        result += right(i)
        result += left(i)
        result += '\n'
    return result

doctest.testmod(verbose=True)
unittest.main(argv=[''], verbosity=2, exit=False)

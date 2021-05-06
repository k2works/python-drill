# %% [markdown]
# # アルゴリズムとは
# %%
import unittest
import doctest
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

doctest.testmod(verbose=True)
unittest.main(argv=[''], verbosity=2, exit=False)

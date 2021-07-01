import unittest
from typing import Any

# %% [markdown]
# # スタックとキュー
# %%

# %% [markdown]
# ## スタック


class TestFixedStack(unittest.TestCase):
    def test_push(self):
        s = FixedStack(64)
        s.push(1)
        self.assertEqual(s.dump(), [1])
        s2 = FixedStack(0)
        with self.assertRaises(IndexError):
            s2.push(1)
    
    def test_find(self):
        s = FixedStack(64)
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(s.find(2), 1)

    def test_count(self):
        s = FixedStack(64)
        s.push(1)
        s.push(1)
        s.push(1)
        self.assertEqual(s.count(1), 3)

    def test_peek(self):
        s = FixedStack(64)
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(s.peek(), 3)
        with self.assertRaises(Exception):
            s.clear()
            s.peek()

    def test_pop(self):
        s = FixedStack(64)
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(s.pop(), 3)
        with self.assertRaises(Exception):
            s.clear()
            s.pop()

    def test_clear(self):
        s = FixedStack(64)
        s.push(1)
        s.push(2)
        s.push(3)
        s.clear()
        self.assertTrue(s.is_empyt())

class FixedStack:
    class Empyt(Exception):
        pass

    class Full(IndexError):
        pass

    def __init__(self, capacity: int = 256) -> None:
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    def push(self, value: Any) -> None:
        if self.ptr >= self.capacity:
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1

    def dump(self) -> None:
        return self.stk[:self.ptr]

    def find(self, value: Any) -> Any:
        for i in range(self.ptr - 1, -1, -1):
            if self.stk[i] == value:
                return i
        return -1

    def count(self, value: Any) -> bool:
        c = 0
        for i in range(self.ptr):
            if self.stk[i] == value:
                c += 1
        return c

    def peek(self) -> Any:
        if self.is_empyt():
            raise FixedStack.Empyt
        return self.stk[self.ptr - 1]

    def pop(self) -> Any:
        if self.is_empyt():
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]

    def clear(self) -> None:
        self.ptr = 0

    def is_empyt(self) -> bool:
        return self.ptr <= 0


# %% [markdown]
# ### 固定長スタック

# %% [markdown]
# ## キュー

# %% [markdown]
# ### 固定長キュー

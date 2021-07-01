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


class FixedStack:
    def __init__(self, capacity: int = 256) -> None:
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    def push(self, value: Any) -> None:
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
        return self.stk[self.ptr - 1]


# %% [markdown]
# ### 固定長スタック

# %% [markdown]
# ## キュー

# %% [markdown]
# ### 固定長キュー

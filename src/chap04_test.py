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


# %% [markdown]
# ### 固定長スタック

# %% [markdown]
# ## キュー

# %% [markdown]
# ### 固定長キュー

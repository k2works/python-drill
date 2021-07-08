import unittest
import doctest
from typing import Any
from collections import deque

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
        self.assertTrue(s.is_empty())
        self.assertEqual(len(s), 0)

class FixedStack:
    """ 固定長スタック

    >>> stack = FixedStack(64)
    >>> stack.push(1)
    >>> stack.push(2)
    >>> stack.push(3)
    >>> stack.dump()
    [1, 2, 3]
    >>> stack.peek()
    3
    >>> stack.find(2)
    1
    >>> stack.count(2)
    1
    >>> stack.clear()
    >>> stack.is_empty()
    True
    """
    class Empyt(Exception):
        pass

    class Full(IndexError):
        pass

    def __init__(self, capacity: int = 256) -> None:
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    def __len__(self) -> int:
        return self.ptr

    def push(self, value: Any) -> None:
        if self.ptr >= self.capacity:
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1

    def dump(self) -> None:
        return self.stk[:self.ptr]

    def find(self, value: Any) -> Any:
        for i in range(self.ptr - 1, -1, -1):
            if self.is_value(i, value):
                return i
        return -1

    def count(self, value: Any) -> bool:
        c = 0
        for i in range(self.ptr):
            if self.is_value(i, value):
                c += 1
        return c

    def peek(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empyt
        return self.stk[self.ptr - 1]

    def pop(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]

    def clear(self) -> None:
        self.ptr = 0

    def is_empty(self) -> bool:
        return self.ptr <= 0

    def is_value(self, i: int, value: Any) -> bool:
        return self.stk[i] == value


# %% [markdown]
# ### 固定長スタック

class TestStack(unittest.TestCase):
    def test_push(self):
        s = Stack(64)
        s.push(1)
        self.assertEqual(s.dump(), [1])

    def test_find(self):
        s = Stack(64)
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(s.find(2), 1)

    def test_count(self):
        s = Stack(64)
        s.push(1)
        s.push(1)
        s.push(1)
        self.assertEqual(s.count(1), 3)
    
    def test_peek(self):
        s = Stack(64)
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(s.peek(), 3)

    def test_pop(self):
        s = Stack(64)
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(len(s), 2)

    def test_clear(self):
        s = Stack(64)
        s.push(1)
        s.push(2)
        s.push(3)
        s.clear()
        self.assertEqual(s.is_empty(), True)

class Stack:
    """ 固定長スタック

    >>> stack = Stack(64)
    >>> stack.push(1)
    >>> stack.push(2)
    >>> stack.push(3)
    >>> stack.dump()
    [1, 2, 3]
    >>> stack.peek()
    3
    >>> stack.find(2)
    1
    >>> stack.count(2)
    1
    >>> stack.clear()
    >>> stack.is_empty()
    True
    """
    def __init__(self,maxlen: int = 256) -> None:
        self.capacity = maxlen
        self.__stk = deque([], maxlen)

    def __len__(self) -> int:
        return len(self.__stk)
    
    def push(self, value: Any) -> None:
        self.__stk.append(value)

    def dump(self) -> Any:
        return list(self.__stk)

    def find(self, value: Any) -> Any:
        try:
            return self.__stk.index(value)
        except ValueError:
            return -1

    def count(self, value: Any) -> int:
        return self.__stk.count(value)

    def peek(self) -> Any:
        return self.__stk[-1]

    def pop(self) -> Any:
        return self.__stk.pop()

    def clear(self) ->None:
        self.__stk.clear()

    def is_empty(self) -> bool:
        return not self.__stk

    def is_full(self) -> bool:
        return len(self.__stk) == self.__stk.maxlen
    

# %% [markdown]
# ## キュー

# %% [markdown]
# ### 固定長キュー

class TestFixedQueue(unittest.TestCase):
    def test_enque(self):
        q = FixedQueue(64)
        q.enque(1)
        self.assertEqual(q.dump()[0], 1)

    def test_deque(self):
        q = FixedQueue(64)
        q.enque(1)
        q.enque(2)
        q.enque(3)
        self.assertEqual(q.deque(), 1)

    def test_peek(self):
        q = FixedQueue(64)
        q.enque(1)
        q.enque(2)
        q.enque(3)
        self.assertEqual(q.peek(), 1) 

    def test_find(self):
        q = FixedQueue(64)
        q.enque(1)
        q.enque(2)
        q.enque(3)
        self.assertEqual(q.find(2), 1)


class FixedQueue:
    def __init__(self, capacity: int) -> None:
        self.no = 0
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.que = [None] * capacity

    def enque(self, x: Any) -> None:
        if self.no >= self.capacity:
            raise Exception
        self.que[self.rear] = x
        self.rear += 1
        self.no += 1
        if self.front == self.capacity:
            self.rear = 0
        return x

    def dump(self) -> Any:
        if self.no <= 0:
            return 'キューは空です。'
        return list(self.que)

    def deque(self) -> Any:
        if self.no <= 0:
            raise Exception
        x = self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return x

    def peek(self) -> Any:
        if self.no >= self.capacity:
            raise Exception
        return self.que[self.front]

    def find(self, value: Any) -> Any:
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                return idx



doctest.testmod(verbose=True)
unittest.main(argv=[''], verbosity=2, exit=False)

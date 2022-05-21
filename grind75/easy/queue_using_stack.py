"""
232: https://leetcode.com/problems/implement-queue-using-stacks/

Implement a first in first out (FIFO) queue using only two stacks. 
The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
Implement the MyQueue class:
    void push(int x) Pushes element x to the back of the queue.
    int pop() Removes the element from the front of the queue and returns it.
    int peek() Returns the element at the front of the queue.
    boolean empty() Returns true if the queue is empty, false otherwise.

Notes:
    You must use only standard operations of a stack, which means only push to top, 
    peek/pop from top, size, and is empty operations are valid.
    Depending on your language, the stack may not be supported natively. 
    You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.


Solutions: 

##### 1
Using stacks s1 and s2:
Only append to s1.
Only peek and pop from s2.
If s2 is empty, move elements from s1. 

"""

class CustomQueue:
  def __init__(self):
    self.s1, self.s2 = [], []

  def push(self, x: int) -> None:
    self.s1.append(x)

  def pop(self) -> int:
    if not self.s2:
      self.shift()
    return self.s2.pop() if self.s2 else None

  def peek(self) -> int:
    if not self.s2:
      self.shift()
    return self.s2[-1] if self.s2 else None

  def empty(self) -> bool:
    return not self.s1 and not self.s2

  def shift(self):
    while self.s1:
      self.s2.append(self.s1.pop())

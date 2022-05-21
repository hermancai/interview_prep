"""
155: https://leetcode.com/problems/min-stack/

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Implement the MinStack class:
  MinStack() initializes the stack object.
  void push(int val) pushes the element val onto the stack.
  void pop() removes the element on the top of the stack.
  int top() gets the top element of the stack.
  int getMin() retrieves the minimum element in the stack.


Solutions:

##### 1
Use a list and keep track of min.
When pushing, push a tuple containing val and current min.
When popping, update min with the min of the top tuple in stack.


##### 2
Use a linked list of nodes that also track min.
When pushing, place node as new head of list. Min of new node 
  will be minimum between current value or previous node min.
When popping, just reference head next.

"""

# Solution 1
class ListStack:
  def __init__(self):
    self.stack = []
    self.minV = None

  def push(self, val: int) -> None:
    if self.minV is None or val < self.minV:
      self.minV = val
    self.stack.append((val, self.minV))

  def pop(self) -> None:
    self.stack.pop()
    if self.stack:
      self.minV = self.stack[-1][1]
    else:
      self.minV = None

  def top(self) -> int:
    return self.stack[-1][0]

  def getMin(self) -> int:
    return self.stack[-1][1]


# Solution 2
class Node:
  def __init__(self, val, minV, next):
    self.val = val
    self.minV = minV
    self.next = next

class LinkedStack:
  def __init__(self):
    self.head = None

  def push(self, val):
    if not self.head: 
      self.head = Node(val, val, None)
    else:
      self.head = Node(val, min(val, self.head.minV), self.head)

  def pop(self):
    self.head = self.head.next

  def top(self):
    return self.head.val

  def getMin(self):
    return self.head.minV

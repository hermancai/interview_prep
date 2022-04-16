'''
Create a Queue class using two stacks.

Solution:
Given stacks s1 and s2, s1 can be reversed by popping s1 and pushing 
to s2. Then peek and pop on s2 will work like a queue.

Push will always add to s1.
Peek and pop will always check from s2. 
If s2 is empty, fill it with elements from s1.

'''

class MyQueue:
  def __init__(self):
    self.old = []
    self.new = []

  def push(self, val):
    self.new.append(val)

  def shift(self):
    if not self.old:
      while self.new:
        self.old.append(self.new.pop())

  def peek(self):
    self.shift()
    return self.old[-1] if self.old else None

  def pop(self):
    self.shift()
    return self.old.pop() if self.old else None


if __name__ == "__main__":
  q = MyQueue()
  q.push(1)
  q.push(2)
  
  print(q.pop())
  q.push(3)
  print(q.pop())

  print(q.new)
  print(q.old)

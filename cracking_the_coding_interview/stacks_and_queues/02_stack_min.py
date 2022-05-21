'''
Create a stack that has functions push, pop, and min which 
returns the minimum element. All three functions must to O(1) time.

Solutions:

##### 1
Push tuples onto the stack, where the other value is the current min.

##### 2
Use another stack to keep track of min.

'''

# Solution 2
class MinStack:
  def __init__(self):
    self.stack = []
    self.minTrack = []

  def pop(self):
    if not self.stack: return None

    val = self.stack.pop()

    if self.minTrack and self.minTrack[-1] == val:
      self.minTrack.pop()

    return val

  def push(self, val):
    self.stack.append(val)

    if not self.minTrack or val <= self.minTrack[-1]:
      self.minTrack.append(val)

  def min(self):
    return self.minTrack[-1]


if __name__ == "__main__":
  s = MinStack()
  s.push(5)
  s.push(6)
  s.push(3)
  s.push(7)
  s.pop()
  s.pop()

  print(s.min())

'''
Suppose stacks have a limited capacity. Implement SetOfStacks, which can 
contain multiple stacks and will create a new stack when the previous stack 
runs out of space. Push and pop should behave the same way as a normal stack.

Solution: 
Use a 2D list to hold the stacks. Update the stacks based on stack capacity 
after each push/pop.

'''

class SetOfStacks:
  def __init__(self):
    self.limit = 2
    self.stacks = []

  def push(self, val):
    # Handle empty or full stack
    if not self.stacks or len(self.stacks[-1]) >= self.limit:
      return self.stacks.append([val])

    # If current stack is not full
    return self.stacks[-1].append(val)

  def pop(self):
    curr = self.stacks[-1]
    if curr:
      val = curr.pop()
      if not curr:
        self.stacks.pop()
      return val

  def printStack(self):
    print(self.stacks)


if __name__ == "__main__":
  s = SetOfStacks()

  s.push(1)
  s.pop()
  s.push(2)
  s.push(3)
  s.push(4)
  s.pop()

  s.printStack()

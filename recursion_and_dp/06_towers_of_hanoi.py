'''
There are 3 towers and n disks on Tower 1. The disks are in ascending order 
in size from top to bottom. Move the disks to Tower 3, keeping the same order.
Rules:
  Only one disk can be moved at a time.
  A disk is taken off the top of one tower and onto another.
  A disk cannot be placed on top of a smaller disk.

Solution:
Recursively get to the base case n = 1, where moving the disk is trivial. 
Moving up the call stack reaches case n = 2. We know how to handle n = 1, 
but instead of moving it to the destination, move it to the buffer instead. 
Then move the second disk (at the origin) to the destination. 
Then perform the n = 1 case again, this time with the buffer as the origin. 
For case n = 3, we know how to handle n = 2. Move n = 2 disks to the buffer, 
and the origin as the buffer.
Then move the last disk (at the origin) to the destination.
Then perform the n = 2 case again, this time with the buffer as the origin, 
and the origin as the buffer.
Keep repeating this process until done.

Note: While moving back up the call stack, each call has to then recurse again 
until n = 1 again.

Time: O(2^n - 1) = O(2^n)
Space: O(n). n represents the depth of recursive calls. Though more calls than 
  n are made, those calls return and free up space before other calls. Recall 
  that every call of n must recursively get to n = 1 for moving up the call 
  stack to n + 1.

'''

class Tower:
  def __init__(self, name: str, li: list):
    self.name = name
    self.li = li

# Note that each call of this function simply moves one disk once.
# The destination, buffer, and origin towers change per call to 
# swap disks as needed. 
def moveDisks(n: int, origin: Tower, destination: Tower, buffer: Tower):
  if n <= 0: return

  # Move previously handled case of n - 1 to the buffer
  moveDisks(n - 1, origin, buffer, destination)

  # Move the largest disk of current n to the destination
  print("Moving disk from", origin.name, "to", destination.name)
  destination.li.append(origin.li.pop())

  # Move everything from the buffer onto the destination
  moveDisks(n - 1, buffer, destination, origin)


if __name__ == "__main__":
  t1, t2, t3 = Tower('A', [4, 3, 2, 1]), Tower('B', []), Tower('C', [])
  moveDisks(len(t1.li), t1, t3, t2)
  print(t1.li, t2.li, t3.li)

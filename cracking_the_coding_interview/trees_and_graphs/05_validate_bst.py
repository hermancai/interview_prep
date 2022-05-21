'''
Check if a binary tree is a binary search tree.

Solutions:

##### 1
Assuming no duplicates.
In-order traversal. 
Use a global variable to hold the previous value (bad practice?).
If the previous value is greater than current, return false.

Time: O(n)
Space: O(h) where h is height of the tree. O(log n) if balanced tree.


##### 2
By definition of a binary search tree, all values to the left of the 
current node must be less than or equal to the current node value. 
Update min and max values on every recursive call.
The current value should be greater than the min and less than or 
equal to the max.
 
Time: O(n)
Space: O(h) where h is height of the tree. O(log n) if balanced tree.

'''

from binary_node import BinaryNode as Node
import print_binary_tree as p

# Solution 1
prev = None

def checkBST1(root: Node) -> bool:
  return helper1(root)

def helper1(root: Node) -> bool:
  global prev
  if not root: return True

  # In Order traversal
  if not helper1(root.left): return False
  if prev is not None and prev >= root.val: return False
  prev = root.val
  if not helper1(root.right): return False

  return True

# Solution 2
def checkBST2(root: Node) -> bool:
  return helper2(root, None, None)

def helper2(root: Node, min: int, max: int) -> bool:
  if not root: return True

  if (min is not None and min >= root.val) or \
    (max is not None and max < root.val): 
      return False

  if not helper2(root.left, min, root.val) or \
    not helper2(root.right, root.val, max):
      return False
  
  return True

if __name__ == "__main__":
  root = Node(5, Node(3, Node(2), Node(4)), Node(7, Node(6)))
  p.print_tree(root)
  # print(checkBST1(root))
  print(checkBST2(root))

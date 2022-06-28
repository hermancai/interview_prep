"""
98: https://leetcode.com/problems/validate-binary-search-tree/

Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
  The left subtree of a node contains only nodes with keys less than the node's key.
  The right subtree of a node contains only nodes with keys greater than the node's key.
  Both the left and right subtrees must also be binary search trees.


Iterative inorder traversal using stack:
  Use empty stack.
  While curr OR stack are not empty:
    While curr is not None:
      Add curr to stack
      curr = curr.left
    curr = pop stack. This curr is the next inorder node.
    curr = curr.right


Solutions:

##### 1
Iterative inorder traversal, keeping track of previous node
If prev is greater than current, return False.

Time: O(n)
Space: O(n)

"""

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def validate(root: Node) -> bool:
  if root is None: return False

  stack = []
  prev = None

  while root or stack:
    while root:
      stack.append(root)
      root = root.left
    root = stack.pop()
    if prev and prev.val > root.val:
      return False
    prev = root
    root = root.right

  return True

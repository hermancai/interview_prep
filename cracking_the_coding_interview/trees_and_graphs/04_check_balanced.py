'''
Check if a binary tree is balanced. 
Balanced means the heights of the two subtrees of any node 
never differ by more than one.

Solution:
Use a helper to recursively get the heights of every subtree.
Compare and return an error anytime the tree is not balanced.

Time: O(n)
Space: O(h) where h is the height of the tree

'''

from binary_node import BinaryNode as Node


# This function recursively goes to leaf nodes 
# and current height + 1 is passed up to parent node.
def checkHeight(root: Node) -> int:
  if not root: return -1

  leftHeight = checkHeight(root.left)
  if leftHeight is None: return None

  rightHeight = checkHeight(root.right)
  if rightHeight is None: return None

  if abs(leftHeight - rightHeight) > 1: return None
  return max(leftHeight, rightHeight) + 1

def isBalanced(root: Node) -> bool:
  return checkHeight(root) is not None


if __name__ == "__main__":
  root = Node(1, Node(2, Node(3), Node(4)), Node(3, Node(5)))
  print(isBalanced(root))

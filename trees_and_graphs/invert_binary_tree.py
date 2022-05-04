'''
Invert a binary tree.

Solutions:

##### 1
Depth first in order traversal. Swap the child nodes.

Time: O(n)
Space: O(d) where d is max depth of tree

'''

from binary_node import BinaryNode as Node
import print_binary_tree as p

def invert(root: Node) -> None:
  if not root: return
  
  invert(root.left)
  root.left, root.right = root.right, root.left
  invert(root.right)


if __name__ == "__main__":
  root = Node(5, Node(3, Node(2), Node(4)), Node(7, Node(6)))
  p.print_tree(root)
  invert(root)
  p.print_tree(root)

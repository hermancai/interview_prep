'''
Invert a binary tree.

Solutions:

##### 1
Depth first pre-order traversal. Swap the child nodes.

Time: O(n)
Space: O(d) -> O(n) where d is max depth of tree


##### 2
Iterative depth first traversal using stack. 

Time: O(n)
Space: O(d) where d is max depth of tree

'''

from binary_node import BinaryNode as Node
import print_binary_tree as p

# Solution 1
def invert(root: Node) -> None:
  if not root: return

  print(root.val)
  root.left, root.right = root.right, root.left
  invert(root.left)
  invert(root.right)

# Solution 2
# NOTE: This is not breadth first traversal, which would use a queue.
def invert2(root: Node) -> None:
  stack = [root]

  while stack:
    node = stack.pop()
    if node: 
      print(node.val)
      node.left, node.right = node.right, node.left
      stack += node.left, node.right


if __name__ == "__main__":
  root = Node(5, Node(3, Node(2), Node(4)), Node(7, Node(6)))
  p.print_tree(root)
  invert(root)
  p.print_tree(root)

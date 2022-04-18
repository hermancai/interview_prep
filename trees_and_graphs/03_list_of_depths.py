'''
Given a binary tree, create a linked list for all nodes per each depth.

NOTE: Python can use a list or deque instead 
  because it does not have a builtin linked list.

Solutions:

##### 1
Depth first traversal with recursive preorder, 
passing through the node, list of linked lists, and next depth.
On each iteration, add the node to the list at depth index.

Time: O(n)
Space: O(n). Recursive calls take O(log n) for balanced tree
  but the returned data takes O(n)


##### 2
Breadth first traversal
Start with list curr[root] and empty results list
Loop until curr is empty:
  Add curr to results
  Add all children of nodes in curr to new list
  Set new list as curr

Time: O(n)
Space: O(n). Technically uses less space than depth first because 
  this does not add recursive calls to the stack. But it still needs 
  to return O(n) data.
'''

import print_binary_tree as p
from binary_node import BinaryNode as Node

# Solution 1
def depthFirstBuild(root: Node) -> list:
  result = []
  depthHelper(root, result, 0)
  return result

def depthHelper(root: Node, result: list, level: int) -> None:
  if not root: return

  # If level has not been visited yet
  if level >= len(result):
    li = []
    result.append(li)
  else:
    li = result[level]
  
  li.append(root.val)
  depthHelper(root.left, result, level + 1)
  depthHelper(root.right, result, level + 1)

# Solution 2
def breadthFirstBuild(root: Node) -> list:
  result = []
  curr = [root]
  
  while curr:
    result.append(curr)
    parents = curr
    curr = []
    for parent in parents:
      # Note: Node values cannot be added directly because each element 
      #       must be revisited to check for children.
      if parent.left: curr.append(parent.left)
      if parent.right: curr.append(parent.right)
  
  return result


if __name__ == "__main__":
  root = Node(1, Node(2, Node(3), Node(4)), Node(3, Node(5)))
  p.print_tree(root)
  # li = depthFirstBuild(root)
  li = breadthFirstBuild(root)
  print(li)

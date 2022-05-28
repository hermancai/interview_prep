"""
102: https://leetcode.com/problems/binary-tree-level-order-traversal/

Given the root of a binary tree, return the level order traversal of 
its nodes' values. (i.e., from left to right, level by level).


Solutions:

##### 1
Create results list containing root value.
Create parents list containing root.
While parents list is not empty:
  Create empty children and levels lists.
  Loop through parents list:
    If curr node has left child: add node/val to children/levels
    Same for right child
  If levels contains anything: Append levels to results.
  Set parents list as children list.
Return results

Time: O(n)
Space: O(n)

"""

class Node:
  def __init__(self, val, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right

def getLevels(root: Node) -> list:
  if not root: return []

  parents = [root]
  results = [[root.val]]

  while parents:
    children, levels = [], []
    for p in parents:
      if p.left:
        children.append(p.left)
        levels.append(p.left.val)
      if p.right:
        children.append(p.right)
        levels.append(p.right.val)
    if levels: results.append(levels)
    parents = children
  
  return results

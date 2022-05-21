"""
235: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
According to the definition of LCA on Wikipedia: 
“The lowest common ancestor is defined between two nodes p and q as 
the lowest node in T that has both p and q as descendants 
(where we allow a node to be a descendant of itself).”


Solutions:

##### 1
Use the definition of a BST to solve this.
If q and p are both less than root: search left side.
If q and p are both more than root: search right side.
Else either q and p are on opposite sides OR one of them is root: return root.

Time: O(h) where h is height of tree
Space: O(h) for recursive call stack

"""

class Node:
  def __init__(self, val, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right

def lca(root: Node, q: Node, p: Node) -> Node:
  if q.val > root.val and p.val > root.val:
    return lca(root.right, q, p)
  elif q.val < root.val and p.val < root.val:
    return lca(root.left, q, p)
  else:
    return root

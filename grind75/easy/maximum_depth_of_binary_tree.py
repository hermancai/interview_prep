"""
104: https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.


Solutions:

##### 1
Use global to track max depth.
Use helper to recursively get to leaf nodes. 

Time: O(n)
Space: O(d) where d is max depth of tree


##### 2
Solution from leetcode. See code below.
Basically this start from the root with depth = 0
  while Solution #1 gets to leaf nodes before incrementing depth.

"""

class Node:
  def __init__(self, val, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right

# Solution 1
class Solution:
  def maxDepth(self, root: Node) -> int:
    self.maxDepth = 0
    
    def getHeight(root: Node):
      if not root: return 0
      left = getHeight(root.left)
      right = getHeight(root.right)
      newDepth = max(left, right) + 1
      self.maxDepth = max(self.maxDepth, newDepth)
      return newDepth
  
    getHeight(root)
    return self.maxDepth


# Solution 2
def maxDepth2(root: Node) -> int:
  def helper(root: Node, depth: int):
    if not root: return depth
    return max(helper(root.left, depth + 1), helper(root.right, depth + 1))
  
  return helper(root, 0)

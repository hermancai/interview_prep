"""
543: https://leetcode.com/problems/diameter-of-binary-tree/

Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.


Solutions: 

##### 1
Use a helper and global variable to hold the answer.
Recursively call the helper to get the depth of every left and right subtree.
Update answer if left + right is larger.

Time: O(n)
Space: O(d) where d is max depth of tree

"""

class Node:
  def __init__(self, val, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def getDiameter(self, root: Node) -> int:
    self.answer = 0

    def getHeight(root: Node) -> int:
      if not root: return 0
      left = getHeight(root.left)
      right = getHeight(root.right)
      self.answer = max(self.answer, left + right)
      return 1 + max(left, right)

    getHeight(root)
    return self.answer

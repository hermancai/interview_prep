"""
110: https://leetcode.com/problems/balanced-binary-tree/

Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
  a binary tree in which the left and right subtrees of every node differ in height by no more than 1.


Solutions:

##### 1
Recursive depth first traversal. Get height of every subtree.
Base case: At leaf node, return 0. 
If left and right heights differ more than 1, return False.
Return -1 for imbalanced heights.

"""

class Node:
  def __init__(self, val, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right

def isBalanced(root: Node) -> bool:
  return helper(root) != -1

def helper(root: Node) -> int:
  if not root: return 0

  left = helper(root.left)
  right = helper(root.right)

  if left == -1 or right == -1 or abs(left - right) > 1: 
    return -1

  # greater subtree height will count for height of parent
  return max(left, right) + 1

'''
Given an ascending sorted list with unique ints, 
build a binary search tree with minimal height.

Input: [1, 2, 3, 4, 5, 6, 7, 8, 9]

Solution:
Root will the the middle of the list. 
Recursively break down the list, adding each element to the tree.

Time: O(n)
Space: O(n)

'''

from binary_node import BinaryNode
import print_binary_tree as p


def minTreeHelper(li: list, start: int, end: int) -> BinaryNode:
  if start > end: return None

  mid = (start + end) // 2
  n = BinaryNode(li[mid])
  n.left = minTreeHelper(li, start, mid - 1)
  n.right = minTreeHelper(li, mid + 1, end)
  return n

def minTree(li: list) -> BinaryNode:
  return minTreeHelper(li, 0, len(li) - 1)

if __name__ == "__main__":
  tree = minTree([1, 2, 3, 4, 5, 6, 7, 8])
  print("In Order:")
  p.inOrderPrint(tree)
  print("\nPre Order:")
  p.preOrderPrint(tree)
  print("\nPost Order:")
  p.postOrderPrint(tree)
  print()
  p.print_tree(tree)

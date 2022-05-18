"""
21: https://leetcode.com/problems/merge-two-sorted-lists/

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. 
The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.


Solutions: 

##### 1
Use dummy head. Insert lowest values of either list until one is empty.
Attach remainder of other list.

Time: O(n + m)
Space: O(n + m)

"""

class Node:
  def __init__(self, val = None, next = None):
    self.val = val
    self.next = next

def merge(l1: Node, l2: Node) -> Node:
  head = curr = Node()

  while l1 and l2:
    if l1.val > l2.val:
      curr.next = l2
      l2 = l2.next
    else:
      curr.next = l1
      l1 = l1.next
    curr = curr.next

  if l1: curr.next = l1
  if l2: curr.next = l2

  return head.next

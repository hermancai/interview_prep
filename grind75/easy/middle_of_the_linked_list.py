"""
876: https://leetcode.com/problems/middle-of-the-linked-list/

Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.


Solutions: 

##### 1
Slow and fast pointer. 
Return slow pointer when fast or fast.next is None.

Time: O(n)
Space: O(1)

"""

class Node:
  def __init__(self, val, next = None):
    self.val = val
    self.next = next

def getMiddle(head: Node) -> Node:
  slow = fast = head

  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

  return slow

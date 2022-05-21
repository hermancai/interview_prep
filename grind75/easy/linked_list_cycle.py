"""
141: https://leetcode.com/problems/linked-list-cycle/

Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached 
again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. 
Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.


Solutions:

##### 1
Use a slow and fast pointer. 
If the fast pointer reaches None, return False.
If there is a cycle, the slow and fast pointer will collide: return True.

Time: O(n)
Space: O(1)

"""

class Node:
  def __init__(self, val, next = None):
    self.val = val
    self.next = next

def isCycle(head: Node) -> bool:
  slow = fast = head

  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow is fast: return True
  
  return False

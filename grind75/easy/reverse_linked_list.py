"""
206: https://leetcode.com/problems/reverse-linked-list/

Given the head of a singly linked list, reverse the list, and return the reversed list.

Solutions:

##### 1
Use one variable to track previous node
Loop through list:
  Update pointers for current node. 

Time: O(n)
Space: O(1)

"""

class Node:
  def __init__(self, val, next = None):
    self.val = val
    self.next = next

def reverse(head: Node) -> Node:
  if not head or not head.next: return head

  # Prev points to the head of the final reversed list      
  prev = None

  while head:
    temp = head  # Hold current node
    head = head.next  # Hold next node

    # Insert current (temp) node in front of prev 
    temp.next = prev  
    prev = temp  
  return prev

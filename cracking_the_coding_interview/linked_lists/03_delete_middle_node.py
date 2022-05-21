'''
Given some middle node in a singly linked list (not the head or tail),
delete that node from the list.

Given a list: 1, 2, 3, 4, 5
Input: 3
Output: The list is now 1, 2, 4, 5

Solutions:

##### 1:
Replace current node value with next node value.
Delete the next node by changing current node link.

Note: This solution does not work if given the tail.
Assume: Node is not the tail or head.

Time: O(1)
Space: O(1)

'''

import singly_linked_list as ll


def deleteMiddleNode(n: ll.Node) -> None:
  if not n or not n.next: return print("Empty or tail node")
  next = n.next
  n.val = next.val
  n.next = next.next
    

if __name__ == "__main__":
  li = ll.SinglyLinkedList([1])
  li.append(2)
  n = li.append(3)
  li.append(4)
  li.append(5)

  deleteMiddleNode(n)
  li.printList()

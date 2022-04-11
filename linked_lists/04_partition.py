'''
Partition a linked list around value x, such that all nodes less than x 
come before all nodes greater than or equal to x.

Input: [3, 5, 8, 5, 10, 2, 1], 5
Output: [3, 1, 2, 10, 5, 5, 8]

Solutions:

##### 1:
Loop through list
  If value is less than x, place it at the head

Time: O(n)
Space: O(1)

'''

from singly_linked_list import SinglyLinkedList


def partition(li: SinglyLinkedList, x: int) -> None:
  if not li.head.next: return None

  prev = li.head
  current = li.head.next

  while current:
    if current.val < x:
      temp = current
      prev.next = current.next
      temp.next = li.head
      li.head = temp
      current = prev.next
    else:
      prev = prev.next
      current = current.next

if __name__ == "__main__":
  li = SinglyLinkedList([3, 5, 8, 5, 10, 2, 1])
  x = 5
  partition(li, x)
  li.printList()

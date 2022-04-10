'''
Find the kth to last element in a singly linked list.

Ask:
Is the list length at least k?

Input:  4, [5, 7, 2, 4, 1, 9, 8, 3]
Output: 1

Solutions:

##### 1
Use a runner that is k spaces away from the other pointer.
Iterate until runner is at the tail.
The other pointer will be at the kth element.

Time: O(n)
Space: O(1)

'''

from singly_linked_list import SinglyLinkedList

def getKthToLast(li: SinglyLinkedList, k: int):
  current = runner = li.head

  for _ in range(k):
    runner = runner.next
    if not runner: return print("k is out of bounds")

  while runner:
    runner = runner.next
    current = current.next

  return current.val


if __name__ == "__main__":
  li = SinglyLinkedList([5, 7, 2, 4, 1, 9, 8, 3])
  k = 4
  print(getKthToLast(li, k))
'''
Given two singly linked lists, determine if the lists intersect.
Return the intersecting node.
Intersection is based on reference, not value.

Input:
3 -> 1 -> 5 -> 9
                \ 
                 7 -> 2 -> 1
                /
          4 -> 6
Output: True

Input: 
3 -> 1 -> 5 -> 9 -> 7 -> 2 -> 1
          4 -> 6 -> 7 -> 2 -> 1
Output: False

Note:
Intersecting lists will always have the same tail.

Solutions: 

##### 1:
Get the length of each list by traveling to the tail.
If tails are not equal by reference, there is no intersection.
Advance the longer list pointer by the difference between lengths.
Advance both lists, comparing nodes until equal.
Return that node.

Time: O(n)
Space: O(1)

'''

import singly_linked_list as ll


def advanceNode(li: ll.SinglyLinkedList, n: int) -> ll.Node:
  curr = li.head
  for _ in range(n):
    curr = curr.next
  return curr

def intersects(l1: ll.SinglyLinkedList, l2: ll.SinglyLinkedList) -> ll.Node:
  # Get length and tail of both lists
  curr1, length1 = l1.head, 1
  while curr1.next:
    length1 += 1
    curr1 = curr1.next
  
  curr2, length2 = l2.head, 1
  while curr2.next:
    length2 += 1
    curr2 = curr2.next
  
  # Check tails by reference
  if curr1 is not curr2:
    return None

  # Advance longer list pointer to match shorter list
  curr1, curr2 = l1.head, l2.head
  if length1 > length2:
    curr1 = advanceNode(l1, length1 - length2)
  elif length1 < length2:
    curr2 = advanceNode(l2, length2 - length1)

  # Traverse both lists until equal node found
  while curr1:
    if curr1 is curr2:
      return curr1
    curr1 = curr1.next
    curr2 = curr2.next

  return None


if __name__ == "__main__":
  l1 = ll.SinglyLinkedList([3, 1, 5, 9])
  l2 = ll.SinglyLinkedList([4, 6])

  n1 = ll.Node(7)
  n2 = ll.Node(2)
  n3 = ll.Node(1)

  l1.append(n1)
  l1.append(n2)
  l1.append(n3)

  l2.append(n1)

  result = intersects(l1, l2)
  if type(result) is ll.Node:
    print(result.val)

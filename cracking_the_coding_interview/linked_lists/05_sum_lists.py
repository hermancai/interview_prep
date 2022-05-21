'''
Given two ints represented as linked lists in reverse, add the numbers
and return the sum as a linked list.
What if the digits are stored in forward order?

Input: [7, 1, 6], [5, 9, 2]
Output: [2, 1, 9]
Explanation: 617 + 295 = 912

Solutions: 

##### 1:
Loop through both lists at the same time.
  Keep track of a carry over digit. 
  Add that digit to the next node while building sum list.
Check for remaining values in both given lists. Add to sum.
  If carry over exists, add to tail of sum list.

Time: O(n)
Space: O(n)

'''

from singly_linked_list import SinglyLinkedList

def sumLists(l1: SinglyLinkedList, l2: SinglyLinkedList) -> SinglyLinkedList:
  curr1, curr2 = l1.head, l2.head
  sum = SinglyLinkedList()
  carry = 0

  while curr1 or curr2:
    v1 = curr1.val if curr1 else 0
    v2 = curr2.val if curr2 else 0
    val = v1 + v2 + carry
    carry = 0
    if val > 9:
      carry = 1
      val = val % 10
    sum.append(val)
    if curr1: curr1 = curr1.next
    if curr2: curr2 = curr2.next

  if carry > 0:
    sum.append(1)

  return sum


if __name__ == "__main__":
  l1 = SinglyLinkedList([1, 1, 1])
  l2 = SinglyLinkedList([9, 1, 9])
  result = sumLists(l1, l2)
  result.printList()

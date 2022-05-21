'''
Remove duplicates from an unsorted linked list.
What if you cannot use extra data structures?

Input:  4, 7, 2, 4, 9, 5, 3, 3, 7
Output: 4, 7, 2, 9, 5, 3

Solutions:

##### 1:
Use a set to keep track of unique elements.
If the current element is in the set, remove from the list.
Else add the current element to the set.

Time: O(n)
Space: O(n)


##### 2:
Iterate through the list with two pointers.
The current pointer iterates normally.
The runner pointer checks every subsequent node of current.

Time: O(n^2)
Space: O(1)

'''

from singly_linked_list import SinglyLinkedList


# Solution 1
def deleteDupes1(li: SinglyLinkedList) -> None:
  valSet = set()
  current = li.head
  previous = None

  while current:
    if current.val not in valSet:
      valSet.add(current.val)
      previous = current
    else:
      previous.next = current.next
    current = current.next

# Solution 2
def deleteDupes2(li: SinglyLinkedList) -> None:
  current = li.head

  while current:
    runner = current
    while runner.next:
      if (runner.next.val == current.val):
        runner.next = runner.next.next
      else:
        runner = runner.next
    current = current.next


if __name__ == "__main__":
  li = SinglyLinkedList([4, 7, 2, 4, 9, 5, 3, 3, 7])
  deleteDupes2(li)
  li.printList()

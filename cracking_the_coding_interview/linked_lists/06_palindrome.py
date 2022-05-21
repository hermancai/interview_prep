'''
Check if a linked list is a palindrome.

Input: [1, 2, 3, 4, 5, 4, 3, 2, 1]
Output: True

Input: [1, 2, 3, 4, 4, 3, 2, 1]
Output: True

Solutions:

##### 1:
Reverse the list and compare it to the original.

Time: O(n)
Space: O(n)


##### 2:
Use a slow and fast pointer to get to the middle of the list.
  Place each value the slow pointer reaches onto a stack.
Use the slow pointer to get to the end of the list while
  comparing and popping the stack.

Time: O(n)
Space: O(n)

'''

from singly_linked_list import SinglyLinkedList

# Solution 2
def isPalindrome(li: SinglyLinkedList) -> bool:
  slow = fast = li.head
  stack = []

  # Get to middle of list by having fast go two spaces per iteration
  while fast and fast.next:
    stack.append(slow.val)
    slow = slow.next
    fast = fast.next.next

  # Handle odd length list
  if fast is not None:
    slow = slow.next

  # Compare rest of list with stack
  while slow:
    if stack.pop() != slow.val:
      return False
    slow = slow.next
  
  return True


if __name__ == "__main__":
  li = SinglyLinkedList([1, 2, 3, 4, 5, 4, 3, 2, 1])
  print(isPalindrome(li))

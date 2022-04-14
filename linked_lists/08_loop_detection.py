'''
Given a linked list that might contain a loop, return 
the node at the beginning of the loop if it exists.

Input: 1 -> 2 -> 3 -> 4 -> 5 -> 3 (same node as previous '3')
Output: 3

Test case:
Tail loops into head.

Solution: 
Use a Fast and Slow pointer. k = steps from head to the start of the loop.
When Slow reaches the start of the loop after k steps, Fast will 
be k steps into the loop because it is moving twice as fast. 
Now Fast and Slow are both in the loop. Fast being k nodes ahead of Slow 
also means Fast is (loop size - k) spaces away from Slow. Fast gets one node 
closer to Slow every iteration. This means Fast and Slow will collide after
(loop size - k) iterations. This means Slow, which started at the beginning 
of the loop, collided with Fast at (loop size - k) nodes into the loop.
This means the collision node is k nodes away from the start of the loop.
It is given that the head is also k nodes away from the start of the loop.
Use Slow and a new head pointer to iterate through the whole list again, until 
a node matches by reference. That node is the start of the loop.

Time: O(n)
Space: O(1)

'''

import singly_linked_list as ll


def findLoop(li: ll.SinglyLinkedList) -> ll.Node:
  slow = fast = li.head

  # Loop until end of list or slow and fast collide
  while fast and fast.next:
    fast = fast.next.next
    slow = slow.next
    if fast is slow:
      break
  
  # In case list is not a loop
  if not fast or not fast.next:
    return None

  # Slow and head are now same distance from loop start
  curr = li.head
  while True:
    if curr is slow:
      return curr
    curr = curr.next
    slow = slow.next

if __name__ == "__main__":
  li = ll.SinglyLinkedList([1, 2])
  n1 = ll.Node(3)
  n2 = ll.Node(4)
  n3 = ll.Node(5)
  
  li.append(n1)
  li.append(n2)
  li.append(n3)
  n3.next = n1

  result = findLoop(li)
  if type(result) is ll.Node:
    print(result.val)

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

class SinglyLinkedList:
  def __init__(self, li: list = None) -> None:
    if not li:
      self.head = self.tail = None
      return

    self.head = self.tail = Node(li[0])

    for i in range(1, len(li)):
      self.append(li[i])

  def append(self, val) -> Node:
    temp = val if type(val) is Node else Node(val)

    if not self.head:
      self.head = self.tail = temp
      return
    
    self.tail.next = temp
    self.tail = temp
    return temp

  def pop(self) -> Node:
    if self.tail is self.head:
      temp = self.tail
      self.tail = self.head = None
      return temp
    
    curr = self.head
    while curr.next.next:
      curr = curr.next
    
    curr.next = None
    return curr

  def printList(self) -> None:
    current = self.head
    while current:
      print(current.val, end=" ")
      current = current.next
    print()

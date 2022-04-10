class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

class SinglyLinkedList:
  def __init__(self, li: list) -> None:
    if not list: return

    self.head = self.tail = Node(li[0])

    for i in range(1, len(li)):
      self.append(li[i])

  def append(self, val) -> Node:
    temp = Node(val)
    self.tail.next = temp
    self.tail = temp
    return temp

  def printList(self) -> None:
    current = self.head
    while current:
      print(current.val, end=" ")
      current = current.next
    print()

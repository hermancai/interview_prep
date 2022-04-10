class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

class SinglyLinkedList:
  def __init__(self, li: list):
    if not list: return

    self.head = self.tail = Node(li[0])

    for i in range(1, len(li)):
      temp = Node(li[i])
      self.tail.next = temp
      self.tail = temp

  def printList(self):
    current = self.head
    while current:
      print(current.val, end=" ")
      current = current.next
    print()

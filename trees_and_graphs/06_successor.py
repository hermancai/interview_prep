'''
Find the next (in order successor) node of a given binary search tree node.
Assume each node has a link to its parent.

Solution:
Given node n:
By definition of in order traversal, everything in n's left subtree 
  has been traversed.
If n has a right subtree, then the successor is the leftmost node 
  of the right subtree.
If n does not have a right subtree, then the successor must be in a parent.
Give parent node q of current node n, and n has no right subtree:
  If n is the right child of q, that means q has already been traversed.
    Move on to check the parent's parent.
    Keep going up while n is the right child of q.
  If n is the left child of q, q would be the successor of in order traversal.
If n is the rightmost node in the entire tree (ie end of in order traversal),
  return None.

Time: O(n)
Space: O(1)

'''

from binary_node import BinaryNode as Node

def getNextNode(n: Node) -> Node:
  if n.right:
    # Return the leftmost node in the right subtree
    n = n.right
    while n.left:
      n = n.left
    return n
  
  p = n.parent
  # Go up until n is the left child of p
  while p and p.right is n:
    n = p
    p = p.parent
  return p


if __name__ == "__main__":
  n2 = Node(2)
  n3 = Node(3)
  n4 = Node(4)
  n5 = Node(5)
  n6 = Node(6)
  n7 = Node(7)

  n2.parent = n4.parent = n3
  n3.left, n3.right, n3.parent = n2, n4, n5
  n5.left, n5.right = n3, n7
  n7.left, n7.parent = n6, n5
  n6.parent = n7

  next = getNextNode(n7)
  if next: print(next.val)

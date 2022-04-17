'''
Given a directed graph and two nodes (S and E), find out if 
there is a path from S to E.

Solutions:

##### 1
Depth first traversal

Time: O(n) where n is the number of nodes
Space: O(d) where d is the max depth of the graph


##### 2
Breadth first traversal

Time: O(n) where n is the number of nodes
Space: O(n) where n is the number of nodes

'''

from collections import deque
from node import Node

# Solution 2
def search(s: Node, e: Node) -> bool:
  if s is e: return True

  q = deque()
  q.append(s)
  s.visited = True

  # Loop until queue is empty i.e. every connected node is visited
  while q:
    curr = q.popleft()
    # Add unvisited neighbors of current node
    for n in curr.neighbors:
      if not n.visited:
        if n is e: return True
        # Mark as visited to avoid infinite loop
        n.visited = True
        q.append(n)
    print(curr.val)

  return False


if __name__ == "__main__":
  s = Node(1)
  n2 = Node(2)
  n3 = Node(3)
  n4 = Node(4)
  e = Node(5)
  n6 = Node(6)

  s.neighbors.extend([n2, n3, n4])
  n4.neighbors.append(e)
  e.neighbors.append(n6)

  print(search(s, e))

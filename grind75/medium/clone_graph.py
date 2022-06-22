"""
133: https://leetcode.com/problems/clone-graph/

Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

Test case format:
For simplicity, each node's value is the same as the node's index (1-indexed). 
For example, the first node with val == 1, the second node with val == 2, and so on. 
The graph is represented in the test case using an adjacency list.
An adjacency list is a collection of unordered lists used to represent a finite graph. 
Each list describes the set of neighbors of a node in the graph.
The given node will always be the first node with val = 1. 
You must return the copy of the given node as a reference to the cloned graph.


Solutions:

##### 1 (own solution)
Create map. Key = value: int; Value = neighbors: List[Node]. Add initial node value
Create stack with initial node.
While stack is not empty:
  Pop node from stack.
  Loop through node neighbors:
    If neighbor is not in map:
      Add neighbor node to stack
      Add neighbor node value to map
Create list of fixed length = length of map + 1
Loop through map keys:
  Create Node of val = (key) in list[key]
Loop through map keys:
  Loop through neighbors in map[key]:
    Append list[key] node into neighbors list of current node

Time: O(E + V) where E is number of edges in graph and V is number of nodes
Space: O(E + V)


##### 2
Create map. Key = node: Node; Value = clone: Node.
Create and keep reference to clone of initial node with empty neighbors list. Add to map.
Create stack with initial node.
While stack is not empty:
  Pop node from stack.
  Loop through node neighbors:
    If neighbor is not in map:
      Create clone of neighbor with empty neighbors list
      Add neighbor and clone to map
      Append clone of neighbor to neighbors list of clone of current node in map
      Add neighbor to stack
Return initial node clone


"""

class Node:
  def __init__(self, val: int, neighbors: list = None):
    self.val = val
    self.neighbors = neighbors if neighbors is None else []


def cloneGraph(node: Node) -> Node:
  m = {}
  m[node.val] = node.neighbors

  stack = [node]

  while stack:
    node = stack.pop()
    for neighbor in node.neighbors:
      if neighbor not in m:
        stack.append(neighbor)
        m[neighbor.val] = neighbor.neighbors

  nodeList = [0] * (len(m) + 1)

  for n in m.keys():
    nodeList[n] = Node(n)

  for n in m.keys():
    for neighbor in m[n]:
      nodeList[n].neighbors.append(nodeList[neighbor.val])

  return nodeList[1]

'''
Find the first common ancestor of two nodes in a binary tree.
Avoid storing additional nodes. Do not assume this is a BST.

Ask: Does each node have a link to its parent?

Solutions: 

##### 1
Assuming each node has link to parent

Given nodes p and q, find the depths of both.
Move the deeper node upwards (via parent) to match depth of other node.
Move both nodes upwards until the parent nodes match.

Note that this is similar to finding the intersection of two linked lists.

Time: O(d) where d is the depth of the deeper node.
Space: O(1)


##### 2
Assuming each node has link to parent

Given nodes p and q.
Move upwards with p until a node is found that covers q. 
  On each move up, a sibling subtree of the current node may be found.
  Check this sibling subtree for q. 

Time: O(n) where n is the number of nodes in the tree
Space: O(1)


##### 3
Assuming no link to parent node

Given nodes p and q, starting with root of tree.
Check if p and q are both on the left or right side. (ie which of the current 
node's children cover p/q?)
  If they are on different sides, the current node is the ancestor.
Move down left/right depending which side p and q are both on.
Repeat the check until p and q are on different sides.

Time: O(n). The algorithm repeatedly checks nodes, but on each iteration down 
  to a child node, that node's sibling subtree will be ignored.
Space: O(1)

'''
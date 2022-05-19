"""
226: https://leetcode.com/problems/invert-binary-tree/

Given the root of a binary tree, invert the tree, and return its root.


Solutions:

##### 1
Pre-order OR post-order traversal, swapping left and right children of current node.

Time: O(n)
Space: O(d) where d is the depth of the tree


##### 2 
Swap left and right children with returned nodes from recursive calls.

Time: O(n)
Space: O(d) 


##### 3
Use a stack and iterative instead of recursive.
This is depth first traversal. Use a queue for breath first.
While the stack is not empty, swap the node's children and 
  add the children to the stack.

Time: O(n)
Space: O(n)

"""

class Node:
  def __init__(self, val = 0, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right

# Solution 1
def invert1(root: Node) -> Node:
  if root:
    root.left, root.right = root.right, root.left
    invert1(root.left)
    invert1(root.right)
  return root

# Solution 2
def invert2(root: Node) -> Node:
  if not root: return None

  root.left, root.right = invert2(root.right), invert2(root.left)
  return root

# Solution 3
def invertStack(root: Node) -> Node:
  if not root: return None
  stack = [root]

  while stack:
    curr = stack.pop()
    if curr:
      curr.left, curr.right = curr.right, curr.left
      stack += curr.left, curr.right

  return root

# Source: https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
def print_tree(root, val="val", left="left", right="right"):
    def display(root, val=val, left=left, right=right):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if getattr(root, right) is None and getattr(root, left) is None:
            line = '%s' % getattr(root, val)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if getattr(root, right) is None:
            lines, n, p, x = display(getattr(root, left))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if getattr(root, left) is None:
            lines, n, p, x = display(getattr(root, right))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = display(getattr(root, left))
        right, m, q, y = display(getattr(root, right))
        s = '%s' % getattr(root, val)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    lines, *_ = display(root, val, left, right)
    for line in lines:
        print(line)


if __name__ == "__main__":
  root = Node(5, Node(3, Node(2), Node(4)), Node(7, Node(6), Node(8)))
  print_tree(root)
  invertStack(root)
  print_tree(root)

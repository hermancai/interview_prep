"""
150: https://leetcode.com/problems/evaluate-reverse-polish-notation/

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. 
That means the expression would always evaluate to a result, 
and there will not be any division by zero operation.


Solutions:

##### 1
Use stack.
Loop through each token:
  If token is a number:
    Push to stack
  Else pop twice from stack and evaluate expression.
Return remaining value in stack.

Time: O(n)
Space: O(n)

"""

def evalRPN(tokens: list) -> int:
  def evaluate(v1: int, v2: int, op: str):
    if op == "+":
      return v2 + v1
    elif op == "-":
      return v2 - v1
    elif op == "*":
      return v2 * v1
    else:
      # Int conversion behaves differently compared to floor division
      # int() truncates towards 0
      return int(v2 / v1) 
  
  def validInt(s: str) -> bool:
    try:
      int(s)
      return True
    except ValueError:
      return False

  stack = []
  for c in tokens:
    if validInt(c):
      stack.append(int(c))
    else:
      stack.append(evaluate(stack.pop(), stack.pop(), c))
  
  return stack[0]


if __name__ == "__main__":
  print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

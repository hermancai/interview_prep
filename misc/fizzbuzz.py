'''
Given an integer, return a string array (1-indexed) where:
  -answer[i] == "fizzbuzz" if i is divisible by 3 and 5
  -answer[i] == "fizz" if i is divisible by 3
  -answer[i] == "buzz" if i is divisible by 5
  -answer[i] == i as a string if not of above are true

Input: 5
Output: ["1", "2", "fizz", "4", "buzz"]

'''

def func1(n: int) -> list:
  result = []

  for i in range(1, n + 1):
    if i % 15 == 0: result.append("fizzbuzz")
    elif i % 3 == 0: result.append("fizz")
    elif i % 5 == 0: result.append("buzz")
    else: result.append(str(i))

  return result


# This method uses less conditionals but uses more space 
# because of immutable strings.
def func2(n: int) -> list:
  result = []

  for i in range(1, n + 1):
    ans = ""
    if i % 3 == 0: ans += "fizz"
    if i % 5 == 0: ans += "buzz"
    result.append(str(i) if len(ans) == 0 else ans)

  return result


if __name__ == "__main__":
  print(func2(15))

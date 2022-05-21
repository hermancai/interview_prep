'''
Return all subsets of a set of n elements.

Solution:

Cases: 
n = 0 returns one subset: {}
n = 1 returns two subsets: {}, {a1}
n = 2 returns four: {}, {a1}, {a2}, {a1, a2}
n = 3 returns eight: {}, {a1}, {a2}, {a3}, {a1, a2}, {a1, a3}, {a2, a3}, {a1, a2, a3}

P(n-1) contains all subsets in P(n) that do not contain the newest element. 
To create P(n) using P(n-1), add the new element to each subset in P(n-1) as 
  well as adding the original subsets. This creates 2^n results. 

Time: O(n * 2^n)
Space: O(n * 2^n)

'''

def getSubsets(li, index):
  # Base case: n = number of elements in original list.
  # Return and start building the list now
  if len(li) == index: return [[]]
  
  allSubsets = getSubsets(li, index + 1)
  item = li[index]  # Basically iterating through the given list backwards
  moreSubsets = []  # New list to hold cloned subsets with new element added

  # Loop through all subsets currently in final answer
  for s in allSubsets:
    newSubset = [] + s  # Clone the current subset
    newSubset.append(item)  # Add the newest element to that clone
    moreSubsets.append(newSubset)  # Add to list

  allSubsets += moreSubsets  # Combines the lists  
  return allSubsets


if __name__ == "__main__":
  li = [1, 2, 3, 4, 5]
  print(getSubsets(li, 0))

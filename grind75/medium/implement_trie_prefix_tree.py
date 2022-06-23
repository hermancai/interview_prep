"""
208: https://leetcode.com/problems/implement-trie-prefix-tree/

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently 
store and retrieve keys in a dataset of strings. There are various applications of this 
data structure, such as autocomplete and spellchecker.
Implement the Trie class:
  Trie() Initializes the trie object.
  void insert(String word) Inserts the string word into the trie.
  boolean search(String word) Returns true if the string word is in the trie 
    (i.e., was inserted before), and false otherwise.
  boolean startsWith(String prefix) Returns true if there is a previously inserted string word 
    that has the prefix prefix, and false otherwise.

Notes: 
A trie only contains a word if the last char is somehow marked as the end of the word.
  If there is no mark, the word does not count as existing in the trie.

Solution:

##### 1
Use a map where each key represents a child node. Keys will be nested maps.
insert: Keep track of current "node". Loop string. Add a non-alpha char as null terminator.
search: Pass to startsWith(string + designated null char)
searchWith: Keep track of current. Loop string. Return false if key is not found for current char.

Time: O(n) where n is length of word for all operations.
Space: O(n) for insert. O(1) for search and startsWith.

"""

class Trie:
  def __init__(self):
    self.trie = {}

  def insert(self, word):
    curr = self.trie
    for c in word:
      if c not in curr:
        curr[c] = {}
      curr = curr[c]
    # Arbitrary non-alpha null terminator
    curr["~"] = True

  def search(self, word):
    return self.startsWith(word + "~")
  
  def startsWith(self, word):
    curr = self.trie
    for c in word:
      if c not in curr:
        return False
      curr = curr[c]
    return True

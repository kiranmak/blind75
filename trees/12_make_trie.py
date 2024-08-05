'''
208. Implement Trie (Prefix Tree)
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
     
'''

class TrieNode:
    def __init__(self):
        self.chnodes = [None] * 26
        self.isLeaf = False

class Trie:
    
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        tnode = self.root
        for letter in word:
            idx = ord(letter) - ord('a')
            if not tnode.chnodes[idx]:
                tnode.chnodes[idx] = TrieNode()
            tnode = tnode.chnodes[idx]
        tnode.isLeaf = True
        
    def search(self, word: str) -> bool:
        tnode = self.root
        for letter in word:
            idx = ord(letter) - ord('a')
            if not tnode.chnodes[idx]:
                return False
            tnode = tnode.chnodes[idx]
        return tnode.isLeaf
        

    def startsWith(self, prefix: str) -> bool:
        tnode = self.root
        for letter in prefix:
            idx = ord(letter) - ord('a')
            if not tnode.chnodes[idx]:
                return False
            tnode = tnode.chnodes[idx]
        if not tnode:
            return False
        return True


# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("apple");
result = trie.search("apple") # return True
print("search apple", result)
result = trie.search("app") # return False
print("search app", result)
result = trie.startsWith("app") # return True
print("startwith app", result)
trie.insert("app")
result = trie.search("app") # return True
print("search app", result)
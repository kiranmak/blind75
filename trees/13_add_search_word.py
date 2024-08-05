'''
211. Design Add and Search Words Data Structure
Design a data structure that supports adding new words and finding if a string matches any previously added string.
Implement the WordDictionary class:
WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
Example:
Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
'''
class TrieNode:
    def __init__(self):
        self.len = 26
        self.chnodes = [None] * self.len
        self.isLeaf = False
        self.count = 0

    def getC(self, ix):
        ch = chr(ix + ord('a'))
        return ch

    def prn_letter(self, ix, level):
        x = '-'
        ch = chr(ix + ord('a'))
        print(x*level, ch, end='')
            
    def _pprint(self, level):
                        
        if self.isLeaf:
            print(".")  # Terminate with '.'

        for ix in range(self.len):
            if not self.chnodes[ix]:
                continue
            self.prn_letter(ix, level)
            node = self.chnodes[ix]
            node._pprint(level+1)

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()        

    def addWord(self, word: str) -> None:
        mydict = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if not mydict.chnodes[idx]:
                mydict.chnodes[idx] = TrieNode()
            mydict = mydict.chnodes[idx]
        mydict.isLeaf = True
        mydict.count += 1
    

    def pprint(self):
        self.root._pprint(0)

        
            
    def search(self, word: str) -> bool:
        node = self.root
        ans = self.wildcard(node, word)
        return ans

    def wildcard(self, node:TrieNode, word) -> bool:
        if not node:
            return False

        if not word:
            return True
        if node.isLeaf:
            return True 
       
        if word[0] != '.':
            idx = ord(word[0]) - ord('a')
            child = node.chnodes[idx]
            if child:
                return self.wildcard(child, word[1:])
            else: return False
       
        if word[0] == '.':
            for i in range(node.len):
                if node.chnodes[i]:
                    child = node.chnodes[i]
                    ans = self.wildcard(child, word[1:])
                    if ans:
                        return True
        return False
        
action = ["addWord","addWord","addWord","addWord",
          "search", "search", "addWord","search",
          "search", "search", "search", "search",
          "search"]
words = [["at"], ["and"], ["an"], ["add"],
         ["a"],  [".at"], ["bat"],[".at"],
         ["an."],["a.d."],["b."], ["a.d"],
         ["."]]

worddict = WordDictionary()
worddict.addWord("at")
worddict.addWord("and")
worddict.addWord("an")
worddict.addWord("add")

ans = worddict.search("a")
print("ans to search 'a'", ans)
ans = worddict.search(".at")
print("ans to search '.at'", ans)

worddict.addWord("bat")
worddict.pprint()

ans = worddict.search(".at")
print("ans to search '.at'", ans)

ans = worddict.search("an.")
print("ans to search 'an.'", ans)

'''
ans = worddict.search("a.d.")
print("ans to search 'a.d.'", ans)

ans = worddict.search("b.")
print("ans to search 'b.'", ans)

for i in range(len(action)):
    if action[i] == "addword":
        worddict.addword(words[i])
        print("[",i,"]added:", words[i])
    if action[i] == "search":
        ans = worddict.search(words[i])
        print("[",i,"]search:", words[i], "found=", ans)
        
'''
'''
worddict.addWord("bad")
worddict.addWord("dad")
worddict.addWord("mad")

ans = worddict.search("pad") #return False
print("ans to search 'pad'", ans)
ans = worddict.search("bad") #return True
print("search 'bad'", ans)
ans = worddict.search(".ad") #return True
print("search '.ad'", ans)
ans = worddict.search("b..") #return True
print("search 'b..'", ans)
'''
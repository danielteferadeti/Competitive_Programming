class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False 
class Trie:

    def __init__(self): 
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        root = self.root
        
        for char in word:
            if char not in root.children:
                newNode = TrieNode()
                root.children[char] = newNode
            root = root.children[char]
        root.isEndOfWord = True
        
    def startsWith(self, prefix: str) -> bool:
        root = self.root
        count = 0
        for char in prefix:
            if char not in root.children:
                return False
            count+=1
            root = root.children[char]
        return root.isEndOfWord
    
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        myTrie = Trie()
        
        myTrie.insert(pref)
        
        count = 0
        for word in words:
            if myTrie.startsWith(word[:len(pref)]):
                count +=1
        return count 
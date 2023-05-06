class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfNode = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            
        cur.endOfNode = True

    def search(self, word: str) -> bool:
        cur = self.root 
        for c in word: 
            if c not in cur.children: 
                return False 
            cur = cur.children[c] 
            
        return cur.endOfNode
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root 
        for c in prefix: 
            if c not in cur.children: 
                return False 
            cur = cur.children[c] 
            
        return True    


trie = Trie()
print(trie.insert("apple"))     # None
print(trie.search("apple"))     # True
print(trie.search("app"))       # False
print(trie.startsWith("app"))   # True
print(trie.insert("app"))       # None
print(trie.search("app"))       # True
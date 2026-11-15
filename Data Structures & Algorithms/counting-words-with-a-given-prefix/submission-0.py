class TrieNode:
    def __init__(self):
        self.children={}
        self.is_end=False
        self.prefix_count=0
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        node=self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch]=TrieNode()
            node=node.children[ch]
            node.prefix_count+=1
        node.is_end=True
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        trie=Trie()
        root=trie.root
        for word in words:
            trie.insert(word)
        for ch in pref:
            if ch in root.children:
                root=root.children[ch]
            else:
                return 0
        return root.prefix_count
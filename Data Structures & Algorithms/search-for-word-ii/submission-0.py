class TrieNode:
    def __init__(self):
        self.children={}
        self.is_end=False
        self.word=None

class Trie:

    def __init__(self):
        self.root=TrieNode()

    def insert(self,word):
        node=self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch]=TrieNode()
            node=node.children[ch]
        node.is_end=True
        node.word=word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie=Trie()
        for word in words:
            trie.insert(word)
        dir=[(1,0),(-1,0),(0,1),(0,-1)]
        r=len(board)
        c=len(board[0])
        ans=[]
        def dfs(row,col,node):
            if row<0 or row>=r or col<0 or col>=c:
                return 
            ch=board[row][col]
            if ch=='#':
                return 
            if ch not in node.children :
                return 
            node=node.children[ch]
            if node.is_end:
                ans.append(node.word)
                node.is_end=False
                node.word=None
            if not node.children :
                return 
            temp=ch
            board[row][col]='#'
            for i,j in dir:
                dfs(row+i,col+j,node)
            board[row][col]=temp
        for i in range(r):
            for j in range(c):
                if board[i][j] in trie.root.children:
                    dfs(i,j,trie.root)
        return ans
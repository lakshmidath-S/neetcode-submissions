class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        curr=[]
        def match(open,close):
            if n==open and n==close:
                ans.append("".join(curr[:]))
                return
            if open<n:
                curr.append('(')
                match(open+1,close)
                curr.pop()
            if close<open:
                curr.append(')')
                match(open,close+1)
                curr.pop()
        match(0,0)
        return ans
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        for i in s:
            if i.isalpha() or i=='(':
                stack.append(i)
            elif i==')':
                rev=[]
                while stack and stack[-1]!='(':
                    rev.append(stack.pop())
                stack.pop()
                for j in rev:
                    stack.append(j)
        return  ''.join(stack)

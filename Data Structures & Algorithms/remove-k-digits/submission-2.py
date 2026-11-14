class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for i in num:
            while stack and k>0 and stack[-1]>i:
                stack.pop()
                k-=1
            stack.append(i)
        if k>0:
            stack=stack[:-k]
        for i in range(len(stack)):
            if stack[i]!='0':
                return ''.join(stack[i:])
        return '0'
        

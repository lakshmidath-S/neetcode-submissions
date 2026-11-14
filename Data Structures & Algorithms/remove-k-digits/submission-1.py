class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num)==k:
            return '0'
        stack=[]
        for i in num:
            if not stack:
                stack.append(i)
            elif stack and stack[-1]<=i:
                stack.append(i)
            elif stack and k>0 and stack[-1]>i:
                while stack and k>0 and stack[-1]>i:
                    stack.pop()
                    k-=1
                stack.append(i)
            elif k==0:
                stack.append(i)
        if k>0:
            stack=stack[:-k]
        for i in range(len(stack)):
            if stack[i]!='0':
                return ''.join(stack[i:])
        return '0'
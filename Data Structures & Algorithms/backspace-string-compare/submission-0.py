class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def parse(arr):
            stack=[]
            for i in arr:
                if i=='#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(i)
            return stack
        return parse(s)==parse(t)
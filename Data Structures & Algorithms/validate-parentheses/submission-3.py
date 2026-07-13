class Solution:
    def isValid(self, s: str) -> bool:
        pairs={'}':'{',']':'[',')':'('}
        i=0
        stack=[]
        while(i<len(s)):
            if s[i]=='[' or s[i]=='{' or s[i]=='(':
                stack.append(s[i])
                i+=1
            elif s[i]==']' or s[i]=='}' or s[i]==')':
                if len(stack)>0:
                    a=stack.pop()
                else:
                    return False
                if a==pairs[s[i]]:
                    i+=1
                else:
                    return False
        if len(stack)>0:
            return False
        return True


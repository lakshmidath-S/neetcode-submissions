class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        i=0
        while(i<len(s)):
            if s[i]=='[' or s[i]=='{' or s[i]=='(':
                stack.append(s[i])
                i+=1
            elif s[i]==']':
                if len(stack)>0:
                    a=stack.pop()
                    if a=='[':
                        i+=1
                        continue
                    else:
                        return False
                else:
                    return False
            elif s[i]=='}':
                if len(stack)>0:
                    a=stack.pop()
                    if a=='{':
                        i+=1
                        continue
                    else:
                        return False
                else:
                    return False
            elif s[i]==')':
                if len(stack)>0:
                    a=stack.pop()
                    if a=='(':
                        i+=1
                        continue
                    else:
                        return False
                else:
                    return False
        if len(stack)>0:
            return False
        return True


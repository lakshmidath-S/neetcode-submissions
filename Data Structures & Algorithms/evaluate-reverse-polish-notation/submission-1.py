class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(len(tokens)):
            if tokens[i] not in["+","-","*","/"]:
                stack.append(int(tokens[i]))
                continue
            else:
                num2=stack.pop()
                num1=stack.pop()
                if tokens[i]=="+":
                    result=num1+num2
                elif tokens[i]=="/":
                    result=num1/num2
                elif tokens[i]=="-":
                    result=num1-num2
                elif tokens[i]=="*":
                    result=num1*num2
                stack.append(int(result))
        return stack[-1]
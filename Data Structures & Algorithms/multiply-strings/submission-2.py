class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1=0
        for ch in num1:
            n1=n1*10+int(ch)
        n2=0
        for ch in num2:
            n2=n2*10+int(ch)
        return str(n1*n2)
        
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def value(ch):
            if ch=='0':
                return 0
            if ch=='1':
                return 1
            if ch=='2':
                return 2
            if ch=='3':
                return 3
            if ch=='4':
                return 4
            if ch=='5':
                return 5
            if ch=='6':
                return 6
            if ch=='7':
                return 7
            if ch=='8':
                return 8
            if ch=='9':
                return 9
            else:
                return
        n1=0
        for ch in num1:
            n1=n1*10+value(ch)
        n2=0
        for ch in num2:
            n2=n2*10+value(ch)
        return str(n1*n2)
        
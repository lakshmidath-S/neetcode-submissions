class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carr=0
        result=[]
        i=len(a)-1
        j=len(b)-1
        while i>-1 or j>-1:
            num1=int(a[i]) if i>-1 else 0
            num2=int(b[j]) if j>-1 else 0
            i-=1
            j-=1
            if num1==1 and num2==1:
                if carr==1:
                    result.append(1)
                else:
                    result.append(0)
                    carr=1
                continue
            elif (num1==1 and num2==0) or (num1==0 and num2==1):
                if carr==1:
                    result.append(0)
                else:
                    result.append(1)
                continue
            elif num1==0 and num2==0:
                if carr==1:
                    result.append(1)
                    carr=0
                else:
                    result.append(0)
        if carr==1:
            result.append(1)
        return "".join(map(str,result[::-1]))



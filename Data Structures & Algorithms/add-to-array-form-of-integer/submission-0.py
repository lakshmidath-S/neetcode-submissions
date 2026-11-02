class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        carry=0
        i=0
        while i<len(num) or k>0 or carry>0:
            if i<len(num):
                s=num[-1-i]+k%10+carry
                num[-1-i]=s%10
                carry=s//10
            else:
                s=k%10+carry
                num.insert(0,s%10)
                carry=s//10
            i+=1
            k=k//10
        return num
                
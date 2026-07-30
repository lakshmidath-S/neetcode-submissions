class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=0
        for i in range(len(digits)-1,-1,-1):
            if i==len(digits)-1:
                carry=1
            sum=digits[i]+carry
            if sum>9:
                carry=1
                digits[i]=sum-10
            else:
                carry=0
                digits[i]=sum
        if carry==1:
            digits=[1]+digits
        return digits

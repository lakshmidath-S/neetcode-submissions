class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=1
        for i in range(len(digits)-1,-1,-1):
            total=digits[i]+carry
            if total>9:
                carry=1
                digits[i]=total-10
            else:
                carry=0
                digits[i]=total
        if carry==1:
            digits=[1]+digits
        return digits

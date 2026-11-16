class Solution:
    def largestOddNumber(self, num: str) -> str:
        while num and int(num[-1])%2==0:
            num=num[:len(num)-1]
        return num

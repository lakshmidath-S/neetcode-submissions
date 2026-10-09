class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero=0
        one=0
        two=0
        for i in nums:
            if i==0:
                zero+=1
            elif i==1:
                one+=1
            else:
                two+=1
        for i in range(len(nums)):
            if zero>0:
                zero-=1
                nums[i]=0
            elif one>0:
                one-=1
                nums[i]=1
            else:
                nums[i]=2

        
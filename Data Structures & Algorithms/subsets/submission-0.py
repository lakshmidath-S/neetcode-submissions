class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sub=[]
        def back(i):
            if i==len(nums):
                sub.append(a[:])
                return
            back(i+1)
            a.append(nums[i])
            back(i+1)
            a.pop()
        a=[]
        back(0)
        return sub

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def back(start):
            ans.append(curr[:])
            for i in range(start,len(nums)):
                if i>start and nums[i]==nums[i-1]:
                    continue
                curr.append(nums[i])
                back(i+1)
                curr.pop()
        curr=[]
        nums.sort()
        back(0)
        return ans
            
            
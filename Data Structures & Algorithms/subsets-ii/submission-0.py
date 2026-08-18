class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        def back(i):
            if i==len(nums) :
                ans.add(tuple(curr[:]))
                return
            back(i+1)
            curr.append(nums[i])
            back(i+1)
            curr.pop()
        curr=[]
        nums.sort()
        back(0)
        return [list(a) for a in ans]
            
            
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        l=[]
        visited = [False] * len(nums)
        def back(a):
            if len(a)==len(nums):
                l.append(a[:])
                return
            for j in range(len(nums)):
                if visited[j]==False:
                    a.append(nums[j])
                    visited[j]=True
                    back(a)
                    visited[j]=False
                    a.pop()
                
        a=[]
        back(a)
        return l
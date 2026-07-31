class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        l=[]
        visited = [False] * len(nums)
        def back(i,a):
            if len(a)==len(nums):
                l.append(a[:])
                return
            for j in range(len(nums)):
                if visited[j]==False:
                    a.append(nums[j])
                    visited[j]=True
                    back(i+1,a)
                    visited[j]=False
                    a.pop()
                
        a=[]
        back(0,a)
        return l
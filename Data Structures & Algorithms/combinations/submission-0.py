class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        nums=[x for x in range(1,n+1)]
        curr=[]
        def back(curr,i):
            if len(curr)==k:
                ans.append(curr[:])
                return
            if i==n:
                return 
            curr.append(nums[i])
            back(curr,i+1)
            curr.pop()
            back(curr,i+1)
        back([],0)
        return ans
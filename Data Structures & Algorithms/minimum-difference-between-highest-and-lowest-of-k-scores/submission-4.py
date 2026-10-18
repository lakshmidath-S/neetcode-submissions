class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        j=k-1
        n=len(nums)
        mindiff=100001
        while j<n:
            mindiff=min(mindiff,(nums[j]-nums[j-k+1]))
            j+=1
        return mindiff


        
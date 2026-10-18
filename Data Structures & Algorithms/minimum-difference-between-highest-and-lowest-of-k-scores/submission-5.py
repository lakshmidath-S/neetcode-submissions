class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        j=k-1
        n=len(nums)
        mindiff=float("inf")
        while j<n:
            mindiff=min(mindiff,(nums[j]-nums[j-k+1]))
            j+=1
        return mindiff


        
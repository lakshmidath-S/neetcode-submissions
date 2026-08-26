class Solution:
    def jump(self, nums: List[int]) -> int:
        count=0
        i=0
        n=len(nums)
        while i<n-1:
            curmax=0
            if i+nums[i]>=n-1:
                return count+1
            for j in range(1,nums[i]+1):
                curidx=i+j
                curval=nums[curidx]
                futureidx=curidx+curval
                if futureidx>curmax:
                    curmax=futureidx
                    maxidx=curidx
                    if curmax>=n-1:
                        count+=2
                        return count
                j+=1
            i=maxidx
            count+=1
        return count
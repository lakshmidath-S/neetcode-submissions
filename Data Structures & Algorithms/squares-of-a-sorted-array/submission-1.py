class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[0]*n
        i,j=0,n-1
        for k in range(n-1,-1,-1):
            if abs(nums[i])>abs(nums[j]):
                result[k]=nums[i]**2
                i+=1
            else:
                result[k]=nums[j]**2
                j-=1
        return result
            

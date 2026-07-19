class Solution:
    def trap(self, height: List[int]) -> int:
        i,j=0,len(height)-1
        leftmax=height[i]
        rightmax=height[j]
        water=0
        while(i<=j):
            if rightmax<leftmax:
                if height[j]>rightmax:
                    rightmax=height[j]
                else:
                    water+=rightmax-height[j]
                j-=1
            else:
                if height[i]>leftmax:
                    leftmax=height[i]
                else:
                    water+=leftmax-height[i]
                i+=1
        return water
        

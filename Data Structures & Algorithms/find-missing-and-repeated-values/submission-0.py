class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        arr=[False]*(n*n)
        for i in grid:
            for j in i:
                if not arr[j-1]:
                    arr[j-1]=True
                else:
                    a=j
        for i in range(n*n):
            if arr[i]==False:
                b=i+1
        return [a,b]
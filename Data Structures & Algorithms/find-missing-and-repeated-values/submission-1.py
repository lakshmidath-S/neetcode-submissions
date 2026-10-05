class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        for i in range(n):
            for j in range(n):
                x=abs(grid[i][j])
                r=(x-1)//n
                c=(x-1)%n
                if grid[r][c]<0:
                    a=x
                else:
                    grid[r][c]=-grid[r][c]
        for i in range(n):
            for j in range(n):
                if grid[i][j]>0:
                    b=i*n+j+1
        return [a,b]
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea=0
        col=len(grid[0])
        row=len(grid)
        visited=[[False]*col for _ in range(row)]
        def dfs(i,j):
            if i==-1 or i==row or j==-1 or j==col:
                return 0
            if visited[i][j]:
                return 0
            if grid[i][j]==0:
                return 0
            visited[i][j]=True
            return (1+dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1))
            
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1 and not visited[i][j] :
                    area=dfs(i,j)
                    maxarea=max(maxarea,area)

        return maxarea
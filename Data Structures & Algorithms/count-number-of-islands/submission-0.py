class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(m,n):
            if m==-1 or n==-1 or m==row or n==col or visited[m][n]:
                return 
            if grid[m][n]=='1':
                visited[m][n]=True
                dfs(m+1,n)
                dfs(m-1,n)
                dfs(m,n+1)
                dfs(m,n-1)


        count=0
        row=len(grid)
        col=len(grid[0])
        visited=[[False]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if grid[i][j]=='1' and not visited[i][j]:
                    count+=1
                    dfs(i,j)
                else:
                    continue
        return count
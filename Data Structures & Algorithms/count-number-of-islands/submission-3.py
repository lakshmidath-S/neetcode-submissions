#bfs
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(m,n):
            queue = deque()
            visited[m][n]=True
            queue.append((m, n))
            while queue:
                r,c=queue.popleft()
                directions=[(1,0),(-1,0),(0,-1),(0,1)]
                for dr,dc in directions:
                    nr=r+dr
                    nc=c+dc
                    if 0<=nr<row and 0<=nc<col:
                        if grid[nr][nc]=='1' and not visited[nr][nc]:
                            visited[nr][nc]=True
                            queue.append((nr,nc))



        count=0
        row=len(grid)
        col=len(grid[0])
        visited=[[False]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if grid[i][j]=='1' and not visited[i][j]:
                    count+=1
                    bfs(i,j)
                else:
                    continue
        return count
from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        r=len(grid)
        c=len(grid[0])
        queue=deque()
        for i in range(r):
            for j in range(c):
                if grid[i][j]==0:
                    queue.append((i,j))
        direc=[(0,1),(0,-1),(1,0),(-1,0)]
        while queue:
            i,j=queue.popleft()
            for di,dj in direc:
                newi=i+di
                newj=j+dj
                if newi>=r or newj>=c or newi<0 or newj<0:
                    continue
                if grid[newi][newj]==-1:
                    continue
                if grid[newi][newj]!=2147483647:
                    continue
                grid[newi][newj]=grid[i][j]+1
                queue.append((newi,newj))
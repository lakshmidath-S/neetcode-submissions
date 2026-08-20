from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue=deque()
        fresh=0
        minutes=0
        r=len(grid)
        c=len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j]==2:
                    queue.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1

        directions=[(1,0),(-1,0),(0,1),(0,-1)]

        while queue and fresh>0:
            for _ in range(len(queue)):
                i,j=queue.popleft()
                for di,dj in directions:
                    ni=i+di
                    nj=j+dj
                    if 0<=ni<r and 0<=nj<c and grid[ni][nj]==1:
                        grid[ni][nj]=2
                        fresh-=1
                        queue.append((ni,nj))

            minutes+=1
        return minutes if fresh==0 else -1
            

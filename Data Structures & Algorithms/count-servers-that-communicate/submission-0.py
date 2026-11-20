class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows=[0]*len(grid)
        cols=[0]*len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    rows[i]+=1
                    cols[j]+=1 
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if((grid[i][j])and (rows[i]>1 or cols[j]>1)):
                    count+=1
        return count




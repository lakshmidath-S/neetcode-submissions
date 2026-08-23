class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r=len(heights)
        c=len(heights[0])
        preach=[[False]*c for _ in range(r)]
        areach=[[False]*c for _ in range(r)]
        p=[]
        a=[]
        directions=[(1,0),(0,1),(0,-1),(-1,0)]
        visited=[[False]*c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if i==0 or j==0:
                    p.append([i,j])
                if i==r-1 or j==c-1:
                    a.append([i,j])
        def preachable():
            while p:
                for _ in range(len(p)):
                    i,j=p.pop()
                    visited[i][j]=True
                    preach[i][j]=True
                    k=heights[i][j]
                    for di,dj in directions:
                        ni=di+i
                        nj=dj+j
                        if ni<0 or nj<0 or ni>=r or nj>=c:
                            continue
                        if visited[ni][nj]:
                            continue
                        if heights[ni][nj]>=k:
                            p.append([ni,nj])
                    
        preachable()
        visited=[[False]*c for _ in range(r)]
        def areachable():
            while a:
                for _ in range(len(a)):
                    i,j=a.pop()
                    visited[i][j]=True
                    areach[i][j]=True
                    k=heights[i][j]
                    for di,dj in directions:
                        ni=di+i
                        nj=dj+j
                        if ni<0 or nj<0 or ni>=r or nj>=c:
                            continue
                        if visited[ni][nj]:
                            continue
                        if heights[ni][nj]>=k:
                            a.append([ni,nj])
            
        areachable()
        ans=[]
        for i in range(r):
            for j in range(c):
                if areach[i][j] and preach[i][j]:
                    ans.append([i,j])
        return ans
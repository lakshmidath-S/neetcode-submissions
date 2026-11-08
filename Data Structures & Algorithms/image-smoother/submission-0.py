class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        dir=[(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
        n=len(img)
        m=len(img[0])
        result=[[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                val=img[i][j]
                count=1
                for p,q in dir:
                    inew=p+i
                    jnew=q+j
                    if 0<=inew<n and 0<=jnew<m:
                        count+=1
                        val+=img[inew][jnew]
                result[i][j]=val//count
        return result


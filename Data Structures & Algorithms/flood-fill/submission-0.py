from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        curr=image[sr][sc]
        visited=[[False]*len(image[0]) for _ in range(len(image))]
        que=deque([(sr,sc)])
        while que:
            a,b=que.popleft()
            if a<0 or b<0 or a>=len(image) or b>=len(image[0]):
                continue
            if not visited[a][b] and image[a][b]==curr:
                image[a][b]=color
                que.append([a,b+1])
                que.append([a+1,b])
                que.append([a-1,b])
                que.append([a,b-1])
            visited[a][b]=True
        return image

            


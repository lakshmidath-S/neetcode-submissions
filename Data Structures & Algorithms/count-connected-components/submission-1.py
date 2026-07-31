class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(i):
            if visited[i]==True:
                return 
            visited[i]=True
            for j in graph[i]:
                dfs(j)

        graph=[[]for _ in range (n)]
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        count=0
        visited=[False]*n
        for i in range(n):
            if visited[i]==False:
                count+=1
            for neighbor in graph[i]:
                if not visited[neighbor]:
                    dfs(neighbor)
        return count
        
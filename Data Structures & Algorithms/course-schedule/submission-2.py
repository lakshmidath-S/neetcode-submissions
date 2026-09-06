class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited=[0]*numCourses
        graph=[[] for _ in range(numCourses)]
        def dfs(node):
            if visited[node]==1:
                return False
            if visited[node]==2:
                return True
            visited[node]=1
            for j in graph[node]:
                if not dfs(j):
                    return False
            visited[node]=2
            return True
        for i,j in prerequisites:
            graph[j].append(i)
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

        
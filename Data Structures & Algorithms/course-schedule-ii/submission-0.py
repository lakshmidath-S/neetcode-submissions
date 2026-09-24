class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=[[]for _ in range(numCourses)]
        for u,v in prerequisites:
            graph[v].append(u)
        ans=[]
        state=[0]*numCourses
        def dfs(node):
            if state[node]==1:
                return False
            if state[node]==2:
                return True
            state[node]=1
            for next in graph[node]:
                if not dfs(next):
                    return False
            state[node]=2
            ans.append(node)
            return True
        for courses in range(numCourses):
            if not dfs(courses):
                return []
        return ans[::-1]
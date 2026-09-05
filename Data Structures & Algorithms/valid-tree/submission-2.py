class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
        visited=set()
        graph=[[]for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        dfs(0)

        return len(visited)==n
        
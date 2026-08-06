class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # Directed graph
        graph = [[] for _ in range(n)]

        # Undirected graph (used to propagate from safe methods)
        undirected = [[] for _ in range(n)]

        for u, v in invocations:
            graph[u].append(v)
            undirected[u].append(v)
            undirected[v].append(u)

        suspicious = [False] * n

        # DFS to mark all suspicious methods
        def dfs(node):
            suspicious[node] = True
            for nxt in graph[node]:
                if not suspicious[nxt]:
                    dfs(nxt)

        dfs(k)

        visited = [False] * n

        # DFS from non-suspicious methods
        # If a suspicious node is connected to a safe node,
        # it cannot be removed.
        def dfs2(node):
            visited[node] = True
            for nxt in undirected[node]:
                if not visited[nxt]:
                    suspicious[nxt] = False
                    dfs2(nxt)

        for i in range(n):
            if not suspicious[i] and not visited[i]:
                dfs2(i)

        ans = []
        for i in range(n):
            if not suspicious[i]:
                ans.append(i)

        return ans
class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        parent = list(range(c + 1))
        rank = [0] * (c + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[rb] < rank[ra]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1

        # build components
        for u, v in connections:
            union(u, v)

        # heaps for components
        import heapq
        heaps = {}
        for i in range(1, c + 1):
            r = find(i)
            if r not in heaps:
                heaps[r] = []
            heapq.heappush(heaps[r], i)

        online = [True] * (c + 1)
        ans = []

        for t, x in queries:
            if t == 2:
                online[x] = False
            else:  # t == 1
                if online[x]:
                    ans.append(x)
                else:
                    r = find(x)
                    h = heaps[r]
                    while h and not online[h[0]]:
                        heapq.heappop(h)
                    ans.append(h[0] if h else -1)

        return ans

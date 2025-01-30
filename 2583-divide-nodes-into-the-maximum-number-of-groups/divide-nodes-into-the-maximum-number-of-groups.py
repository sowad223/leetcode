from collections import defaultdict, deque
from math import inf

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        
        vis = [False] * (n + 1)
        ans = 0
        
        def dfs(i):
            arr.append(i)
            vis[i] = True
            for j in g[i]:
                if not vis[j]:
                    dfs(j)
        
        def bfs(i):
            dist = [inf] * (n + 1)
            dist[i] = 1
            q = deque([i])
            while q:
                i = q.popleft()
                for j in g[i]:
                    if dist[j] == inf:
                        dist[j] = dist[i] + 1
                        q.append(j)
            for i in arr:
                if dist[i] == inf:
                    dist[i] = dist[i - 1] + 1
            for i in arr:
                for j in g[i]:
                    if abs(dist[i] - dist[j]) != 1:
                        return -1
            return max(dist[i] for i in arr)
        
        for i in range(1, n + 1):
            if not vis[i]:
                arr = []
                dfs(i)
                t = max(bfs(v) for v in arr)
                if t == -1:
                    return -1
                ans += t
        return ans
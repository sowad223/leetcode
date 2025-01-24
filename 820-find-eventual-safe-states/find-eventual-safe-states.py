from typing import List
from collections import deque

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
       
        reverse_graph = [[] for _ in range(n)]
        out_degree = [0] * n
     
        for i in range(n):
            for neighbor in graph[i]:
                reverse_graph[neighbor].append(i)
            out_degree[i] = len(graph[i])
        
      
        queue = deque([i for i in range(n) if out_degree[i] == 0])
        safe = [False] * n  

        while queue:
            node = queue.popleft()
            safe[node] = True 
            for neighbor in reverse_graph[node]:
                out_degree[neighbor] -= 1
                if out_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return [i for i in range(n) if safe[i]]

        
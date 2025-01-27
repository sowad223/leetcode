from collections import defaultdict, deque
from typing import List

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        

        reachable = [[False] * numCourses for _ in range(numCourses)]
        for course in range(numCourses):
            queue = deque([course])
            while queue:
                current = queue.popleft()
                for neighbor in graph[current]:
                    if not reachable[course][neighbor]:
                        reachable[course][neighbor] = True
                        queue.append(neighbor)
        
  
        answer = []
        for u, v in queries:
            answer.append(reachable[u][v])
        
        return answer
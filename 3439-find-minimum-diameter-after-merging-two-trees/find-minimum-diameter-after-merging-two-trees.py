from collections import defaultdict, deque
from typing import List, Optional

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        # Helper to build adjacency list
        def build_adj_list(edges):
            adj = defaultdict(list)
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            return adj

        # BFS to find the farthest node and its distance
        def bfs(adj, start):
            visited = set()
            queue = deque([(start, 0)])  # (node, distance)
            farthest_node, max_distance = start, 0

            while queue:
                node, dist = queue.popleft()
                visited.add(node)

                if dist > max_distance:
                    farthest_node, max_distance = node, dist

                for neighbor in adj[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, dist + 1))

            return farthest_node, max_distance

        # Compute diameter and maximum height of the tree
        def compute_diameter_and_depth(edges):
            adj = build_adj_list(edges)
            # Start BFS from any node (e.g., node 0)
            farthest_node, _ = bfs(adj, 0)
            # Second BFS to find the diameter
            farthest_node, diameter = bfs(adj, farthest_node)
            # Max depth is half of the diameter (rounded up) for balanced trees
            return diameter, (diameter + 1) // 2

        # Compute D1, D2 (diameters) and H1, H2 (max depths)
        D1, H1 = compute_diameter_and_depth(edges1)
        D2, H2 = compute_diameter_and_depth(edges2)

        # The minimum possible diameter after merging
        return max(D1, D2, H1 + H2 + 1)

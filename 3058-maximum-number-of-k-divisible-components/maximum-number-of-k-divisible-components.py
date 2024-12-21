class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        tree = defaultdict(list)
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
        
        max_components = 0
        visited = [False] * n
        stack = [(0, -1)]
        subtree_sums = [0] * n
        
        while stack:
            node, parent = stack.pop()
            
            if not visited[node]:
                visited[node] = True
                stack.append((node, parent))
                for neighbor in tree[node]:
                    if neighbor != parent and not visited[neighbor]:
                        stack.append((neighbor, node))
            else:
                subtree_sum = values[node]
                for neighbor in tree[node]:
                    if neighbor != parent:
                        subtree_sum += subtree_sums[neighbor]
                
                if subtree_sum % k == 0:
                    max_components += 1
                    subtree_sum = 0
                
                subtree_sums[node] = subtree_sum

        return max_components
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        tree = defaultdict(list)
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
        
        
        max_components = 0

        
        def dfs(node, parent):
            nonlocal max_components
            subtree_sum = values[node]  

            for neighbor in tree[node]:
                if neighbor != parent:
                    child_sum = dfs(neighbor, node)
                    subtree_sum += child_sum

            
            if subtree_sum % k == 0:
                max_components += 1
                return 0  
            return subtree_sum

       
        dfs(0, -1)

        return max_components 


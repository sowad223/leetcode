class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parent = {} 
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x]) 
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return False  
            parent[rootX] = rootY  
            return True
        for u, v in edges:
            if u not in parent:
                parent[u] = u
            if v not in parent:
                parent[v] = v
            if not union(u, v):
                return [u, v]  
        
        return []


sol = Solution()
edges = [[1,2], [1,3], [2,3]]
print(sol.findRedundantConnection(edges))  
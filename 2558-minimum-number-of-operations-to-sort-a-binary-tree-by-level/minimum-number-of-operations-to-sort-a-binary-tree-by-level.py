from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def count_swaps_to_sort(arr):
            # Pair elements with their indices
            sorted_arr = sorted((val, idx) for idx, val in enumerate(arr))
            visited = [False] * len(arr)
            swaps = 0

            for i in range(len(arr)):
                if visited[i] or sorted_arr[i][1] == i:
                    continue

                # Count the size of the cycle
                cycle_size = 0
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = sorted_arr[j][1]
                    cycle_size += 1

                # If there's a cycle of size k, we need (k - 1) swaps
                if cycle_size > 1:
                    swaps += cycle_size - 1

            return swaps

        # BFS to collect levels
        levels = []
        queue = deque([(root, 0)])
        
        while queue:
            node, level = queue.popleft()
            if level == len(levels):
                levels.append([])
            levels[level].append(node.val)
            
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        # Count swaps for each level
        total_swaps = 0
        for level_vals in levels:
            total_swaps += count_swaps_to_sort(level_vals)

        return total_swaps

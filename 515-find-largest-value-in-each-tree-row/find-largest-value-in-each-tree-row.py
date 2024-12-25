from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        queue = deque([root])  # Use a queue for BFS
        
        while queue:
            level_size = len(queue)  # Number of nodes at the current level
            max_value = float('-inf')  # Initialize the max value for this level
            
            for _ in range(level_size):
                node = queue.popleft()
                max_value = max(max_value, node.val)  # Update the max value
                
                # Add child nodes to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(max_value)  # Store the largest value for this level
        
        return result

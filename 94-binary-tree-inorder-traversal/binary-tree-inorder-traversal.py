# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self._inorder(root, result)
        return result

    def _inorder(self, node: Optional[TreeNode], result: List[int]) -> None:
        if node is None:
            return
        self._inorder(node.left, result)  
        result.append(node.val)           
        self._inorder(node.right, result) 
        
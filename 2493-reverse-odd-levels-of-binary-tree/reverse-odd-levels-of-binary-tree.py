# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None


        queue = [root]
        level = 0

        while queue:
            level_size = len(queue)
            level_nodes = []

    
            for _ in range(level_size):
                node = queue.pop(0)
                level_nodes.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        
            if level % 2 == 1:
                i, j = 0, len(level_nodes) - 1
                while i < j:
                    level_nodes[i].val, level_nodes[j].val = level_nodes[j].val, level_nodes[i].val
                    i += 1
                    j -= 1

            level += 1 

        return root
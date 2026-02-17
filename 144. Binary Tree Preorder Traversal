# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Handle the empty tree case
        if not root:
            return []
        
        stack = [root]
        result = []
        
        while stack:
            # Pop the current node and visit it
            node = stack.pop()
            result.append(node.val)
            
            # Push right child first, so left child is popped first
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
        return result

class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node:
                return (0, None)  
            
            left_depth, left_subtree = dfs(node.left)
            right_depth, right_subtree = dfs(node.right)
            
            if left_depth > right_depth:
                return (left_depth + 1, left_subtree)
            elif right_depth > left_depth:
                return (right_depth + 1, right_subtree)
            else:
                return (left_depth + 1, node)
        
        return dfs(root)[1]

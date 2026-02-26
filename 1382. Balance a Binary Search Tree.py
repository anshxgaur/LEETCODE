# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Step 1: Inorder traversal to get sorted values
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        values = inorder(root)
        
        # Step 2: Build balanced BST from sorted values
        def buildBalancedBST(nums, left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = buildBalancedBST(nums, left, mid - 1)
            node.right = buildBalancedBST(nums, mid + 1, right)
            return node
        
        return buildBalancedBST(values, 0, len(values) - 1)

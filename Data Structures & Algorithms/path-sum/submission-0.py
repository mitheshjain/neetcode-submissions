# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        globalFlag=False

        def dfs(node,sum):
            if not node:
                return False
            nonlocal globalFlag
            print (sum)
            if not node.left and not node.right:
                if sum+node.val == targetSum:
                    globalFlag=True
            if globalFlag:
                return
            else:
                dfs(node.left,sum+node.val)
                dfs(node.right,sum+node.val)
        dfs(root,0)
        return globalFlag

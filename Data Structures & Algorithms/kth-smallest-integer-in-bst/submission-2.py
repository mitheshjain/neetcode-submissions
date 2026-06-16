# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res=root.val
        cnt=k
        def find(node,index):
            nonlocal cnt,res
            if not node:
                return
            find(node.left,index)
            cnt-=1
            if cnt==0:
                res=node.val
                return
            find(node.right,index)
        find(root,0)
        return res


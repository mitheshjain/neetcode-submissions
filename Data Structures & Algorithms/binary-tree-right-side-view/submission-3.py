class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            level_size = len(q)

            for i in range(level_size):
                node = q.popleft()

                if i==0:
                    res.append(node.val)
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)

        return res
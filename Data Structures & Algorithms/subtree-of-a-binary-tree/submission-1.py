class Solution:
    def isSubtree(self, root, subRoot):
        # 1. A null subRoot is technically a subtree of any tree
        if not subRoot: 
            return True
        
        # 2. If the main tree is null but subRoot isn't, it's impossible
        if not root: 
            return False
        
        # 3. If the trees starting at these nodes are identical, we found it!
        if self.isSameTree(root, subRoot):
            return True
        
        # 4. Otherwise, check the left and right children of the main tree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p, q):
        # Helper function from our previous problem
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False
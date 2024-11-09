# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        result=[]
        res=[]
        def dfs_p(node):
            if node is None:
                return
            
            result.append(node.val)

            dfs_p(node.left)
            dfs_p(node.right)
        dfs_p(p)
        def dfs_q(node):
            if node is None:
                return
            res.append(node.val)

            dfs_q(node.left)
            dfs_q(node.right)
        dfs_q(q)
        if res==result:
            return True
        else:
            return False
        
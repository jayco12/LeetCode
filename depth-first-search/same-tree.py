# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node, result):
            if node is None:
                result.append(None)
                return
            result.append(node.val)
            dfs(node.left, result)
            dfs(node.right, result)
    
        result_p, result_q = [], []
        dfs(p, result_p)
        dfs(q, result_q)
        
        return result_p == result_q
        
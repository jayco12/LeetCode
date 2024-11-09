# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return

        queue = [root]
        is_last_level = False

        while queue:
            node = queue.pop(0)

            if is_last_level:
                # If we're on the last level, all nodes should be leaf nodes
                if node.left or node.right:
                    return False
            else:
                # If we're not on the last level, nodes should have two children
                if node.left is None or node.right is None:
                    is_last_level = True

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return True
        
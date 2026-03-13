# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        from collections import deque

        q = deque([(root, targetSum - root.val)])

        while q:
            # pop the first item
            node, currentTargetValue = q.popleft()

            # condition check
            if not node.left and not node.right and currentTargetValue == 0:
                return True
            
            # update the queue values
            # starting the left
            if node.left:
                q.append((node.left, currentTargetValue - node.left.val))
            if node.right:
                q.append((node.right, currentTargetValue - node.right.val))

        return False

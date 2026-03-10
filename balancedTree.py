# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def check_balanced(node):
            if not node:
                return 0

            left = check_balanced(node.left)
            if left == -1: return -1

            right = check_balanced(node.right)
            if right == -1: return -1

            if abs(left - right) > 1: 
                return -1
            
            return 1 + max(left, right)

            '''
            this code check for the balance health of the tree
            1. using recursive code to start from the bottom up. 
            2. left and right check height
            3. return -1 when left and right have difference greater than 1
            4. null node = 0
            '''
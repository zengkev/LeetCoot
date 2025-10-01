'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false
 
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if not root.left and not root.right:
            return True
                
        return self.isSame(root.left, root.right)
    
    # Split the tree into two
    def isSame(self, s1: [TreeNode], s2: [TreeNode]) -> bool:

        if not s1 and not s2:
            return True
        
        if not s1 or not s2 or s1.val != s2.val:
            return False
        
        return self.isSame(s1.left, s2.right) and self.isSame(s1.right, s2.left)
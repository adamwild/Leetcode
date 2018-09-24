# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root == None:
            return TreeNode(val)
        
        curr_node = root
        while curr_node is not None:
            if val> curr_node.val:
                prev_node = curr_node
                curr_node = curr_node.right
                flag = False
            else:
                prev_node = curr_node
                curr_node = curr_node.left
                flag = True
        if flag:
            prev_node.left = TreeNode(val)
        else:
            prev_node.right = TreeNode(val)
            
        return root

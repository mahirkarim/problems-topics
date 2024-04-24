# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        difference = self.checkNode(root, root.val)
        node_queue = [root.left, root.right]

        for node in node_queue:
            try:
                temp_difference = self.checkNode(node, node.val)
                if temp_difference < difference:
                    difference = temp_difference
            except:
                continue
            node_queue.append(node.left)
            node_queue.append(node.right)
            
        return difference
    
    # return closest values from left and right for a given node 
    # traverse to rightmost value on left branch and leftmost value on right branch
    # either make this recursive or call it in a loop in the main function
    def checkNode(self, node, root_val):
        left = node.left
        left_val = None
        while left:
            left_val = left.val
            left = left.right

        right = node.right
        right_val = None
        while right:
            right_val = right.val
            right = right.left

        if left_val:
            left_val = abs(root_val - left_val)
        else:
            left_val = right_val
        
        if right_val:
            right_val = abs(root_val - right_val)
        else:
            right_val = left_val
        
        try:
            return min(left_val, right_val)
        except:
            return None
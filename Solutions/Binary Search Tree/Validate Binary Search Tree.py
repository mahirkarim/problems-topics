import sys
import TreeNode

class Solution:
    def isValidBST(self, root) -> bool:
        node_list = [(root, root.val)]
        ans = True
        while node_list:
            node = node_list.pop(0)
            parent = node(1)
            node = node(0)
            left = node.left
            right = node.right
            
            if left:
                node_list.append((left, node.val))
                x = left.val
                if x < parent:
                    ans = False
                    break
            else:
                x = node.val - 1
            if right:
                node_list.append((right, node.val))
                y = right.val 
                if y > parent:
                    ans = False
                    break
            else:
                y = node.val + 1

            if node.val <= x or node.val >= y:
                ans = False
                break
            
        return ans
    

if __name__ == '__main__':
    x = Solution()
    print(x.isValidBST(sys.argv[1]))
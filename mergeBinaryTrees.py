# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def mergeTrees(self, root1, root2):
        if not root1 and not root2:
            return None
        elif not root1:
            return root2
        elif not root2:
            return root1
        
        mergedRoot = TreeNode(root1.val + root2.val)
        mergedRoot.left = self.mergeTrees(root1.left, root2.left)
        mergedRoot.right = self.mergeTrees(root1.right, root2.right)
        return mergedRoot



# def printTree(node, level=0, label="Root:"):
#     """Utility function to print the tree level by level"""
#     if node is not None:
#         print(" " * (level * 4) + label, node.val)
#         printTree(node.left, level + 1, label="L---")
#         printTree(node.right, level + 1, label="R---")

# def main():
#     # Creating tree 1
#     tree1 = TreeNode(1)
#     tree1.left = TreeNode(3, TreeNode(5))
#     tree1.right = TreeNode(2)

#     # Creating tree 2
#     tree2 = TreeNode(2)
#     tree2.left = TreeNode(1, None, TreeNode(4))
#     tree2.right = TreeNode(3, None, TreeNode(7))

#     # Instantiate the Solution class
#     solution = Solution()
    
#     # Merge the trees
#     mergedTree = solution.mergeTrees(tree1, tree2)
    
#     # Print the merged tree
#     print("Merged Tree:")
#     printTree(mergedTree)

# if __name__ == "__main__":
#     main()
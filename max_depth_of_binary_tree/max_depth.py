class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth =  self.exploreNode(root, 0)
        return max_depth

    def exploreNode(self, node: TreeNode, depth: int) -> int:
        if node == None:
            return depth

        depth += 1
        left_depth = self.exploreNode(node.left, depth)
        right_depth = self.exploreNode(node.right, depth)
        return max(left_depth, right_depth) 

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(val=9)
    right = TreeNode(val=20)
    right.left = TreeNode(val=15)
    right.right = TreeNode(val=7)
    root.right = right

    sol = Solution()
    result = sol.maxDepth(root)
    print(result)

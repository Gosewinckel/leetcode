from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == []:
            return []
        explore = deque()
        explore.append(root)
        results = []
        while len(explore) > 0:
            nums = []
            queue = explore.copy()
            for node in queue:
                if node == None:
                    explore.popleft()
                    continue
                nums.append(node.val)
                explore.append(node.left)
                explore.append(node.right)
                explore.popleft()
            if nums == []:
                continue
            results.append(nums)
        return results
                

if __name__ == "__main__":
    root = []
    #root.left = TreeNode(val=9)
    #right = TreeNode(val=20)
    #right.left = TreeNode(val=15)
    #right.right = TreeNode(val=7)
    #root.right = right

    sol = Solution()
    result = sol.levelOrder(root)
    print(result)

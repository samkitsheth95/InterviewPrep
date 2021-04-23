# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        maxScore = 0

        def dfs(curr):
            nonlocal maxScore
            if not curr:
                return (0, 0)

            leftSum, leftCount = dfs(curr.left)
            rightSum, rightCount = dfs(curr.right)

            totalSum = curr.val + leftSum + rightSum
            totalCount = 1 + leftCount + rightCount

            maxScore = max(maxScore, totalSum / totalCount)

            return (totalSum, totalCount)

        ans = dfs(root)
        return maxScore

    def maximumAverageSubtree(self, root: TreeNode) -> float:
        def dfs(curr):
            if not curr:
                return (0, 0, 0)

            leftSum, leftCount, leftMax = dfs(curr.left)
            rightSum, rightCount, rightMax = dfs(curr.right)

            totalSum = curr.val + leftSum + rightSum
            totalCount = 1 + leftCount + rightCount

            maxOfThree = max(leftMax, rightMax, totalSum / totalCount)

            return (totalSum, totalCount, maxOfThree)

        ans = dfs(root)
        return ans[2]

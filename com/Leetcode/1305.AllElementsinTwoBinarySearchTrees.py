# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def getInorderTraversal(self, root: TreeNode):
        listI = []
        stack = []
        current = root
        while True:
            if current:
                stack.append(current)
                current = current.left
            else:
                if not stack:
                    break
                current = stack.pop()
                listI.append(current.val)
                current = current.right
        return listI

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        list1 = self.getInorderTraversal(root1)
        list2 = self.getInorderTraversal(root2)
        print(list1, list2)
        i = 0
        j = 0
        ans = []
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                ans.append(list1[i])
                i += 1
            else:
                ans.append(list2[j])
                j += 1
        while j < len(list2):
            ans.append(list2[j])
            j += 1
        while i < len(list1):
            ans.append(list1[i])
            i += 1
        return ans

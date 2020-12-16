class Solution:
    def isMatching(self, left, right):
        if left == '{' and right == '}':
            return True
        elif left == '(' and right == ')':
            return True
        elif left == '[' and right == ']':
            return True
        return False

    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i in '({[':
                stack.append(i)
            else:
                if not stack or not self.isMatching(stack.pop(), i):
                    return False
        return True if not stack else False


sol = Solution()
print(sol.isValid(s="()[]{}"))

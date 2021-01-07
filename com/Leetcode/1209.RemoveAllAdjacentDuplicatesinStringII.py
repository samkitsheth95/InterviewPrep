class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack, ans = [], ''
        for i in s:
            if stack and stack[-1][0] == i:
                char, value = stack.pop()
                if value + 1 != k:
                    stack.append((char, value + 1))
            else:
                stack.append((i, 1))
        for char, value in stack:
            ans += char * value
        return ans


sol = Solution()
print(sol.removeDuplicates(s="pbbcggttciiippooaais", k=2))

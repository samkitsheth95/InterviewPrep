class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack, i = [], 0

        while i < len(num):
            if not stack:
                if num[i] != "0":
                    stack.append(num[i])
            elif stack[-1] <= num[i]:
                stack.append(num[i])
            else:
                while stack and stack[-1] > num[i] and k > 0:
                    stack.pop()
                    k -= 1
                if not stack and num[i] == "0":
                    continue
                stack.append(num[i])
            i += 1

        while stack and k > 0:
            stack.pop()
            k -= 1

        return ''.join(stack) if stack else "0"

    def removeKdigitsLeetcode(self, num: str, k: int) -> str:
        stack = []

        for i in num:
            while stack and k > 0 and stack[-1] > i:
                stack.pop()
                k -= 1
            stack.append(i)

        while stack and k > 0:
            stack.pop()
            k -= 1

        while stack and stack[0] == "0":
            stack.pop(0)

        return ''.join(stack) if stack else "0"


sol = Solution()
print(sol.removeKdigitsLeetcode(num="1432219", k=3))

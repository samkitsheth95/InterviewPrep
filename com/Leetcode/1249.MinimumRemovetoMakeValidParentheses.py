class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        ans = list(s)
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if not stack:
                    ans[i] = ''
                else:
                    stack.pop()
        for i in stack:
            ans[i] = ''
        return ''.join(ans)

    def minRemoveToMakeValidTwoPass(self, s: str) -> str:
        stack = []
        ans = list(s)
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if not stack:
                    ans[i] = ''
                else:
                    stack.pop()
        for i in stack:
            ans[i] = ''
        return ''.join(ans)


sol = Solution()
print(sol.minRemoveToMakeValidTwoPass("lee(t(c)o)de)"))

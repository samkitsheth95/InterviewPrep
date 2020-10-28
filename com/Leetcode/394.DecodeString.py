from collections import deque


class Solution:

    def decodeStringStack(self, s: str) -> str:
        num, stack, ans = 0, [], ''
        for i in range(len(s)):
            current = s[i]
            if current == '[':
                stack.append([ans, num])
                num = 0
                ans = ''
            elif current == ']':
                temp = stack.pop()
                ans = temp[0] + temp[1] * ans
            elif current.isdigit():
                num = num * 10 + ord(current) - ord('0')
            else:
                ans += current
        return ans

    def decodeStringQueueRecursion(self, s: str) -> str:
        q = deque()
        for i in s:
            q.append(i)
        return self.dfs(q)

    def dfs(self, q):
        s = ""
        while q:
            current = q.popleft()
            if current.isdigit():
                temp = 0
                while current != '[':
                    temp = temp * 10 + ord(current) - ord('0')
                    current = q.popleft()
                s += int(temp) * self.dfs(q)
            elif current == ']':
                return s
            else:
                s += current
        return s

    def decodeStringRecursion(self, s: str) -> str:
        n = len(s)
        return self.dfs(s, 0, n)[0]

    def dfs(self, s, i, n):
        ans = ""
        while i < n:
            current = s[i]
            if current.isdigit():
                temp = 0
                while current != '[':
                    temp = temp * 10 + ord(current) - ord('0')
                    i += 1
                    current = s[i]
                tup = self.dfs(s, i + 1, n)
                ans += (temp * tup[0])
                i = tup[1]
            elif current == ']':
                return (ans, i)
            else:
                ans += current
            i += 1
        return (ans, i)


sol = Solution()
print(sol.decodeStringRecursion(s="30[a]2[bc]"))

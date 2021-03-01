class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        lookUp, ans = set(jewels), 0
        for c in stones:
            if c in lookUp:
                ans += 1
        return ans


sol = Solution()
print(sol.numJewelsInStones(jewels="aA", stones="aAAbbbb"))

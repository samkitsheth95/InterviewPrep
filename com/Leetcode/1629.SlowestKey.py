from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        longestTime, key, prev = 0, '@', 0
        for i in range(len(releaseTimes)):
            pressDuration = releaseTimes[i] - prev
            if longestTime < pressDuration:
                longestTime = pressDuration
                key = keysPressed[i]
            elif longestTime == pressDuration:
                key = max(key, keysPressed[i])
            prev = releaseTimes[i]
        return key


sol = Solution()
print(sol.slowestKey(releaseTimes=[9, 29, 49, 50], keysPressed="cbcd"))

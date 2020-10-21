from typing import List


class Solution:

    def getMaxLenOne(self, nums: List[int]) -> int:
        numNeg, maxLen = 0, 0
        firstNeg, zeroPos = -1, -1
        for i in range(len(nums)):
            if nums[i] < 0:
                numNeg += 1
                if firstNeg == -1:
                    firstNeg = i
            elif nums[i] == 0:
                numNeg, firstNeg = 0, -1
                zeroPos = i
            if not numNeg % 2:
                maxLen = max(maxLen, i - zeroPos)
            else:
                maxLen = max(maxLen, i - firstNeg)
        return maxLen

    def getMaxLen(self, nums: List[int]) -> int:
        maxLen = 0
        negP = [0, 0]
        posP = [0, 0]
        for i in range(len(nums)):
            if nums[i] > 0:
                posP[0] += 1
                if sum(negP):
                    negP[0] += 1
            elif nums[i] < 0:
                negP, posP = posP, negP
                negP[1] += 1
                if sum(posP):
                    posP[0] += 1
            else:
                negP, posP = [0, 0], [0, 0]
            maxLen = max(maxLen, sum(posP))
        return maxLen


sol = Solution()
print(sol.getMaxLenOne(nums=[1, -2, -3, 4]))

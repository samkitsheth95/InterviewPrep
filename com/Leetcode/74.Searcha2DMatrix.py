from typing import List


class Solution:
    def binarySearch(self, a, low, high, target):
        while low <= high:
            mid = (low + high) // 2
            if a[mid] == target:
                return True
            elif a[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) < 1 or len(matrix[0]) < 1:
            return False
        lowC, lowR = 0, 0
        highC, highR = len(matrix[0]) - 1, len(matrix) - 1
        while lowR <= highR:
            midC = (lowC + highC) // 2
            midR = (lowR + highR) // 2
            if matrix[midR][midC] == target:
                return True
            elif matrix[midR][midC] < target:
                if matrix[midR][-1] >= target:
                    return self.binarySearch(matrix[midR], midC, len(matrix[midR]) - 1, target)
                else:
                    if midC + 1 <= len(matrix[0]) - 1 and midR + 1 <= len(matrix) - 1:
                        lowC = midC + 1
                        lowR = midR + 1
                    elif midC + 1 <= len(matrix[0]) - 1:
                        lowC = midC + 1
                    elif midR + 1 <= len(matrix) - 1:
                        lowR = midR + 1
                    else:
                        return False
            else:
                if matrix[midR][0] <= target:
                    return self.binarySearch(matrix[midR], 0, midC - 1, target)
                else:
                    if midC - 1 >= 0 and midR - 1 >= 0:
                        highC = midC - 1
                        highR = midR - 1
                    elif midC - 1 >= 0:
                        highC = midC - 1
                    elif midR - 1 >= 0:
                        highR = midR - 1
                    else:
                        return False
        return False

    def searchMatrixClever(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1
        while low <= high:
            mid = (low + high) // 2
            num = matrix[mid // cols][mid % cols]
            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
        return False


sol = Solution()
print(sol.searchMatrixClever(
    [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 5))

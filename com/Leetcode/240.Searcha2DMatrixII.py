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

    def searchMatrixNaive(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        n = len(matrix[0]) - 1
        for i in matrix:
            if self.binarySearch(i, 0, n, target):
                return True
        return False

    def searchMatrixBetter(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        row = m - 1
        col = 0
        while row >= 0 and col < n:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                row -= 1
            else:
                col += 1
        return False


sol = Solution()
print(sol.searchMatrixBetter([
    [1,   4,  7, 11, 15],
    [2,   5,  8, 12, 19],
    [3,   6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
], 4
))

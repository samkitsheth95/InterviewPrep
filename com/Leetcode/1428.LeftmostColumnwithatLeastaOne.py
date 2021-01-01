class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:        
        rows, cols = binaryMatrix.dimensions()
        currRow, currCol = 0, cols - 1
        while currRow < rows and currCol >= 0:
            if binaryMatrix.get(currRow, currCol):
                currCol -= 1
            else:
                currRow += 1
        
        return currCol + 1 if currCol != cols-1 else -1
    
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        row, cols = binaryMatrix.dimensions()
        low, high = 0, cols - 1
        gans = 102
        for i in range(row):
            low = 0
            high = cols - 1
            ans = cols
            while low <= high:
                mid = low + (high - low) // 2
                if binaryMatrix.get(i,mid):
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            if ans != cols:
                gans = min(gans, ans)
                if not gans:
                    break
        return -1 if gans == 102 else gans
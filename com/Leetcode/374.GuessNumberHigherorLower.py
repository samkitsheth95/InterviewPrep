# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 0
        high = n

        while low <= high:
            mid = low + (high - low) // 2
            temp = guess(mid)
            if not temp:
                return mid
            elif temp == 1:
                low = mid + 1
            else:
                high = mid - 1

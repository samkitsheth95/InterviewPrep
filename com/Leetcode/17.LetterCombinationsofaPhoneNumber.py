from typing import List


class Solution:

    def letterCombinationsIterative(self, digits: str) -> List[str]:
        allCombination = [''] if digits else []
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        for digit in digits:
            currentCombination = []
            for letter in mapping[digit]:
                for combination in allCombination:
                    currentCombination.append(combination + letter)
            allCombination = currentCombination
        return allCombination

    def letterCombinationsRecursive(self, digits: str) -> List[str]:
        if not digits:
            return []
        allCombination = []
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def helper(i, combination):
            if i == len(digits):
                allCombination.append(combination)
            else:
                for letter in mapping[combination[i]]:
                    helper(i + 1, combination[:i] +
                           letter + combination[i + 1:])
        helper(0, digits)
        return allCombination


sol = Solution()
print(sol.letterCombinationsRecursive("23"))

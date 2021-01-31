"""
Why dose this Solution Work?

The Fisher-Yates algorithm is remarkably similar to the brute force 
solution. On each iteration of the algorithm, we generate a random 
integer between the current index and the last index of the array. 
Then, we swap the elements at the current index and the chosen index
this simulates drawing (and removing) the element from the hat, as 
the next range from which we select a random index will not include 
the most recently processed one. One small, yet important detail is 
that it is possible to swap an element with itself - otherwise, 
some array permutations would be more likely than others.

"""


class Solution:

    def __init__(self, nums: List[int]):
        self.original = list(nums)
        self.array = nums
        self.n = len(nums)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(self.n):
            idx = randint(i, self.n - 1)
            self.array[i], self.array[idx] = self.array[idx], self.array[i]
        return self.array


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

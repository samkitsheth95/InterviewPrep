class Solution:

    def subsetsIterativeOne(self, nums: List[int]) -> List[List[int]]:
        subset = [[]]
        for val in nums:
            currentSubset = []
            for j in subset:
                newj = j[:]
                newj.append(val)
                currentSubset.append(newj)
            subset.extend(currentSubset)
        return subset

    def subsetsRecursiveOne(self, nums: List[int], idx=None) -> List[List[int]]:
        if idx is None:
            idx = len(nums) - 1
        if idx < 0:
            return [[]]
        subset = self.subsets(nums, idx - 1)
        currentSubset = []
        for i in subset:
            j = i[:]
            j.append(nums[idx])
            currentSubset.append(j)
        subset.extend(currentSubset)
        return subset

    def subsetsIterativeTwo(self, nums: List[int]) -> List[List[int]]:
        subset = [[]]
        for val in nums:
            for i in range(len(subset)):
                currentSubset = subset[i]
                subset.append(currentSubset + [val])
        return subset

    def subsetsRecursiveTwo(self, nums: List[int], idx=None) -> List[List[int]]:
        if idx is None:
            idx = len(nums) - 1
        if idx < 0:
            return [[]]
        subset = self.subsets(nums, idx - 1)
        for i in range(len(subset)):
            currentSubset = subset[i]
            subset.append(currentSubset + [nums[idx]])
        return subset

from typing import List
import itertools

class Solution:

    def compareVersion(self, version1: str, version2: str) -> int:
        version1list = list(map(int,version1.split(".")))
        version2list = list(map(int,version2.split(".")))
        for i  in range(min(len(version1list),len(version2list))):
            if version1list[i] > version2list[i]:
                return 1
            if version1list[i] < version2list[i]:
                return -1
        if len(version1list) > len(version2list):
            for i in range(len(version1list) - 1,len(version1list)- (len(version1list)-len(version2list)) - 1,-1):
                if version1list[i] != 0:
                    return 1;
        elif len(version1list) < len(version2list):
            for i in range(len(version2list) - 1,len(version2list)- (len(version2list)-len(version1list)) - 1,-1):
                if version2list[i] != 0:
                    return -1;
        return 0

    def compareVersionOne(self, version1: str, version2: str) -> int:
        nums1 = version1.split('.')
        nums2 = version2.split('.')
        n1, n2 = len(nums1), len(nums2)
        
        # compare versions
        for i in range(max(n1, n2)):
            i1 = int(nums1[i]) if i < n1 else 0
            i2 = int(nums2[i]) if i < n2 else 0
            if i1 != i2:
                return 1 if i1 > i2 else -1
        
        # the versions are equal
        return 0
        
    def get_next_chunk(self, version: str, n: int, p: int) -> List[int]:
        # if pointer is set to the end of string
        # return 0
        if p > n - 1:
            return 0, p
        
        # find the end of chunk
        p_end = p
        while p_end < n and version[p_end] != '.':
            p_end += 1
        # retrieve the chunk
        i = int(version[p:p_end]) if p_end != n - 1 else int(version[p:n])
        # find the beginning of next chunk
        p = p_end + 1
        
        return i, p
        
    def compareVersionSpaceOptimized(self, version1: str, version2: str) -> int:
        p1 = p2 = 0
        n1, n2 = len(version1), len(version2)
        
        # compare versions
        while p1 < n1 or p2 < n2:
            i1, p1 = self.get_next_chunk(version1, n1, p1)
            i2, p2 = self.get_next_chunk(version2, n2, p2)            
            if i1 != i2:
                return 1 if i1 > i2 else -1
        
        # the versions are equal
        return 0
    
    def compareVersion(v1, v2):
        v1, v2 = map(int, v1.split('.')), map(int, v2.split('.'))
        v1, v2 = zip(*itertools.zip_longest(v1, v2, fillvalue = 0))
        return (0, 1, -1)[(v1 > v2) - (v1 < v2)]

sol = Solution()
print(sol.compareVersionSpaceOptimized("1","1.1"))

from collections import Counter


class Solution:

    def minWindowOrdHashing(self, s: str, t: str) -> str:
        tCount = [0] * 128
        start, end, count = 0, 0, 0
        ans = (float('inf'), [0, 0])
        for i in t:
            tCount[ord(i)] += 1
        
        while end < len(s):
            if tCount[ord(s[end])] > 0:
                count += 1
            tCount[ord(s[end])] -= 1
            
            if count == len(t):
                while start <= end and tCount[ord(s[start])] < 0:
                    tCount[ord(s[start])] += 1
                    start += 1
                if ans[0] >= end - start + 1:
                    ans = (end - start + 1, [start, end])
                tCount[ord(s[start])] += 1
                start += 1
                count -= 1
            end += 1
        return "" if ans[0] == float('inf') else s[ans[1][0]:ans[1][1] + 1]
    
    def minWindow(self, s: str, t: str) -> str:
        tCount = Counter(t)
        start, end, count = 0, 0, 0
        ans = (float('inf'), [0, 0])
        while end < len(s):
            if s[end] in tCount and tCount[s[end]] > 0:
                tCount[s[end]] -= 1
                count += 1
            else:
                if s[end] in tCount:
                    tCount[s[end]] -= 1
                else:
                    tCount[s[end]] = -1
            if count == len(t):
                while start <= end and tCount[s[start]] < 0:
                    tCount[s[start]] += 1
                    start += 1
                if ans[0] >= end - start + 1:
                    ans = (end - start + 1, [start, end])
                tCount[s[start]] += 1
                start += 1
                count -= 1
            end += 1
        return "" if ans[0] == float('inf') else s[ans[1][0]:ans[1][1] + 1]
    
    def isValid(self, arr, locations):
        temp = 0
        for i in arr.keys():
            if i in locations and locations[i] >= arr[i]:
                temp += 1
        return True if temp == len(arr) else False
    
    def minWindowNaive(self, s: str, t: str) -> str:
        arr = Counter(t)
        locations = {}
        start, end = 0, 0
        ans = (50000001, [0, 0])
        while end < len(s):
            if s[end] in locations:
                locations[s[end]] += 1
            else:
                locations[s[end]] = 1
            while self.isValid(arr, locations):
                if ans[0] >= end - start + 1:
                    ans = (end - start + 1, [start, end])
                locations[s[start]] -= 1
                start += 1
            end += 1
        return "" if ans[0] == 50000001 else s[ans[1][0]:ans[1][1] + 1]


sol = Solution()
print(sol.minWindowOrdHashing(s="ADOBECODEBANC", t="ABC"))

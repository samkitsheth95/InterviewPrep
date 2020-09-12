from collections import Counter
from typing import List

def wordSubsets(A: List[str], B: List[str]) -> List[str]:
    minFreq = {}
    for word in B:
        freq = Counter(word)
        for key, value in freq.items():
            if key in minFreq:
                if value > minFreq[key]:
                    minFreq[key] = value
            else:
                minFreq[key] = value
    ans = []
    for word in A:
        c = minFreq.copy()
        flag = True
        for i in range(len(word)):
            if word[i] in c:
                c[word[i]] -= 1
        for value in c.values():
            if value > 0:
                flag = False
                break
        if flag:
            ans.append(word)
    return ans
    
print(wordSubsets(["amazon","apple","facebook","google","leetcode"],["e","o"]))
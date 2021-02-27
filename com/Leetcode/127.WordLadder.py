from typing import List
from collections import defaultdict, deque


class Solution:

    def preMadeWords(self, wordListSet):
        ans = defaultdict(list)
        for word in wordListSet:
            for i in range(len(word)):
                ans[word[:i] + '_' + word[i+1:]].append(word)
        return ans

    def ladderLengthAllCombination(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        level, depth, q, usedWord = 0, 0, deque(), set()
        wordList.append(beginWord)
        madeWords = self.preMadeWords(wordList)
        q.append(beginWord)
        usedWord.add(beginWord)
        while q:
            depth += 1
            lvl = len(q)
            while lvl:
                currentWord = q.popleft()
                for i in range(len(currentWord)):
                    matchingList = madeWords[currentWord[:i] +
                                             '_' + currentWord[i+1:]]
                    for word in matchingList:
                        if word not in usedWord:
                            q.append(word)
                            usedWord.add(word)
                            if word == endWord:
                                return depth + 1
                    matchingList = []
                lvl -= 1
        return 0

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordListSet = set(wordList)
        if endWord not in wordListSet:
            return 0
        lvl, depth, q = 0, 0, deque()
        q.append(beginWord)
        while q:
            depth += 1
            lvl = len(q)
            while lvl:
                currentWord = list(q.popleft())
                for i in range(len(currentWord)):
                    temp = currentWord[i]
                    for j in range(26):
                        currentWord[i] = chr(ord('a') + j)
                        formedWord = ''.join(currentWord)
                        if formedWord in wordListSet:
                            q.append(formedWord)
                            wordListSet.remove(formedWord)
                            if formedWord == endWord:
                                return depth + 1
                    currentWord[i] = temp
                lvl -= 1
        return 0


sol = Solution()
print(sol.ladderLengthAllCombination(beginWord="hit", endWord="cog",
                                     wordList=["hot", "dot", "dog", "lot", "log", "cog"]))

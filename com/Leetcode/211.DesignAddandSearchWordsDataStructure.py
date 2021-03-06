##############
# using Trie
##############

class Node:

    def __init__(self):
        self.child = {}
        self.end = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for i in word:
            if i not in curr.child:
                curr.child[i] = Node()
            curr = curr.child[i]
        curr.end = True

    def search(self, word: str) -> bool:
        return self.dfs(word, self.root)

    def dfs(self, word: str, curr) -> bool:
        for i in range(len(word)):
            if word[i] == '.':
                for nodes in curr.child.values():
                    if self.dfs(word[i + 1:], nodes):
                        return True
                return False
            else:
                if word[i] not in curr.child:
                    return False
                curr = curr.child[word[i]]
        return curr.end

########################
# using hashmap and set
########################


class Node:

    def __init__(self):
        self.child = {}
        self.end = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = defaultdict(set)

    def addWord(self, word: str) -> None:
        self.data[len(word)].add(word)

    def search(self, word: str) -> bool:
        n = len(word)
        for sameLenWords in self.data[n]:
            i = 0
            while i < n and (word[i] == sameLenWords[i] or word[i] == '.'):
                i += 1
            if i == n:
                return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

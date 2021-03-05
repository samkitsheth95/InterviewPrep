##############
# USING Array
##############
class Node:

    def __init__(self):
        self.end = False
        self.child = [0] * 26


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for i in word:
            if not curr.child[ord(i) - ord('a')]:
                curr.child[ord(i) - ord('a')] = Node()
            curr = curr.child[ord(i) - ord('a')]
        curr.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for i in word:
            if not curr.child[ord(i) - ord('a')]:
                return False
            curr = curr.child[ord(i) - ord('a')]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for i in prefix:
            if not curr.child[ord(i) - ord('a')]:
                return False
            curr = curr.child[ord(i) - ord('a')]
        return True

##############
# USING DICT
##############


class Node:

    def __init__(self):
        self.end = False
        self.child = {}


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for i in word:
            if i not in curr.child:
                curr.child[i] = Node()
            curr = curr.child[i]
        curr.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for i in word:
            if i not in curr.child:
                return False
            curr = curr.child[i]
        return True if curr.end else False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for i in prefix:
            if i not in curr.child:
                return False
            curr = curr.child[i]
        return True


##############
# USING DEFAULTDICT
##############

class Node:

    def __init__(self):
        self.end = False
        self.child = defaultdict(Node)


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for i in word:
            curr = curr.child[i]
        curr.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for i in word:
            if i not in curr.child:
                return False
            curr = curr.child[i]
        return True if curr.end else False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for i in prefix:
            if i not in curr.child:
                return False
            curr = curr.child[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

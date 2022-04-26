class TrieNode:
    def __init__(self, end=False):
        self.children = [None] * 26
        self.end = end


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Time: O(m); Space: O(1)
    def insert(self, word: str) -> None:

        curr = self.root

        for c in word:
            if curr.children[self.index(c)] is None:
                curr.children[self.index(c)] = TrieNode()

            curr = curr.children[self.index(c)]

        curr.end = True

    def search(self, word: str) -> bool:

        curr = self.root

        for c in word:
            if curr.children[self.index(c)] is None:
                return False

            curr = curr.children[self.index(c)]

        return curr.end

    # Time: O(m); Space: O(1)

    def startsWith(self, prefix: str) -> bool:

        curr = self.root

        for c in prefix:
            if curr.children[self.index(c)] is None:
                return False

            curr = curr.children[self.index(c)]

        return True

    def index(self, c):
        return ord(c) - ord("a")


Sol = Trie()

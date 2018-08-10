class Node(object):
    def __init__(self):
        self.children = dict()


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.roots = dict()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = 0
        nodes = self.roots
        while cur < len(word):
            char = word[cur]
            if char not in nodes:
                nodes[char] = Node()
            nodes = nodes[char].children
            cur += 1
        nodes[""] = Node()

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = 0
        nodes = self.roots
        while cur < len(word):
            char = word[cur]
            if char in nodes:
                nodes = nodes[char].children
            else:
                return False
            cur += 1
        return "" in nodes

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = 0
        nodes = self.roots
        while cur < len(prefix):
            char = prefix[cur]
            if char in nodes:
                nodes = nodes[char].children
            else:
                return False
            cur += 1
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
obj.insert("banana")
print(obj.search("app"))
print(obj.startsWith("ap"))
print(obj.search("banana"))
print(obj.search("ban"))
print(obj.startsWith("ban"))
print(obj.search("bananapple"))

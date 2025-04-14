class Trie:

    def __init__(self):
        self.next = {}
        self.is_end = False

    def insert(self, word: str) -> None:
        curr = self
        for char in word:
            if char not in curr.next:
                curr.next[char] = Trie()
            curr = curr.next[char]
        curr.is_end = True
        

    def search(self, word: str) -> bool:
        curr = self
        for char in word:
            if char not in curr.next:
                return False
            curr = curr.next[char]
        return curr.is_end


    def startsWith(self, prefix: str) -> bool:
        curr = self
        for char in prefix:
            if char not in curr.next:
                return False
            curr = curr.next[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
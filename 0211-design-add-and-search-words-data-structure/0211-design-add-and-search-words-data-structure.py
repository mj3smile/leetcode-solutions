class Character:
    def __init__(self):
        self.children = dict()
        self.word = False

class WordDictionary:
    def __init__(self):
        self.root = Character()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Character()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            curr = node
            
            for c in range(i, len(word)):
                char = word[c]
                if char == ".":
                    for child in curr.children.values():
                        if dfs(c + 1, child):
                            return True
                    return False
                else:
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
            return curr.word
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
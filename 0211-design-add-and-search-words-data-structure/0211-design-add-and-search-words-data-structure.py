class TrieNode:
    def __init__(self, letter = ""):
        self.letter = letter
        self.children = dict() # key: letter, val: TrieNode
        self.end_of_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode(char)
            curr = curr.children[char]
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        return self.searchWithIndex(word, 0, self.root)

    def searchWithIndex(self, word, start_index, root):
        curr_root = root
        for i in range(start_index, len(word)):
            char = word[i]
            if char == ".":
                for child in curr_root.children.values():
                    if self.searchWithIndex(word, i + 1, child):
                        return True
                return False
            else:
                if char not in curr_root.children:
                    return False
                curr_root = curr_root.children[char]
        return curr_root.end_of_word

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
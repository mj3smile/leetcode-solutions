class Node:
    def __init__(self):
        self.children = dict()
        self.word = False

class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        if word == "":
            return
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = Node()
            curr = curr.children[char]
        curr.word = True

    def search(self, word: str) -> bool:
        if word == "":
            return False
        return self.searchWithRoot(word, 0, self.root)
        
    
    def searchWithRoot(self, word, index, root):
        if index == len(word):
            return root.word
        
        if word[index] == ".":
            for child in root.children.values():
                if self.searchWithRoot(word, index + 1, child):
                    return True
            return False
        elif word[index] not in root.children:
            return False
        else:
            return self.searchWithRoot(word, index + 1, root.children[word[index]])

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
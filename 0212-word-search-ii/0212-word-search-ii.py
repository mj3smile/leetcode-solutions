class Letter:
    def __init__(self):
        self.children = dict()
        self.word = False

class Trie:
    def __init__(self, words):
        self.root = Letter()
        for word in words:
            curr = self.root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = Letter()
                curr = curr.children[c]
            curr.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        groupByFirstLetter = dict()
        for word in words:
            groupByFirstLetter[word[0]] = groupByFirstLetter.get(word[0], set())
            groupByFirstLetter[word[0]].add(word)
        
        self.trie = Trie(words)
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board
        result = list()
        for r in range(len(board)):
            for c in range(len(board[r])):
                if len(groupByFirstLetter) == 0:
                    return result

                if board[r][c] not in groupByFirstLetter:
                    continue
                
                for word in self.existWords(r, c, self.trie.root, "", set(), set()):
                    if word in groupByFirstLetter[board[r][c]]:
                        groupByFirstLetter[board[r][c]].remove(word)
                        result.append(word)

                if len(groupByFirstLetter[board[r][c]]) == 0:
                    del groupByFirstLetter[board[r][c]]
        
        return result

    
    def existWords(self, row, col, root, word, visited, result):
        if root.word:
            result.add(word)

        if row < 0 or row == self.ROWS or col < 0 or col == self.COLS or self.board[row][col] not in root.children or (row, col) in visited:
            return result
        
        char = self.board[row][col]
        visited.add((row, col))
        self.existWords(row + 1, col, root.children[char], word + char, visited, result) 
        self.existWords(row - 1, col, root.children[char], word + char, visited, result) 
        self.existWords(row, col - 1, root.children[char], word + char, visited, result)
        self.existWords(row, col + 1, root.children[char], word + char, visited, result)
        visited.remove((row, col))
        return result
        
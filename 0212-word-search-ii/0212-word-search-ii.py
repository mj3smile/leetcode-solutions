class Trie:
    def __init__(self):
        self.children = dict()
        self.word = False
        self.childs = 0
    
    def insert(self, word: str) -> None:
        curr = self
        curr.childs += 1
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
            curr.childs += 1
        curr.word = True
    
    def remove(self, word: str) -> None:
        curr = self
        curr.childs -= 1
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
                curr.childs -= 1
        curr.word = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:   
        root = Trie()
        for w in words:
            root.insert(w)
        result, visited = set(), set()
        
        def find(r, c, node, word):
            if r < 0 or c < 0 or r == len(board) or c == len(board[0]) or (r, c) in visited or node.childs < 1 or board[r][c] not in node.children:
                return
            
            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.word:
                result.add(word)
                root.remove(word)
            
            find(r, c + 1, node, word)
            find(r, c - 1, node, word)
            find(r + 1, c, node, word)
            find(r - 1, c, node, word)
            visited.remove((r, c))
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                find(r, c, root, '')
        return list(result)
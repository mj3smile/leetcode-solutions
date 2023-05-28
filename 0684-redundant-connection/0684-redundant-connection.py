class UnionFind:
    def __init__(self, n):
        self.parent = dict()
        self.rank = dict()
        
        for i in range(1, n+1):
            self.parent[i] = i
            self.rank[i] = 0
    
    def findParent(self, n):
        parent = self.parent[n]
        while parent != self.parent[parent]:
            self.parent[parent] = self.parent[self.parent[parent]]
            parent = self.parent[parent]
        return parent
    
    def union(self, n1, n2):
        p1, p2 = self.findParent(n1), self.findParent(n2)
        if p1 == p2: return False
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        u = UnionFind(len(edges))
        result = edges[0]
        for n1, n2 in edges:
            if not u.union(n1, n2):
                result = [n1, n2]
        return result
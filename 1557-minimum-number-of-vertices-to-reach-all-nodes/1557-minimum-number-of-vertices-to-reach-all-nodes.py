class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        unreachable = set(list(range(n)))
        for s, d in edges:
            if d in unreachable:
                unreachable.remove(d)
        
        return list(unreachable)
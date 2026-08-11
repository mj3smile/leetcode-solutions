class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        reachableFrom = set()
        for s, d in edges:
            reachableFrom.add(d)
        
        result = list()
        for i in range(n):
            if i not in reachableFrom:
                result.append(i)
        
        return result
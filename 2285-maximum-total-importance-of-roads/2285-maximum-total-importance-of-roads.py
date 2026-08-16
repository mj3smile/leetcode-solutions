class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        neighbors = list()
        neighbors_index = dict()

        for r1, r2 in roads:
            if r1 not in neighbors_index:
                neighbors_index[r1] = len(neighbors)
                neighbors.append([0, r1])
            if r2 not in neighbors_index:
                neighbors_index[r2] = len(neighbors)
                neighbors.append([0, r2])
            
            neighbors[neighbors_index[r1]][0] += 1
            neighbors[neighbors_index[r2]][0] += 1
        
        heapq.heapify_max(neighbors)
        values = dict()
        for v in range(n, 0, -1):
            if not neighbors:
                break
            _, r = heapq.heappop_max(neighbors)
            values[r] = v
        
        result = 0
        for r1, r2 in roads:
            result += values[r1] + values[r2]
        
        return result

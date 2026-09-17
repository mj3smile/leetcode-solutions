class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        unique = dict()
        numByFreq = list()

        for n in arr:
            unique[n] = unique.get(n, 0) + 1
        
        for n, f in unique.items():
            heapq.heappush(numByFreq, [f, n])
        
        for i in range(k):
            if not numByFreq:
                break

            numByFreq[0][0] -= 1
            unique[numByFreq[0][1]] -= 1
            if numByFreq[0][0] == 0:
                del unique[numByFreq[0][1]]
                heapq.heappop(numByFreq)
        
        return len(unique)
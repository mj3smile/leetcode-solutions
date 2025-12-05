class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        freq = [(-a, "a"), (-b, "b"), (-c, "c")]
        heapq.heapify(freq)

        result = ""
        while True:
            top2Chars = heapq.nsmallest(2, freq)
            first, second = top2Chars
            # print(top2Chars)
            # if first[0] == 0:
            #     break

            if first[0] != 0 and (result == "" or result[-1] != first[1]):
                n = min(first[0] * -1, 2)
                for _ in range(n):
                    result += first[1]

                heapq.heappop(freq)
                heapq.heappush(freq, (first[0] + n, first[1]))
            elif second[0] != 0:
                n = min(second[0] * -1, 1)
                for _ in range(n):
                    result += second[1]
                
                heapq.heappop(freq)
                heapq.heappop(freq)
                heapq.heappush(freq, first)
                heapq.heappush(freq, (second[0] + n, second[1]))
            else:
                break
            
            # print(result)
        return result
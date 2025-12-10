class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = dict()
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        heap = list()
        heapq.heapify(heap)
        for char, freq in freq.items():
            heapq.heappush(heap, (-freq, char))
        
        result = ""
        while heap:
            most_freq_char = heapq.heappop(heap)
            freq1, char1 = -most_freq_char[0], most_freq_char[1]
            if freq1 > 0 and (result == "" or result[-1] != char1):
                result += char1
                if freq1 > 1: heapq.heappush(heap, (-freq1 + 1, char1))
                continue
            
            if not heap:
                return ""
                
            second_most_char = heapq.heappop(heap)
            freq2, char2 = -second_most_char[0], second_most_char[1]
            if freq2 > 0:
                result += char2
                if freq1 > 0: heapq.heappush(heap, most_freq_char)
                if freq2 > 1: heapq.heappush(heap, (-freq + 1, char))
                continue
            
            return ""
        
        return result
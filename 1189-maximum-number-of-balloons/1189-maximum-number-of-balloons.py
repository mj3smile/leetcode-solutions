class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        index = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        least_freq = 'b'
        
        for i in text:
            if not i in index: continue
            index[i] += 1
            if index[i] <= index[least_freq]: least_freq = i
        
        # if min(index['l'], index['o']) // 2 == index[least_freq]: return index[least_freq]
        
        return min(min(index['l'], index['o']) // 2, index[least_freq])
    
    
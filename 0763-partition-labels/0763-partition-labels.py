class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        rightestIndex = dict()
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in rightestIndex:
                rightestIndex[s[i]] = i
        
        result = []
        while i < len(s):
            length = rightestIndex[s[i]]
            j = i + 1
            while j < length:
                length = max(length, rightestIndex[s[j]])
                j += 1
            
            result.append(length - i + 1)
            i = length + 1
            
        
        return result
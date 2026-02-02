class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = []

        first_appereance = dict()
        for i in range(len(s)):
            char = s[i]
            # if not result:
            #     result.append(0)
            
            if char not in first_appereance:
                first_appereance[char] = i
                result.append(1)
            else:
                total = i - first_appereance[char] + 1
                curr = 1
                while curr < total and result:
                    curr += result.pop()
                result.append(curr)
        
        return result
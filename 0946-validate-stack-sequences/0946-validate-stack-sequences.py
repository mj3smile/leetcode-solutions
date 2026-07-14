class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        result = []

        i = 0
        for p in pushed:
            result.append(p)
            
            while result and result[-1] == popped[i]:
                result.pop()
                i += 1
        
        return len(result) == 0
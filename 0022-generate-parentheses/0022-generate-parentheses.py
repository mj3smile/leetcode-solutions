class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = list()

        def combination(openCount, closeCount, currCombination):
            if openCount > n or closeCount > n or closeCount > openCount:
                return

            nonlocal result
            if openCount == n and closeCount == n:
                result.append(currCombination)
                return
            combination(openCount + 1, closeCount, currCombination + "(")
            combination(openCount, closeCount + 1, currCombination + ")")
            
        combination(0, 0, "")
        return result

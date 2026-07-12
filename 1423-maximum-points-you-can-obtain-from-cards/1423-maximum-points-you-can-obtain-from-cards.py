class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        prefix = [0 for _ in range(n)]
        suffix = [0 for _ in range(n)]

        for left in range(n):
            right = n - 1 - left
            prefix[left] = cardPoints[left]
            suffix[right] = cardPoints[right]

            if left > 0:    
                prefix[left] += prefix[left - 1]
                suffix[right] += suffix[right + 1]
        
        result = 0
        for i in range(k + 1):
            left, right = i - 1, n - (k - i)
            leftSum = 0
            if left >= 0:
                leftSum = prefix[left]
            rightSum = 0
            if right < n:
                rightSum = suffix[right]

            result = max(result, leftSum + rightSum)
        
        return result
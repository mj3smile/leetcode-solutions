class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0
        l, r = 0, len(tokens) - 1
        while l <= r:
            if power >= tokens[l]:
                while l <= r and power >= tokens[l]:
                    score += 1
                    power -= tokens[l]
                    l += 1
            elif score > 0 and l < r and tokens[r] >= tokens[l]:
                power += tokens[r]
                score -= 1
                r -= 1
            else:
                break
        
        return score
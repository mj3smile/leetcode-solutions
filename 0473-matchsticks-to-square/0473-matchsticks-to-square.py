class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        
        max_length = total // 4
        total_sides = [0, 0, 0, 0]

        def canMakeSquare(index):
            if index == len(matchsticks):
                return total_sides[0] == max_length and total_sides[1] == max_length and total_sides[2] == max_length and total_sides[3] == max_length
            
            result = False
            for i in range(len(total_sides)):
                if i > 0 and total_sides[i - 1] == total_sides[i]:
                    continue
                    
                new_total = total_sides[i] + matchsticks[index]
                if new_total <= max_length:
                    total_sides[i] += matchsticks[index]
                    if canMakeSquare(index + 1):
                        return True
                    total_sides[i] -= matchsticks[index]
                elif new_total > max_length:
                    continue
            
            return result
        
        return canMakeSquare(0)
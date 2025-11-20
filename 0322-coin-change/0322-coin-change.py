class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coins = coins
        self.amount = amount
        self.coins.sort()
        
        i = 0
        while i + 1 < len(self.coins) and self.coins[i + 1] <= amount:
            i += 1
        
        self.found = False
        self.result = amount
        while i >= 0:
            r = self.calculateCoins(i, 0, dict())
            if r > -1:
                self.result = min(self.result, r)
                self.found = True
            i -= 1
        
        if not self.found:
            return -1
        return self.result

    def calculateCoins(self, index, total, cache):
        # print("index:", index, "total:", total)
        if index < 0 or index == len(self.coins) or total > self.amount:
            return -1
        
        if total == self.amount:
            return 0
        
        if (index, total) in cache:
            return cache[(index, total)]
        
        result = self.amount - total
        found = False
        for i in range(index, -1, -1):
            r = self.calculateCoins(i, total + self.coins[index], cache)
            if r > -1:
                result = min(result, r)
                found = True
                # if index == 2 and total == 0:
                #     print("result:", result, "r:", r, "found:", found)
                

        if not found:
            cache[(index, total)] = -1
            return -1
        
        cache[(index, total)] = 1 + result
        return 1 + result
class Solution:
    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        
        result = 0
        for i in range(len(nums)):
            robbed_house = [False] * len(nums)
            self.cache = dict()
            profit = self.countMaxProfit(i, robbed_house)
            result = max(result, profit)
        
        return result
    
    def countMaxProfit(self, house: int, robbed_house: List[bool]) -> int:
        left_house = (house - 1) % len(self.nums)
        right_house = (house + 1) % len(self.nums)
        if robbed_house[left_house] or robbed_house[right_house]:
            return 0
        
        house = house % len(self.nums)
        if robbed_house[house]:
            return 0
        
        if house in self.cache:
            return self.cache[house]
        
        robbed_house[house] = True
        one = self.countMaxProfit(house + 2, robbed_house)
        two = self.countMaxProfit(house + 3, robbed_house)
        robbed_house[house] = False
        
        self.cache[house] = self.nums[house] + max(one, two)
        return self.cache[house]
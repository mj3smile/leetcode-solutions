class Solution:
    def canJump(self, nums: List[int]) -> bool:
        self.nums = nums
        self.cache = dict()

        return self.jump(0)

    def jump(self, index):
        if index >= len(self.nums) - 1:
            return True
        
        if self.nums[index] == 0:
            return False
        
        if index in self.cache:
            return self.cache[index]
        
        result = False
        for i in range(index + self.nums[index], index, -1):
            result = result or self.jump(i)
            if result: break
        
        self.cache[index] = result
        return self.cache[index]
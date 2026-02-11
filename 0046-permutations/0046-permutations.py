class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.result = list()
        self.construct(list(), [False for _ in range(len(nums))])
        return self.result
    
    def construct(self, permutation, picked):
        if len(permutation) == len(self.nums):
            self.result.append(permutation.copy())
            return
        
        for i in range(len(self.nums)):
            if picked[i]:
                continue
            picked[i] = True
            permutation.append(self.nums[i])
            self.construct(permutation, picked)
            picked[i] = False
            permutation.pop()
        
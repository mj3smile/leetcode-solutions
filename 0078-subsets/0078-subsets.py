class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.n = len(nums)
        self.result = list()
        self.generateSubsets(0, list(), set())
        return self.result

    def generateSubsets(self, index, items, cache):
        i = items.copy()
        key = tuple(i)
        if key not in cache:
            self.result.append(i)
            cache.add(key)

        if index == self.n:
            return
        
        items.append(self.nums[index])
        self.generateSubsets(index + 1, items, cache)
        items.pop()

        self.generateSubsets(index + 1, items, cache)
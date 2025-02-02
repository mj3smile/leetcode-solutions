class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = nums[0]
        frequency = dict()

        for n in nums:
            frequency[n] = frequency.get(n, 0) + 1
            if frequency[n] > frequency[result]:
                result = n
        
        return result
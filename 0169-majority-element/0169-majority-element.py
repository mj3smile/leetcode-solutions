class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        index = dict()
        most_freq = nums[0]
        
        
        for i in nums:
            index[i] = index.get(i, 0) + 1
            if index[i] > index[most_freq]:
                most_freq = i
        
        return most_freq
        
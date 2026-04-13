class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n < 3:
            return list(set(nums))
        
        appereanceLimit = n / 3
        appereances = dict()

        result = set()
        for n in nums:
            appereances[n] = appereances.get(n, 0) + 1
            if appereances[n] > appereanceLimit:
                result.add(n)
        
        return list(result)
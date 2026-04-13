class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        prefixSums = {0: 1}

        currSum = 0
        for n in nums:
            currSum += n
            diff = currSum - k

            if diff in prefixSums:
                result += prefixSums[diff]
            
            prefixSums[currSum] = prefixSums.get(currSum, 0) + 1
        
        return result
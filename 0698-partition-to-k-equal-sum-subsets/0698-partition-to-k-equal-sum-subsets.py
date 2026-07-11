class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        
        target = total / k
        subsets = [0 for _ in range(k)]
        
        nums.sort(reverse=True)
        def canPartition(index):
            if index == len(nums):
                return sum(subsets) == total
            
            for i in range(len(subsets)):
                if i > 0 and subsets[i] == subsets[i - 1]:
                    continue

                new_total = subsets[i] + nums[index]
                if new_total <= target:
                    subsets[i] = new_total
                    if canPartition(index + 1):
                        return True
                    subsets[i] -= nums[index]
            
            return False
        
        return canPartition(0)

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = list()
        cache = set()
        combination = dict() # key: index of nums, val: map(key: 3sum, val: arr of second and third index)

        nums.sort()
        for n1 in range(len(nums)):
            if target > 0 and nums[n1] > target and len(result) > 0:
                break
            
            if n1 > 0 and nums[n1] == nums[n1 - 1]:
                continue

            for n2 in range(n1 + 1, len(nums)):
                total = target - nums[n1] - nums[n2]
                n3, n4 = n2 + 1, len(nums) - 1

                while n3 < n4:
                    two_sum = nums[n3] + nums[n4]
                    if two_sum == total:
                        cacheable = (nums[n1], nums[n2], nums[n3], nums[n4])
                        if cacheable not in cache:
                            result.append([nums[n1], nums[n2], nums[n3], nums[n4]])
                            cache.add(cacheable)
                        
                        n4 -= 1
                        n3 += 1
                    elif two_sum > total:
                        n4 -= 1
                    else:
                        n3 += 1
        
        return result
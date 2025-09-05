class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_to_r = [1] * len(nums)
        r_to_l = [1] * len(nums)

        for l in range(len(nums)):
            r = len(nums) - 1 - l

            if l == 0:
                l_to_r[l] = nums[l]
                r_to_l[r] = nums[r]
                continue
            
            l_to_r[l] = nums[l] * l_to_r[l - 1]
            r_to_l[r] = nums[r] * r_to_l[r + 1]
        
        result = list()
        for i in range(len(nums)):
            if i == 0:
                result.append(r_to_l[i + 1])
                continue
            
            if i == len(nums) - 1:
                result.append(l_to_r[i - 1])
                continue
            
            l = l_to_r[i - 1]
            r = r_to_l[i + 1]
            result.append(l * r)
        
        return result
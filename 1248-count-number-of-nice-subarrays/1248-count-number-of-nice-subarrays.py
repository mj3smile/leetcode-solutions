class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def is_odd(n):
            return n % 2 != 0

        odd = 0
        result = 0
        l, m = 0, 0
        for r in range(len(nums)):
            if is_odd(nums[r]):
                odd += 1

            while odd > k:
                if is_odd(nums[l]):
                    odd -= 1
                l += 1
                m = l
            
            if odd == k:
                while not is_odd(nums[m]):
                    m += 1
                result += (m - l) + 1
        
        return result

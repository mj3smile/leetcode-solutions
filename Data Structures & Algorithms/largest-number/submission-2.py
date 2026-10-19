from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def comparator(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            return 0

        nums_str = [str(n) for n in nums]
        nums_str.sort(key=cmp_to_key(comparator))
        result = "".join(nums_str)
        if len(result) > 0 and result[0] == "0":
            return "0"
        return result
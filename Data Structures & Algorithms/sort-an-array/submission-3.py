class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def getLeft(p):
            return (p + 1) * 2 - 1
        def getRight(p):
            return (p + 1) * 2
        
        n = len(nums)
        for i in range(len(nums) - 1, -1, -1):
            p = i
            l, r = getLeft(p), getRight(p)
            while l < n and nums[p] < nums[l] or r < n and nums[p] < nums[r]:
                if r >= n or nums[l] >= nums[r]:
                    nums[p], nums[l] = nums[l], nums[p]
                    p = l
                else:
                    nums[p], nums[r] = nums[r], nums[p]
                    p = r
                l, r = getLeft(p), getRight(p)
        
        nums[len(nums) - 1], nums[0] = nums[0], nums[len(nums) - 1]
        newLen = len(nums) - 1
        while newLen > 1:
            p = 0
            l, r = getLeft(p), getRight(p)
            while l < newLen and nums[p] < nums[l] or r < newLen and nums[p] < nums[r]:
                if r >= newLen or nums[l] >= nums[r]:
                    nums[p], nums[l] = nums[l], nums[p]
                    p = l
                else:
                    nums[p], nums[r] = nums[r], nums[p]
                    p = r
                l, r = getLeft(p), getRight(p)

            newLen -= 1
            nums[newLen], nums[0] = nums[0], nums[newLen]
        
        return nums
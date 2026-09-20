class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def getLeft(p):
            return (p + 1) * 2 - 1
        def getRight(p):
            return (p + 1) * 2
        
        n = len(nums)
        for i in range(len(nums) - 1, -1, -1):
            j = i
            l, r = getLeft(j), getRight(j)
            while l < n and nums[j] < nums[l] or r < n and nums[j] < nums[r]:
                if r >= n or nums[l] >= nums[r]:
                    nums[j], nums[l] = nums[l], nums[j]
                    j = l
                else:
                    nums[j], nums[r] = nums[r], nums[j]
                    j = r
                l, r = getLeft(j), getRight(j)
        
        nums[len(nums) - 1], nums[0] = nums[0], nums[len(nums) - 1]
        newLen = len(nums) - 1
        while newLen > 1:
            p = 0
            l, r = getLeft(p), getRight(p)
            while l < newLen and nums[l] > nums[p] or r < newLen and nums[r] > nums[p]:
                if r >= newLen or nums[l] >= nums[r]:
                    nums[l], nums[p] = nums[p], nums[l]
                    p = l
                else:
                    nums[r], nums[p] = nums[p], nums[r]
                    p = r
                l, r = getLeft(p), getRight(p)

            newLen -= 1
            nums[newLen], nums[0] = nums[0], nums[newLen]
        
        return nums
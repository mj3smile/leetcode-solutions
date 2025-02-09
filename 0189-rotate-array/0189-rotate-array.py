class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        temp = []
        last_first_element = 0
        n = 0
        for iteration in range(len(nums)):
            next_n = (n + k) % len(nums)

            if len(temp) == 0:
                temp.append(nums[next_n])
                nums[next_n] = nums[n]
            else:
                nums[next_n], temp[0] = temp[0], nums[next_n]
            
            n = next_n
            if next_n == last_first_element:
                temp = []
                n += 1
                last_first_element = n
            


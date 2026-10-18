class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = list()
        results_set = set()

        def sets(index, subset):
            key = tuple(list(subset))
            if key not in results_set:
                result.append(list(subset))
                results_set.add(key)
            if len(subset) == len(nums):
                return
            for i in range(index, len(nums)):
                if nums[i] in subset:
                    continue
                subset.add(nums[i])
                sets(i + 1, subset)
                subset.remove(nums[i])

        sets(0, set())
        return result
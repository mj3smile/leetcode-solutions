class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        cache = set()
        result = [[]]
        
        def find(arr, i, subset):
            if i >= len(arr):
                return
            
            subset.append(arr[i])
            if not tuple(subset) in cache:
                result.append(subset.copy())
                cache.add(tuple(subset))
            
            find(arr, i + 1, subset)
            subset.pop()
            find(arr, i + 1, subset)
        
        find(nums, 0, [])
        return result
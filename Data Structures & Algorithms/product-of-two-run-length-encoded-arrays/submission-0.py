class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        def decode(encoded):
            n = list()
            for v, f in encoded:
                for _ in range(f):
                    n.append(v)
            return n
        
        def encode(nums):
            encoded = list()
            i = 0
            while i < len(nums):
                v = nums[i]
                f = 1

                i += 1
                while i < len(nums) and nums[i] == v:
                    f += 1
                    i += 1
                encoded.append([v, f])
            return encoded
        
        nums1 = decode(encoded1)
        nums2 = decode(encoded2)
        for i in range(len(nums1)):
            nums1[i] = nums1[i] * nums2[i]
        
        return encode(nums1)
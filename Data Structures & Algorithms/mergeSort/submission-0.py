# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def merge(self, original, arr1, arr2):
        j, k = 0, 0
        for i in range(len(original)):
            if k >= len(arr2) or j < len(arr1) and arr1[j].key <= arr2[k].key:
                original[i] = arr1[j]
                j += 1
            else:
                original[i] = arr2[k]
                k += 1
        return original

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) < 2:
            return pairs
        
        s, e = 0, len(pairs)
        m = (s + e) // 2

        half1 = self.mergeSort(pairs[s:m])
        half2 = self.mergeSort(pairs[m:e])

        # def printHalf(h):
        #     r = list()
        #     for i in h:
        #         r.append((i.key, i.value))
        #     print(r)
        
        # printHalf(half1)
        # printHalf(half2)
        mer = self.merge(pairs.copy(), half1, half2)
        # printHalf(mer)
        # print("aaaaaaaaaaaaaaaaaaaa")
        return mer
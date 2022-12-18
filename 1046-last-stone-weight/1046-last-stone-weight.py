class Solution:
    def percolateDown(self, root, arr):
        i = root
        while 2 * i < len(arr):
            if 2 * i + 1 < len(arr) and arr[2 * i + 1] > arr[2 * i] and arr[2 * i + 1] > arr[i]:
                arr[i], arr[2 * i + 1] = arr[2 * i + 1], arr[i]
                i = 2 * i + 1
            elif arr[2 * i] > arr[i]:
                arr[i], arr[2 * i] = arr[2 * i], arr[i]
                i = 2 * i
            else:
                break
        return arr
        
    def heapify(self, arr):
        arr.append(arr[0])
        i = (len(arr) - 1) // 2
        while i > 0:
            arr = self.percolateDown(i, arr)
            i -= 1
        return arr
    
    def append(self, arr, val):
        arr.append(val)
        i = len(arr) - 1
        while i // 2 >= 1 and arr[i] > arr[i // 2]:
            arr[i], arr[i // 2] = arr[i // 2], arr[i]
            i = i // 2
        return arr
    
    def pop(self, arr):
        if len(arr) == 1:
            return arr
        if len(arr) == 2:
            arr.pop()
            return arr
        
        arr[1] = arr.pop()
        return self.percolateDown(1, arr)
        
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = self.heapify(stones)
        print(heap)
        while len(heap) > 2:
            y = heap[1]
            x = heap[3] if 3 < len(heap) and heap[3] > heap[2] else heap[2]
            new_weight = y - x
            heap = self.pop(heap)
            heap = self.pop(heap)
            if new_weight > 0:
                heap = self.append(heap, new_weight)
            print(heap)
        
        return 0 if len(heap) < 2 else heap[1]
        
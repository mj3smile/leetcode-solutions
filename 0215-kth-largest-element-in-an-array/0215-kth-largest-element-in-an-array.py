class MinHeap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.nodes = [0]
    
    def push(self, val):
        if len(self.nodes) - 1 == self.capacity:
            if val >= self.getRoot():
                self.popAndReplaceWithValue(val)
            return
        
        self.nodes.append(val)
        child_index = len(self.nodes) - 1
        parent_index = child_index // 2
        while parent_index > 0 and self.nodes[parent_index] > self.nodes[child_index]:
            self.nodes[parent_index], self.nodes[child_index] = self.nodes[child_index], self.nodes[parent_index]
            child_index = parent_index
            parent_index = parent_index // 2
    
    def popAndReplaceWithValue(self, val):
        if len(self.nodes) < 2:
            return 0
        
        root = self.nodes[1]
        if len(self.nodes) == 2:
            self.nodes[1] = val
            return root
        
        self.nodes[1] = val
        parent_index = 1
        left_child_index = 2
        right_child_index = 3
        while (left_child_index < len(self.nodes) and self.nodes[parent_index] > self.nodes[left_child_index]) or (right_child_index < len(self.nodes) and self.nodes[parent_index] > self.nodes[right_child_index]):
            if right_child_index >= len(self.nodes) or self.nodes[left_child_index] < self.nodes[right_child_index]:
                self.nodes[parent_index], self.nodes[left_child_index] = self.nodes[left_child_index], self.nodes[parent_index]
                parent_index = left_child_index
            else:
                self.nodes[parent_index], self.nodes[right_child_index] = self.nodes[right_child_index], self.nodes[parent_index]
                parent_index = right_child_index

            left_child_index = parent_index * 2
            right_child_index = parent_index * 2 + 1
        
        return root

    def getRoot(self):
        return self.nodes[1]

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = MinHeap(k)
        for n in nums:
            heap.push(n)
        return heap.getRoot()
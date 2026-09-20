class MinHeap:
    def __init__(self):
        self.items = [0]

    def push(self, val: int) -> None:
        self.items.append(val)
        if len(self.items) == 2:
            return

        index = len(self.items) - 1
        parent = index // 2
        while parent > 0 and self.items[parent] > self.items[index]:
            self.items[parent], self.items[index] = self.items[index], self.items[parent]
            index = parent
            parent = index // 2

    def pop(self) -> int:
        top = self.top()
        if top == -1:
            return top
        if len(self.items) == 2:
            return self.items.pop()

        self.items[1] = self.items.pop()
        index = 1
        child_left, child_right = index * 2, index * 2 + 1

        n = len(self.items)
        while child_left < n and self.items[index] > self.items[child_left] or child_right < n and self.items[index] > self.items[child_right]:
            if child_right >= n or self.items[child_left] < self.items[child_right]:
                self.items[index], self.items[child_left] = self.items[child_left], self.items[index]
                index = child_left
            else:
                self.items[index], self.items[child_right] = self.items[child_right], self.items[index]
                index = child_right
            child_left, child_right = index * 2, index * 2 + 1
        
        return top

    def top(self) -> int:
        if len(self.items) == 1:
            return -1
        return self.items[1]

    def heapify(self, nums: List[int]) -> None:
        self.items = [0]
        for n in nums:
            self.push(n)
        
        
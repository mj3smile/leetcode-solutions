class SegmentTree:
    def __init__(self, left, right, sum = 0):
        self.left = left
        self.right = right
        self.sum = sum
        self.lnode = None
        self.rnode = None
    
    def update(self, index, val):
        if self.right == index and self.left == index:
            self.sum = val
            return
        
        m = (self.left + self.right) // 2
        if index > m:
            self.rnode.update(index, val)
        else:
            self.lnode.update(index, val)
        self.sum = self.lnode.sum + self.rnode.sum
    
    def sumRange(self, left, right):
        if right == self.right and left == self.left:
            return self.sum
        
        m = (self.left + self.right) // 2
        if left > m:
            return self.rnode.sumRange(left, right)
        elif right <= m:
            return self.lnode.sumRange(left, right)
        else:
            return (self.lnode.sumRange(left, m) + self.rnode.sumRange(m + 1, right))

class NumArray:
    def __init__(self, nums: List[int]):
        self.root = self.build(0, len(nums) - 1, nums)
        
    def build(self, left, right, nums):
        if left == right:
            return SegmentTree(left, right, nums[left])
        
        m = (left + right) // 2
        root = SegmentTree(left, right)
        root.lnode = self.build(left, m, nums)
        root.rnode = self.build(m + 1, right, nums)
        root.sum = root.lnode.sum + root.rnode.sum
        return root
        
    def update(self, index: int, val: int) -> None:
        self.root.update(index, val)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.root.sumRange(left, right)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
class Node:
    def __init__(self, value = 0):
        self.val = value
        self.next = None
        self.prev = None

class RangeNode:
    def __init__(self, value = 0):
        self.val = value
        self.head = None
        self.tail = None
        self.count = 0
    
    def add(self):
        node = Node(self.val)
        if self.count == 0:
            self.count += 1
            self.head = node
            self.tail = node
            return
        
        self.count += 1
        node.next = self.tail.next
        self.tail.next.prev = node
        node.prev = self.tail
        self.tail.next = node
        self.tail = node

class MedianFinder:
    def __init__(self):
        self.length = 0
        self.plus = [None]
        self.min_plus_value = 10**5
        self.minus = [None]
        self.max_minus_value = -10**5
        self.list_head = Node()
        self.list_tail = Node()
        self.list_head.next = self.list_tail
        self.list_tail.prev = self.list_head
        self.median = None

    def addNum(self, num: int) -> None:
        ordered_list_primary = self.plus
        ordered_list_secondary = self.minus
        sign = 1
        if num < 0:
            # print("==============")
            # print("signed:", num)
            ordered_list_primary = self.minus
            ordered_list_secondary = self.plus
            sign = -1
            num *= sign
        
        if len(ordered_list_primary) < num + 1:
            new_cap = [None] * (num + 1 - len(ordered_list_primary))
            ordered_list_primary += new_cap
        
        range_node = RangeNode(num * sign)
        new_range_node = False
        if ordered_list_primary[num]:
            range_node = ordered_list_primary[num]
        else:
            ordered_list_primary[num] = range_node
            new_range_node = True
            if sign > 0 and num < self.min_plus_value:
                self.min_plus_value = num
                ordered_list_secondary[0] = range_node
            if sign < 0 and num > self.max_minus_value:
                self.max_minus_value = num * sign
                ordered_list_secondary[0] = range_node
        range_node.add()

        left, right = None, None
        l, r = num - 1, num + 1
        while new_range_node and left == None and right == None and (l >= 0 or r < len(ordered_list_primary)):
            if l >= 0:
                left = ordered_list_primary[l]
            if r < len(ordered_list_primary):
                right = ordered_list_primary[r]
            l, r = l-1, r+1
        
        if sign < 0: left, right = right, left
        if left:
            tail = left.tail
            tail.next.prev = range_node.tail
            range_node.tail.next = tail.next
            range_node.head.prev = tail
            tail.next = range_node.head
        elif right:
            head = right.head
            head.prev.next = range_node.head
            range_node.tail.next = head
            range_node.head.prev = head.prev
            head.prev = range_node.tail
        elif self.length == 0:
            self.list_head.next = range_node.head
            range_node.head.prev = self.list_head
            range_node.tail.next = self.list_tail
            self.list_tail.prev = range_node.tail
        
        # if sign < 0:
        #     print("num:", num)
        #     # print("head value:", head.val)
        #     self.printNodes()
        # print("=======================")
        self.length += 1
        if self.length == 1:
            # print("1")
            self.median = range_node.head
        elif self.length % 2 == 0 and num * sign < self.median.val:
            self.median = self.median.prev
            # print("2")
        elif self.length % 2 > 0 and num * sign >= self.median.val:
            self.median = self.median.next
            # print("3")
        
        # print("num:", num)
        # median_val = "null" if self.median == None else str(self.median.val)
        # print("median val:", median_val)
        # print("length:", self.length)

        
    def findMedian(self) -> float:
        if self.length == 0:
            return -1
        
        if self.length % 2 > 0:
            return self.median.val
        else:
            return (self.median.val + self.median.next.val) / 2
    
    def printNodes(self):
        nodes = list()
        head = self.list_head.next
        count = 10
        while count > 0 and head != self.list_tail:
            nodes.append(head.val)
            head = head.next
            count -= 1
        print("nodes:", nodes)
    
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
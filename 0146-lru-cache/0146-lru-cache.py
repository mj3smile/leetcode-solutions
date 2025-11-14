class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = dict()
        self.cache_list_head = Node(0, 0)
        self.cache_list_tail = Node(0, 0)
        self.cache_list_head.next = self.cache_list_tail
        self.cache_list_tail.prev = self.cache_list_head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.updateMRU(key)
        return self.cache[key].val    

    def put(self, key: int, value: int) -> None:
        if self.size == self.capacity and key not in self.cache:
            self.evictLRU()
        
        if key not in self.cache:
            self.size += 1

        self.cache[key] = self.cache.get(key, Node(key, value))
        self.cache[key].val = value
        self.updateMRU(key)
        # self.printList()

    def evictLRU(self):
        if self.size == 0:
            return

        lru_node = self.cache_list_head.next
        self.cache_list_head.next = lru_node.next
        lru_node.next.prev = self.cache_list_head
        lru_node.next = None
        lru_node.prev = None
        del self.cache[lru_node.key]
        self.size -= 1
    
    def updateMRU(self, key):
        if key not in self.cache:
            return
        
        mru_node = self.cache[key]
        if mru_node.prev:
            mru_node.prev.next = mru_node.next
        if mru_node.next:
            mru_node.next.prev = mru_node.prev
        
        mru_node.next = self.cache_list_tail
        self.cache_list_tail.prev.next = mru_node
        mru_node.prev = self.cache_list_tail.prev
        self.cache_list_tail.prev = mru_node
    
    def printList(self):
        curr = self.cache_list_head.next
        nodes = ""
        while curr != self.cache_list_tail:
            nodes += " " + str(curr.val)
            curr = curr.next
        print(nodes)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
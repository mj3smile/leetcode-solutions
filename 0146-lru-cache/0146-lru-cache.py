class Node:
    def __init__(self, key, val, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict() # key: cache key, val: node
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.update_mru(key)
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if len(self.cache) == self.capacity and key not in self.cache:
            self.evict_lru()
            
        if key in self.cache:
            self.cache[key].val = value
        else:
            self.cache[key] = Node(key, value)

        self.update_mru(key)

    def evict_lru(self):
        lru = self.head.next
        self.head.next = lru.next
        self.head.next.prev = self.head
        del self.cache[lru.key]
    
    def update_mru(self, key):
        mru = self.cache[key]
        if mru.prev:
            mru.prev.next = mru.next
        if mru.next:
            mru.next.prev = mru.prev

        self.tail.prev.next = mru
        mru.prev = self.tail.prev
        mru.next = self.tail
        self.tail.prev = mru


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
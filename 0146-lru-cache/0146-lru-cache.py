class Node:
    def __init__(self, key = 0, value = 0):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.storage = dict()
        self.cache_head = Node()
        self.cache_tail = Node()
        self.cache_head.next = self.cache_tail
        self.cache_tail.prev = self.cache_head

    def get(self, key: int) -> int:
        if key not in self.storage:
            return -1
        self.update_mru(key)
        return self.storage[key].val

    def put(self, key: int, value: int) -> None:
        if key not in self.storage and len(self.storage) == self.capacity:
            self.evict_lru()
        
        if key not in self.storage:
            self.storage[key] = Node(key=key, value=value)
        else:
            self.storage[key].val = value

        self.update_mru(key)
    
    def update_mru(self, key):
        if key not in self.storage:
            return
        
        node = self.storage[key]
        if node.next == self.cache_tail:
            return
        
        if node.next != None and node.prev != None:
            node.prev.next = node.next
            node.next.prev = node.prev

        node.next = self.cache_tail
        node.prev = self.cache_tail.prev
        self.cache_tail.prev = node
        node.prev.next = node
    
    def evict_lru(self):
        if len(self.storage) == 0:
            return
        
        node = self.cache_head.next
        self.cache_head.next = node.next
        node.next.prev = self.cache_head
        node.next, node.prev = None, None

        del self.storage[node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
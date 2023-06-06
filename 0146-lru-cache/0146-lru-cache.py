class ListNode:
    def __init__(self, key = -1, val = -1):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.lru = ListNode()
        self.mru = ListNode()
        self.lru.next, self.mru.prev = self.mru, self.lru

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.removeFromCache(self.cache[key])
        self.insertToCache(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.removeFromCache(self.cache[key])
        
        self.cache[key] = ListNode(key, value)
        self.insertToCache(self.cache[key])
        if len(self.cache) > self.capacity:
            self.removeFromCache(self.cache.pop(self.lru.next.key))
            
    def removeFromCache(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
    
    def insertToCache(self, node):
        node.prev, node.next = self.mru.prev, self.mru
        node.prev.next = node
        self.mru.prev = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
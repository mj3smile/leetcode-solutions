class ListNode:
    def __init__(self, key = -1, val = -1):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru = ListNode()
        self.mru = ListNode()
        self.lru.next, self.mru.prev = self.mru, self.lru
        self.cache = dict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = ListNode(key=key, val=value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.capacity:
            self.remove(self.cache.pop(self.lru.next.key))
    
    # insert to right
    def insert(self, node):
        pr, nx = self.mru.prev, self.mru
        pr.next = nx.prev = node
        node.prev, node.next = pr, nx
    
    # remove from list
    def remove(self, node):
        pr, nx = node.prev, node.next
        pr.next, nx.prev = nx, pr

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
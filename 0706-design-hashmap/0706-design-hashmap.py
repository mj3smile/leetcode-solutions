class MyHashMap:
    def __init__(self):
        self.items = list()

    def put(self, key: int, value: int) -> None:
        if key + 1 > len(self.items):
            for _ in range((key + 1) * 2):
                self.items.append(-1)
        self.items[key] = value

    def get(self, key: int) -> int:
        if not self.contains(key):
            return -1

        return self.items[key]

    def remove(self, key: int) -> None:
        if not self.contains(key):
            return
        
        self.items[key] = -1

    def contains(self, key: int) -> bool:
        if key + 1 > len(self.items) or self.items[key] == -1:
            return False

        return True
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
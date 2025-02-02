class MyHashSet:
    def __init__(self):
        self.items = list()

    def add(self, key: int) -> None:
        if key + 1 > len(self.items):
            for _ in range((key + 1) * 2):
                self.items.append(False)
                
        self.items[key] = True

    def remove(self, key: int) -> None:
        if not self.contains(key):
            return

        self.items[key] = False

    def contains(self, key: int) -> bool:
        if key + 1 > len(self.items) or not self.items[key]:
            return False

        return True


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
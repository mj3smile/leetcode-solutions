class RandomizedSet:
    def __init__(self):
        self.items = list()
        self.valueIndex = dict()
        self.pointer = -1

    def insert(self, val: int) -> bool:
        if val in self.valueIndex:
            return False
        self.items.append(val)
        self.valueIndex[val] = len(self.items) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.valueIndex:
            return False
        index = self.valueIndex[val]
        lastIndex = len(self.items) - 1
        if index < lastIndex:
            self.items[index], self.items[lastIndex] = self.items[lastIndex], self.items[index]
            self.valueIndex[self.items[index]] = index
        
        if self.pointer + 1 == index:
            self.pointer += 1
        
        del self.valueIndex[self.items.pop()]
        return True

    def getRandom(self) -> int:
        # randomIndex = (self.pointer + 1) % len(self.items)
        # self.pointer = randomIndex
        return self.items[random.randint(0, len(self.items) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
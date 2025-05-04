class Value:
    def __init__(self):
        self.values = dict()
        self.timestamps = list()
        self.timestamps_cache = set()
    
    def set(self, value, timestamp):
        self.values[timestamp] = value
        if timestamp in self.timestamps_cache:
            return
        self.timestamps_cache.add(timestamp)
        self.timestamps.append(timestamp)
        self.timestamps.sort()
    
    def get(self, timestamp):
        # print(self.values)
        if timestamp in self.values:
            return self.values[timestamp]

        left, right = 0, len(self.timestamps) - 1
        if timestamp < self.timestamps[left]:
            return ""
        
        if timestamp > self.timestamps[right]:
            return self.values[self.timestamps[right]]

        while left < right:
            mid = (left + right) // 2

            if self.timestamps[mid] == timestamp:
                return self.values[self.timestamps[mid]]
            elif self.timestamps[mid] < timestamp:
                left = mid + 1
            else:
                right = mid - 1
        
        # print("final:", left)
        return self.values[self.timestamps[left - 1]]

class TimeMap:
    def __init__(self):
        self.storage = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        value_obj = Value()
        if key in self.storage:
            value_obj = self.storage[key]
        value_obj.set(value, timestamp)
        self.storage[key] = value_obj

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.storage:
            return ""
        print(key, timestamp)
        return self.storage[key].get(timestamp)
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
class Value:
    def __init__(self):
        self.values = dict()
        self.min_timestamp = 0
        self.max_timestamp = 0
        # self.timestamps = list()
        # self.timestamps_cache = set()
    
    def set(self, value, timestamp):
        self.values[timestamp] = value
        self.min_timestamp = min(self.min_timestamp, timestamp)
        self.max_timestamp = max(self.max_timestamp, timestamp)
        # if timestamp in self.timestamps_cache:
        #     return
        # self.timestamps_cache.add(timestamp)
        # self.timestamps.append(timestamp)
        # self.timestamps.sort()
    
    def get(self, timestamp):
        if timestamp in self.values:
            return self.values[timestamp]
        
        if timestamp < self.min_timestamp:
            return ""
        
        if timestamp > self.max_timestamp:
            return self.values[self.max_timestamp]

        for i in range(timestamp - 1, self.min_timestamp - 1, -1):
            if i in self.values:
                return self.values[i]
        
        return ""

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
        # print(key, timestamp)
        return self.storage[key].get(timestamp)
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
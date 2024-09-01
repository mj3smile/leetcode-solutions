class TimeMap:
    def __init__(self):
        self.values = dict()        # k: key, v: {timestamp: value}
        self.timestamps = dict()    # k: key, v: [timestamp1, timestampN...]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values[key] = self.values.get(key, {})
        self.values[key][timestamp] = value
        self.timestamps[key] = self.timestamps.get(key, [])
        self.timestamps[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.values:
            return ""
        
        timestamp = self.get_timestamp(key, timestamp)
        return self.values[key].get(timestamp, "")
    
    def get_timestamp(self, key, timestamp):
        if timestamp in self.values[key]:
            return timestamp
        
        if timestamp < self.timestamps[key][0]:
            return timestamp
        
        left, right = 0, len(self.timestamps[key]) - 1
        while left <= right:
            mid = (left + right) // 2
            
            if self.timestamps[key][mid] > timestamp:
                right = mid - 1
            else:
                left = mid + 1
        
        return self.timestamps[key][right]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
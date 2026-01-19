class TimeMap:
    def __init__(self):
        self.values = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.values:
            heap = list()
            heapq.heapify(heap)
            self.values[key] = heap

        heapq.heappush(self.values[key], (-timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.values:
            return ""
        
        # print(key, timestamp)
        poppedValues = list()
        largestTimestamp, value = heapq.heappop(self.values[key])
        poppedValues.append((largestTimestamp, value))
        while -largestTimestamp > timestamp and self.values[key]:
            largestTimestamp, value = heapq.heappop(self.values[key])
            poppedValues.append((largestTimestamp, value))
        
        while poppedValues:
            heapq.heappush(self.values[key], poppedValues.pop())
        
        if -largestTimestamp > timestamp:
            return ""
        
        return value

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
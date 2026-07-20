class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])

        empty = capacity
        end_location = trips[0][1]
        stops = list()

        for pax, start, end in trips:
            while stops and stops[0][0] <= start:
                release = heapq.heappop(stops)
                empty += release[1]

            if start >= end_location:
                end_location = end
                if pax > capacity:
                    return False
                empty = capacity - pax
                heapq.heappush(stops, [end, pax])
                continue

            if empty >= pax:
                empty -= pax
                end_location = max(end_location, end)
                heapq.heappush(stops, [end, pax])
                continue
            
            return False
        
        return True
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        previous_days = list()
        
        for today in range(len(temperatures)):
            while previous_days and temperatures[today] > temperatures[previous_days[-1]]:
                result[previous_days[-1]] = today - previous_days[-1]
                previous_days.pop()            
            previous_days.append(today)

        return result
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        result = 0
        left, right = 0, len(people) - 1

        while left <= right:
            total = people[left] + people[right]
            if total <= limit:
                left += 1
            
            right -= 1
            result += 1
        
        return result
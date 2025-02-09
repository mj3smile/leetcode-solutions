class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        result = 0
        # frequency = dict()
        # for n in range(len(people)):
        #     frequency[n] = frequency.get(n, 0) + 1
        
        people.sort()
        right = len(people) - 1
        cache = set()
        for left in range(len(people)):
            # if nums[left] in available_boats:
            #     result.append([people[left], available_boats[people[left]]])
            #     del available_boats[people[left]]
            #     continue
            if left > right + 1 and left not in cache:
                result += 1

            while right >= left:
                if left == right:
                    result += 1
                    cache.add(right)
                    right -= 1
                    break

                total = people[left] + people[right]
                if total > limit:
                    right -= 1
                else:
                    result += 1
                    cache.add(right)
                    right -= 1
                    break
        print("right:", right)
        
        return result
                

                
                

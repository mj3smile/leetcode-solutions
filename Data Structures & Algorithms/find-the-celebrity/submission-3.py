# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidates = set(list(range(n)))
        people_knows = dict()

        print
        for i in range(n):
            know_someone = False
            for j in range(n):
                if i == j:
                    continue
                if knows(i, j):
                    people_knows[j] = people_knows.get(j, 0) + 1
                    know_someone = True
            
            if know_someone:
                candidates.remove(i)
        
        if len(candidates) > 1:
            return -1
        for i in candidates:
            if people_knows.get(i, 0) == n - 1:
                return i

        return -1

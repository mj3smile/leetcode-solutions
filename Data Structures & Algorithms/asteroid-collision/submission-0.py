class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        right = list()
        left = deque()
        result = list()

        for a in asteroids:
            if a >= 0:
                right.append(a)
            else:
                left.append(a)

            while right and left:
                if right[-1] > -left[0]:
                    left.popleft()
                elif right[-1] < -left[0]:
                    right.pop()
                else:
                    left.popleft()
                    right.pop()
            
            while left:
                result.append(left.popleft())
        
        for i in range(len(right)):
            result.append(right[i])   
        
        # if right:
        #     return list(left)
        return result
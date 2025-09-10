class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.pairs = [[] for _ in range(numCourses)]
        self.cache = dict()

        for p in prerequisites:
            self.pairs[p[0]].append(p[1])
        
        # print("pairs:", self.pairs)
        for course in range(len(self.pairs)):
            # print("================")
            # print("course:", course)
            if not self.isCompletable(course, set()):
                return False
                
        return True
    
    def isCompletable(self, course, visited_course) -> bool:
        if course in visited_course:
            return False
        
        if course in self.cache:
            return self.cache[course]
        
        result = True
        visited_course.add(course)
        for prerequisite in self.pairs[course]:
            result = result and self.isCompletable(prerequisite, visited_course)
        visited_course.remove(course)
        self.cache[course] = result
        
        # print("course:", course, "visited:", visited_course, "result", result)
        return result

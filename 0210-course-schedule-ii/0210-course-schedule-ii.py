class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.numCourses = numCourses
        self.prereq = dict()
        self.result = list()
        self.cache = dict()

        for course, prerequisite in prerequisites:
            self.prereq[course] = self.prereq.get(course, list())
            self.prereq[course].append(prerequisite)
        
        for course in range(numCourses):
            self.takeCourse(course, set())
        
        return self.result

    def takeCourse(self, course, visited):
        if course in visited:
            return False
        
        if course in self.cache:
            return self.cache[course]
        
        visited.add(course)
        result = True
        for p in self.prereq.get(course, list()):
            result = result and self.takeCourse(p, visited)

        visited.remove(course)
        if result: self.result.append(course)
        self.cache[course] = result
        return result
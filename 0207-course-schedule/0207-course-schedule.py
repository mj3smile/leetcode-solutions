class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {i: [] for i in range(numCourses)}
        for c1, c2 in prerequisites:
            prereq[c1].append(c2)
        
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if prereq[course] == []:
                return True
            
            visited.add(course)
            for req in prereq[course]:
                if not dfs(req):
                    return False
            visited.remove(course)
            prereq[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True
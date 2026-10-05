class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adj[course].append(prereq)
        
        state = [0] * numCourses

        def has_cycle(course: int) -> bool:
            if state[course] == 1:
                return True
            elif state[course] == 2:
                return False
            
            state[course] = 1

            for prereq in adj[course]:
                if has_cycle(prereq):
                    return True
                
            state[course] = 2
            return False

        for course in range(numCourses):
            if has_cycle(course):
                return False
        return True
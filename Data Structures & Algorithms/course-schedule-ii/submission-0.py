class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}
        inDegree = [0]*numCourses
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            inDegree[course] += 1

        queue = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)
        
        taken = []
        while queue:
            take = queue.popleft()
            taken.append(take)
            for course in adj[take]:
                inDegree[course] -= 1

                if inDegree[course] == 0:
                    queue.append(course)
        
        return taken if len(taken) == numCourses else []
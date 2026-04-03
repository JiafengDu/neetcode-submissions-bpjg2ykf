class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}
        inDegree = [0] * numCourses
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            inDegree[course] += 1
        
        q = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)

        
        courses_taken = 0
        while q:
            curr_course = q.popleft()
            courses_taken += 1

            for next_course in adj[curr_course]:
                inDegree[next_course] -= 1
            
                if inDegree[next_course] == 0:
                    q.append(next_course)
        return courses_taken == numCourses
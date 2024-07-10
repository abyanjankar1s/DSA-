# Course Schedule
# You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

# Return true if it is possible to finish all courses, otherwise return false.

# Example 1:

# Input: numCourses = 2, prerequisites = [[0,1]]

# Output: true
# Explanation: First take course 0 (no prerequisites) and then take course 1.

# Example 2:

# Input: numCourses = 2, prerequisites = [[0,1],[1,0]]

# Output: false 

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prevMap = {i:[] for i in range(numCourses)} 
        for crs, pre in prerequisites:
            prevMap[crs].append(pre) 
        visit = set() 

        def dfs(crs):
            if prevMap[crs] == []:
                return True
            if crs in visit:
                return False
            
            visit.add(crs) 
            for pre in prevMap[crs]:
                if not dfs(pre): return False
            visit.remove(crs)
            prevMap[crs] = [] 
            return True 
        
        for c in range(numCourses):
            if not dfs(c): return False
        return True 
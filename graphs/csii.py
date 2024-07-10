# You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

# Return a valid ordering of courses you can take to finish all courses. If there are many valid answers, return any of them. If it's not possible to finish all courses, return an empty array.

# Example 1:

# Input: numCourses = 3, prerequisites = [[1,0]]

# Output: [0,1,2]

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)} 
        for crs, pre in prerequisites:
            preMap[crs].append(pre) 
        visit, cycle = set(), set() 
        res = [] 

        def dfs(crs):
            if crs in cycle:
                return False 
            if crs in visit:
                return True 
            
            cycle.add(crs)
            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False 
            cycle.remove(crs) 
            visit.add(crs) 
            res.append(crs) 
            return True 
        for c in range(numCourses):
            if dfs(c) == False: return []
        return res 
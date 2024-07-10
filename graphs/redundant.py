# Redundant Connection
# You are given a connected undirected graph with n nodes labeled from 1 to n. Initially, it contained no cycles and consisted of n-1 edges.

# We have now added one additional edge to the graph. The edge has two different vertices chosen from 1 to n, and was not an edge that previously existed in the graph.

# The graph is represented as an array edges of length n where edges[i] = [ai, bi] represents an edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the graph is still a connected non-cyclical graph. If there are multiple answers, return the edge that appears last in the input edges.

# Example 1:



# Input: edges = [[1,2],[1,3],[3,4],[2,4]]

# Output: [2,4] 

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges)+1) 

        def find(n1):
            res = n1 
            if res != par[res]:
                par[res] = par[par[res]] 
                res = par[res] 
            return res 
        
        def union(n1,n2):
            p1,p2 = find(n1), find(n2) 
            if p1 == p2:
                return False 
            
            if rank[p2] > rank[p1]:
                par[p1] = p2 
                rank[p2] += rank[p1] 
            else:
                par[p2] = p1 
                rank[p1] += rank[p2] 
            return True 

        for a,b in edges:
            if not union(a,b):
                return [a,b] 
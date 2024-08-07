# Task Scheduling
# You are given an array of CPU tasks tasks, where tasks[i] is an uppercase english character from A to Z. You are also given an integer n.

# Each CPU cycle allows the completion of a single task, and tasks may be completed in any order.

# The only constraint is that identical tasks must be separated by at least n CPU cycles, to cooldown the CPU.

# Return the minimum number of CPU cycles required to complete all tasks.

# Example 1:

# Input: tasks = ["X","X","Y","Y"], n = 2

# Output: 5

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks) 
        maxheap = [-c for c in count.values()]  
        heapq.heapify(maxheap) 

        time = 0 
        q = deque() 
        while maxheap or q:
            time += 1 

            if not maxheap:
                time = q[0][1]
            else:
                c = 1 + heapq.heappop(maxheap)
                if c:
                    q.append([c, time+n]) 
            if q and time == q[0][1]:
                heapq.heappush(maxheap, q.popleft()[0]) 
        
        return time 
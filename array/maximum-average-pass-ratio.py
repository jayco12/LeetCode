from heapq import heappush, heappop
from typing import List

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(pass_students, total_students):
            return (pass_students + 1) / (total_students + 1) - pass_students / total_students
        
        max_heap = []
        for passes, total in classes:
            heappush(max_heap, (-gain(passes, total), passes, total))
        
        for _ in range(extraStudents):
            current_gain, passes, total = heappop(max_heap)
            passes += 1
            total += 1
            heappush(max_heap, (-gain(passes, total), passes, total))
        
        total_ratio = 0
        for _, passes, total in max_heap:
            total_ratio += passes / total
        
        return total_ratio / len(classes)

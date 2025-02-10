class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[0])
        
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            last_start, last_end = result[-1]
            
            if start <= last_end:  
                result[-1][1] = max(last_end, end)
            else: 
                result.append(intervals[i])
        return result
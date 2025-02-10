class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        current=0
        result=[]
        for i in range(len(intervals)):
            start=intervals[i][0]
            end=intervals[i][0]
            if intervals[i][0]<=intervals[i-1][1]:
                result.append([intervals[i-1][0], intervals[i][1]])
            else:
                result.append(intervals[i])
        return result[1::]
        
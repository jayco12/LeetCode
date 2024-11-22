class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        count=1
        for i in range(len(matrix)-1):
            for j in range(i):
                if matrix[i]!=matrix[j]:
                    count+=1
        return count


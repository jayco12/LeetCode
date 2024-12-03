class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        n=len(height)
        count=0

        for i in range(n):
            for j in range(i + 1, n): 
                count = max(count, min(height[i], height[j]) * (j - i))

        return count

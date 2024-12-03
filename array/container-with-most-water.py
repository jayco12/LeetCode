class Solution:
    def maxArea(self, height: List[int]) -> int:
        count=0
        for i in range(len(height)):
            for j in range(len(height)-1):
                
                count=max(count, min(height[i], height[j])*(i-j))
            i+=1

        return count

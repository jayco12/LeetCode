class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        seen=set()
        for num in nums:
            seen.add(num)
            if original in seen:
               original*=2
            
        return original
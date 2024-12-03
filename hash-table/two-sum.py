class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start= 0
        result=[]
        n=len(nums)
        for start in range(n):
            for stop in range(start + 1, n):
                m=nums[start]+nums[stop]
                if m==target:
                    result.append(start)
                    result.append(stop)
        return result
       

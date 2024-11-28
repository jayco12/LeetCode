class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count=[1] * len(nums)
        pro=1
        for i in range(len(nums)):
            count[i] *= pro
            pro *= nums[i]
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            count[i] *= right
            right *= nums[i]
    
        return count
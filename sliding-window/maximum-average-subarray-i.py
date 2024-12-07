class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        s = sum(nums[:k])
        max_sum = s
        if k==1:
            return nums[0]
        for i in range(k,n):
            s += nums[i] - nums[i - k]
            max_sum = max(max_sum, s)

        return max_sum/k

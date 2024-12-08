class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums=sorted(nums)
        n=len(nums)

        for i in range(n):
            if i ==n-k:
                return nums[i]
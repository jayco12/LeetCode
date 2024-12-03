class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        count=0
        seen=set()

        for num in nums:
            count=max(count, num)
        for i in range(len(nums)):
            if  i != nums.index(count) and count< 2 * nums[i]:
                return -1
        return nums.index(count)
                
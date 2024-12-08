class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen=list(set(nums))
        if sorted(seen)==sorted(nums):
            return False
        return  True
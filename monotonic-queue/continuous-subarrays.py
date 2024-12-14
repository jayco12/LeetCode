class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        i = sub = 0
        seen = dict()
        for j, num in enumerate(nums):
            t = seen.copy()
            for char, freq in t.items():
                if abs(char - num) > 2:
                    i = max(i, freq + 1)
                    seen.pop(char)
            seen[num] = j
            sub += j - i + 1
        return sub
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        line=defaultdict(int)
        for n in nums:

            line[n-k]+=1
            line[n+k+1]-=1

        return max(accumulate(line[k] for k in sorted(line.keys())))
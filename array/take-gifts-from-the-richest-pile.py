class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        for _ in range(k):
            max_val=max(gifts)
            max_index=gifts.index(max_val)


            gifts[max_index]=floor(math.sqrt(max_val))
        return int(sum(gifts))

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts=sorted(gifts)
        print(gifts)
        remainder=[]
        s=0
        for i in range(len(gifts)):
            remainder.append(math.sqrt(gifts[i]))
        for j in range(len(remainder)-k, len(remainder)):
            s+=remainder[j]
            print(remainder[j])
        return int(s)

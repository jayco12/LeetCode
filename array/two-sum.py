class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        it = iter(nums)
        a = next(it, None)
        result=[]
        for x in it:
         result.append(a + x)
         t=nums.index(a)
         l=nums.index(x)
        for m in result:
            if m==target:
                i=result.index(m)
                print(t)
                print(l)
                print(i)
       

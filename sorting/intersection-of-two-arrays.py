class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s=set(nums1)
        result=[]
        for i in range(len(nums2)):
            if nums2[i] in s:
                result.append(nums2[i])

        return list(set(result))
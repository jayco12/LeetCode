class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        seen=set(nums1)
        dic=set(nums2)
        lis1=[]
        lis2=[]

        for i in range(len(nums1)):
            if nums1[i] not in dic:
                lis1.append(nums1[i])
        for i in range(len(nums2)):
            if nums2[i] not in seen:
                lis2.append(nums2[i])
        return [list(set(lis1)), list(set(lis2))]


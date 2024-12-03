class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count=0
        i=0
        freq = {}
        j=len(nums)-1
        

        while i < j:
            current_sum = nums[i] + nums[j]
            if current_sum == k:
                count += 1
                nums.pop(j)  # Remove the larger element first
                nums.pop(i)  # Then remove the smaller element
                j -= 2  # Adjust the pointer for the two removed elements
            elif current_sum < k:
                i += 1  # Move the left pointer to try increasing the sum
            else:
                j -= 1 
        return count
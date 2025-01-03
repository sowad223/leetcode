from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)  # Calculate the total sum of the array
        left_sum = 0  # To keep track of the sum of the left subarray
        valid_splits = 0  # Counter for valid splits

        # Iterate through the array except the last element
        for i in range(len(nums) - 1):
            left_sum += nums[i]  # Update the left sum
            right_sum = total_sum - left_sum  # Calculate the right sum
            if left_sum >= right_sum:  # Check the condition for valid split
                valid_splits += 1
        
        return valid_splits

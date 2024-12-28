from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # Step 1: Calculate the sum of every subarray of length k
        sums = [0] * (n - k + 1)
        current_sum = sum(nums[:k])
        sums[0] = current_sum
        for i in range(1, len(sums)):
            current_sum += nums[i + k - 1] - nums[i - 1]
            sums[i] = current_sum
        
        # Step 2: Create left and right arrays
        left = [0] * len(sums)
        right = [0] * len(sums)
        
        # Fill left array with the best indices for the leftmost subarray
        best = 0
        for i in range(len(sums)):
            if sums[i] > sums[best]:
                best = i
            left[i] = best
        
        # Fill right array with the best indices for the rightmost subarray
        best = len(sums) - 1
        for i in range(len(sums) - 1, -1, -1):
            if sums[i] >= sums[best]:  # Use >= to ensure lexicographical order
                best = i
            right[i] = best
        
        # Step 3: Find the maximum sum by iterating through the middle subarray
        max_sum = 0
        result = []
        for j in range(k, len(sums) - k):
            l, r = left[j - k], right[j + k]
            total = sums[l] + sums[j] + sums[r]
            if total > max_sum:
                max_sum = total
                result = [l, j, r]
        
        return result

        
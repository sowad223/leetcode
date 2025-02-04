from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        return self.divide_and_conquer(nums, 0, len(nums) - 1)

    def divide_and_conquer(self, nums: List[int], left: int, right: int) -> int:
        if left == right:
            return nums[left]

        mid = (left + right) // 2

        left_max = self.divide_and_conquer(nums, left, mid)
        right_max = self.divide_and_conquer(nums, mid + 1, right)
        cross_max = self.max_crossing_sum(nums, left, mid, right)

        return max(left_max, right_max, cross_max)

    def max_crossing_sum(self, nums: List[int], left: int, mid: int, right: int) -> int:
        left_sum = nums[mid]
        temp_sum = nums[mid]
        for i in range(mid - 1, left - 1, -1):
            if nums[i] < nums[i + 1]:
                temp_sum += nums[i]
                left_sum = max(left_sum, temp_sum)
            else:
                break

        right_sum = nums[mid + 1]
        temp_sum = nums[mid + 1]
        for i in range(mid + 2, right + 1):
            if nums[i] > nums[i - 1]:
                temp_sum += nums[i]
                right_sum = max(right_sum, temp_sum)
            else:
                break

        if nums[mid] < nums[mid + 1]:
            return left_sum + right_sum
        else:
            return max(left_sum, right_sum)

class Solution:
    def findDifferentBinaryString(self, nums):
        n = len(nums)
        return "".join('1' if nums[i][i] == '0' else '0' for i in range(n))

        
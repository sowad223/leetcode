from collections import defaultdict

class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = (n * (n - 1)) // 2
        good = 0
        freq = defaultdict(int)

        for i, num in enumerate(nums):
            diff = num - i
            good += freq[diff]
            freq[diff] += 1

        return total - good


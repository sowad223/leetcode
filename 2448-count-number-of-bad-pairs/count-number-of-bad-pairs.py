from collections import Counter
from sortedcontainers import SortedDict

class Solution(object):
    def countBadPairs(self, nums):
        transformed = [nums[i] - i for i in range(len(nums))]
        total_pairs = (len(nums) * (len(nums) - 1)) // 2
        
        freq = SortedDict()
        good_pairs = 0
        
        for val in transformed:
            if val in freq:
                good_pairs += freq[val]
            freq[val] = freq.get(val, 0) + 1
        
        return total_pairs - good_pairs


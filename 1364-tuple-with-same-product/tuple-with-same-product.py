from collections import defaultdict
from typing import List

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        map = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]

                map[product] += 1
        count = 0
        for value in map.values():
         
            count += value * (value - 1) * 4  
        
        return count

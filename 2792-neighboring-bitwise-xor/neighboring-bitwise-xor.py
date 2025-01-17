from typing import List

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        
        def is_valid(start_value: int) -> bool:
            original = [start_value]
            for i in range(1, n):
                original.append(derived[i - 1] ^ original[i - 1])
            return original[-1] ^ original[0] == derived[-1]
        
        return is_valid(0) or is_valid(1)

from typing import List

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        
        def is_valid(start_value: int) -> bool:
            current = start_value
            for i in range(n - 1):
                current = derived[i] ^ current
            return (derived[-1] ^ current) == start_value
        
        sorted_derived = sorted(derived)
        return is_valid(0) or is_valid(1)

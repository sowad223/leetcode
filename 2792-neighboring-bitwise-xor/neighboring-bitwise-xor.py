from typing import List

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        
 
        def is_valid(start_value: int) -> bool:
            original = [0] * n
            original[0] = start_value
            for i in range(1, n):
                original[i] = derived[i - 1] ^ original[i - 1]
            
            return original[n - 1] ^ original[0] == derived[n - 1]
        
      
        return is_valid(0) or is_valid(1)

from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1) 
        
      
        for start, end, direction in shifts:
            shift_value = 1 if direction == 1 else -1
            diff[start] += shift_value
            diff[end + 1] -= shift_value
        
       
        net_shifts = [0] * n
        current_shift = 0
        for i in range(n):
            current_shift += diff[i]
            net_shifts[i] = current_shift
        

        result = []
        for i in range(n):
            original_char = s[i]
            shift = net_shifts[i]
            new_char = chr((ord(original_char) - ord('a') + shift) % 26 + ord('a'))
            result.append(new_char)
        
        return ''.join(result)

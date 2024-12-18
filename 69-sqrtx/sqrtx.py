class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:  
            return x
    
        left, right = 0, x
        result = 0
        
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                result = mid  
                left = mid + 1 
            else:
                right = mid - 1  
        
        return result
            
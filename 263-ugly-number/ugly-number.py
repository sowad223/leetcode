class Solution:
    def isUgly(self, n: int) -> bool:

        if n <= 0:
            return False
        
        
        while True:
            if n == 1:
                return True
            if n - (n // 2) * 2 != 0:
                break
            n = n // 2
        
    
        while True:
            if n == 1:
                return True
            if n - (n // 3) * 3 != 0:
                break
            n = n // 3
        

        while True:
            if n == 1:
                return True
            if n - (n // 5) * 5 != 0:
                break
            n = n // 5
        
 
        return n == 1
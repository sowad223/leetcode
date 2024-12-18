class Solution:
    def reverse(self, x: int) -> int:
        int_min,int_max=-2**31,(2**31)-1
        sign = -1 if x < 0 else 1
        x_str = str(abs(x))
        reversed_x = int(x_str[::-1])
    

        reversed_x *= sign
    
        if reversed_x < int_min or reversed_x > int_max:
            return 0
    
        return reversed_x
        
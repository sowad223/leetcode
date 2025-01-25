class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:  
            j = str(num)  
            total = 0     
            for i in range(len(j)):  
                total += int(j[i])   
            num = total  
        return num 
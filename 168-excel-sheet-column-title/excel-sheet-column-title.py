class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  
        result = ""
        while columnNumber > 0:
            columnNumber -= 1 
            remainder = columnNumber % 26
            result = alphabet[remainder] + result 
            columnNumber //= 26
        return result


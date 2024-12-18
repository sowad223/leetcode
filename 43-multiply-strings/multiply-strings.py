class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n=0
        num3=0
  
        for i in num1:
            n = n * 10 + (ord(i) - 48) 
        for i in num2:
            num3=num3*10+(ord(i)-48)
        k=n*num3
        j=str(k)
        return j

        
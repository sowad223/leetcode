class Solution:
    def hammingWeight(self, n: int) -> int:
        k=bin(n)[2:]
        count=0
        for i in range(len(k)):
            if k[i]=="1":
                count+=1
        return count

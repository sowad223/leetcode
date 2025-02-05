from sortedcontainers import SortedList

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        
        mismatch = SortedList()  
        
        for i in range(len(s1)): 
            if s1[i] != s2[i]:
                mismatch.add(i)
        
        if len(mismatch) != 2:
            return False
        
        i, j = mismatch
        return s1[i] == s2[j] and s1[j] == s2[i] 


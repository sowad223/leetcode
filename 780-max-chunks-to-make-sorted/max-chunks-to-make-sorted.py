class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_seen = [] 
        chunks = 0  

        for i in range(len(arr)):
            value = arr[i]  
            if max_seen:
                max_seen.append(max(max_seen[-1], value)) 
            else:
                max_seen.append(value)  

            if max_seen[-1] == i: 
                chunks += 1  

        return chunks  

            
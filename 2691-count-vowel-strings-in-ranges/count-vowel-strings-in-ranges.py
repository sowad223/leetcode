from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # Precompute the prefix sum array for the strings that start and end with vowels
        prefix_sum = [0] * (len(words) + 1)
        
        for i in range(len(words)):
            # Check if the word starts and ends with a vowel
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefix_sum[i + 1] = prefix_sum[i] + 1
            else:
                prefix_sum[i + 1] = prefix_sum[i]
        
        # Answer each query
        ans = []
        for li, ri in queries:
            # Use the prefix sum array to find the count in the range
            ans.append(prefix_sum[ri + 1] - prefix_sum[li])
        
        return ans

        
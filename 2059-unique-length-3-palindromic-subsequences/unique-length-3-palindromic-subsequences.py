class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        result = set()
        left_seen = set()
        right_counts = [0] * 26
        
        for char in s:
            right_counts[ord(char) - ord('a')] += 1
        
        for i in range(n):
            current_char = s[i]
            right_counts[ord(current_char) - ord('a')] -= 1
            
            for middle_char in range(26):
                if chr(middle_char + ord('a')) in left_seen and right_counts[middle_char] > 0:
                    result.add((current_char, chr(middle_char + ord('a')), current_char))
            
            left_seen.add(current_char)
        
        return len(result)

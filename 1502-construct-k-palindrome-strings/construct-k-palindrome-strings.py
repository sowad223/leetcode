class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        # If k is greater than the length of s, it's impossible to form k palindromes
        if k > len(s):
            return False
        
        # Count the frequency of each character
        from collections import Counter
        char_count = Counter(s)
        
        # Count how many characters have an odd frequency
        odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
        
        # We can form at least odd_count palindromes, and at most len(s) palindromes
        # If k is between odd_count and len(s), it's possible
        return odd_count <= k

        
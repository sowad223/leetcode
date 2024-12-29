from typing import List

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        word_len = len(words[0])
        target_len = len(target)

        # Precompute the count of each character at each position in words
        char_count = [[0] * 26 for _ in range(word_len)]
        for word in words:
            for i, char in enumerate(word):
                char_count[i][ord(char) - ord('a')] += 1

        # dp[j] represents the number of ways to form target[0..j]
        dp = [0] * (target_len + 1)
        dp[0] = 1  # There's exactly one way to form an empty prefix

        # Iterate through the columns of words
        for i in range(word_len):
            # Update dp array from back to front to avoid overwriting
            for j in range(target_len - 1, -1, -1):
                char = target[j]
                if char_count[i][ord(char) - ord('a')] > 0:
                    dp[j + 1] += dp[j] * char_count[i][ord(char) - ord('a')]
                    dp[j + 1] %= MOD

        return dp[target_len]

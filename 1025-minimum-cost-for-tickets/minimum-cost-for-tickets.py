from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # Create a set for faster lookup of travel days
        travel_days = set(days)
        # Create a DP array for all 365 days
        dp = [0] * 366  # dp[i] represents the minimum cost to travel up to day i

        for i in range(1, 366):  # Loop through each day of the year
            if i not in travel_days:
                # If it's not a travel day, cost remains the same as the previous day
                dp[i] = dp[i - 1]
            else:
                # Minimum of 1-day, 7-day, or 30-day pass
                dp[i] = min(
                    dp[max(0, i - 1)] + costs[0],   # 1-day pass
                    dp[max(0, i - 7)] + costs[1],   # 7-day pass
                    dp[max(0, i - 30)] + costs[2]   # 30-day pass
                )

        # The answer is the cost to travel up to the last travel day
        return dp[365]

        
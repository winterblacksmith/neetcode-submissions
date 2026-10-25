class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(remaining):
            if remaining == 0:
                return 0
            if remaining in memo:
                return memo[remaining]
            best = float('inf')
            for coin in coins:
                if coin <= remaining:
                    best = min(best, 1 + dfs(remaining - coin))
            memo[remaining] = best
            return best
        result = dfs(amount)
        return -1 if result == float('inf') else result
        
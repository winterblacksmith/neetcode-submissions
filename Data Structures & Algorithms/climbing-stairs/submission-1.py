class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [None] * n
        def dfs(i):
            if i == n:
                return 1
            if i > n:
                return 0
            elif cache[i] is not None:
                return cache[i]
            else:
                cache[i] = dfs(i+1) + dfs(i+2)
                return cache[i]
        return dfs(0)
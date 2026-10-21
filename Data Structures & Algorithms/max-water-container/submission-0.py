class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxAmount = 0
        while l < r:
            amount = (r - l) *  min(heights[l], heights[r])
            maxAmount = max(maxAmount, amount)
            if heights[l] <= heights[r]: 
                l += 1
            else: 
                r -= 1
        return maxAmount
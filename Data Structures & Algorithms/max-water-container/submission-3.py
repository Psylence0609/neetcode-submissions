class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        ans = 0
        while l < r:
            ans = max(ans, min(heights[l], heights[r]) * (r - l))
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        return ans
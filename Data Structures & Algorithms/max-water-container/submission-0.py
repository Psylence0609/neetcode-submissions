class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_vol = 0
        i = 0
        j = len(heights) - 1
        while i < j:
            max_vol = max(max_vol, min(heights[i], heights[j]) * (j - i))
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        return max_vol
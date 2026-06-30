class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        highest = 0
        while r > l:
            area = min(heights[r], heights[l]) * (r - l)
            highest = max(highest, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return highest
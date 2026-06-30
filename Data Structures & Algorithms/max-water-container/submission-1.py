class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        highest = 0
        for l in range(len(heights)):
            r = l + 1
            while r < len(heights):
                area = min(heights[r], heights[l]) * (r - l)
                if area > highest:
                    highest = area
                r += 1
        return highest
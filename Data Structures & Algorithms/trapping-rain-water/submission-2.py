class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        for i in range(1, len(height) - 1):
            level = min(max(height[0:i]), max(height[i+1:]))
            if height[i] < level:
                water += level - height[i]
        return water

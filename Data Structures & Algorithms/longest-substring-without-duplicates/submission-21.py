class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        right = 0
        longest = 0
        seen = {}

        for right, char in enumerate(s):
            if char in seen and seen[char] >= left:
                left = seen[char] + 1
            seen[char] = right
            longest = max(longest, right - left + 1)
        return longest
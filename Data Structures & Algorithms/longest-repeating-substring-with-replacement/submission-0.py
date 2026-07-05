class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        left = 0
        longest = 0
        for right, char in enumerate(s):
            seen[char] = seen.get(char, 0) + 1
            if ((right - left + 1) - max(seen.values())) > k:
                seen[s[left]] -= 1
                left += 1
                

            
            longest = max(longest, right - left + 1)
        return longest
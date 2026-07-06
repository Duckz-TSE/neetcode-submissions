class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        left = 0
        length = len(s1)
        right = left + length
        seen = {}
        for char in s1:
            seen[char] = seen.get(char, 0) + 1
        
        window = s2[left : (left + length)]
        window_count = {}
        for char in window:
            window_count[char] = window_count.get(char, 0) + 1
        if window_count == seen: return True

        for right in range(length, len(s2)):
            window_count[s2[right]] = window_count.get(s2[right], 0) + 1
            window_count[s2[right - length]] -= 1
            if window_count[s2[right - length]] == 0:
                del window_count[s2[right - length]]
            if window_count == seen:
                return True

        return False   
            

      
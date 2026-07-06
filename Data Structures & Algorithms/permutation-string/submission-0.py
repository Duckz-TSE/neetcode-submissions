class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        length = len(s1)
        seen = {}
        for char in s1:
            seen[char] = seen.get(char, 0) + 1

        for left, char in enumerate(s2):
            window = s2[left : (left + length)]
            window_count = {}
            for char in window:
                window_count[char] = window_count.get(char, 0) + 1
            if window_count == seen:
                return True
        return False   
            

      
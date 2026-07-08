class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        length = len(s1)
        right = length
        seen = {}
        windowseen = {}
        for char in s1:
            seen[char] = seen.get(char, 0) + 1

        initialwindow = s2[0:length]   
        for char in initialwindow:
            windowseen[char] = windowseen.get(char, 0) + 1
        if windowseen == seen: return True

        while right < len(s2):
            windowseen[s2[right]] = windowseen.get(s2[right], 0) + 1

            windowseen[s2[right - length]] -= 1
            if windowseen[s2[right - length]] == 0:
                del windowseen[s2[right - length]]
            if windowseen == seen: return True
            right += 1


        return False